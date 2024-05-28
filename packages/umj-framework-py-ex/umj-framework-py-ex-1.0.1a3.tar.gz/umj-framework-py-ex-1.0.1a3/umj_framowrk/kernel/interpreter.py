from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
)
from kernel.common import get_object_type
from asyncio import run
from dill import load
from pathlib import Path
import logging


INTERPRETER_CON_KEY = 'intepr_data'


class Interpreter():
    def __init__(self, bundle: Path | str | dict):
        print('Starting to init interpreter...')
        if not bundle:
            raise ValueError("Bundle wasn't applied.")

        self.bundle = bundle
        if type(bundle) != dict:
            with open(bundle, 'rb') as file:
                self.bundle = load(file)

        self.windows = self.bundle.get('_windows_initials')
        self.mounts = self.bundle.get('_bundle')
        if not self.mounts:
            raise ValueError('Bundle has no mounts.')

        self.mounted_bots = self.bundle.get('_bots')
        if not self.mounted_bots:
            raise ValueError("Bundle has no bot's mountpoints.")

        print('Interpreter successfully initiated.')

    def start(self) -> None:
        for key, values in self.mounted_bots.items():
            values[0] = Bot(token=values[0])

            obj = Dispatcher(bot=values[0], storage=MemoryStorage())
            obj.message.register(self.process_message)
            obj.callback_query.register(self.process_action)
            values[1] = obj

            print('Starting polling...')
            run(obj.start_polling(values[0]))

    # Inits user's window messages ids storage:
    async def _set_window_data(self, state: FSMContext) -> None:
        data = await state.get_data()

        if INTERPRETER_CON_KEY not in data:
            await state.update_data({INTERPRETER_CON_KEY: {}})

    # Returns bot's reactions on any commands:
    def get_bot_control(self, bot_obj: Bot) -> tuple[str, dict]:
        for name, (bot, *_) in self.mounted_bots.items():
            if bot == bot_obj:
                return name, self.mounted_bots.get(name)[-1]  # Last is it's commands reactions dict

        raise ValueError(f'Bot mount point for {bot_obj} not found.')

    # Incoming message entry point handler:
    async def process_message(self, message: Message, state: FSMContext) -> None:
        await self._set_window_data(state)

        name, control = self.get_bot_control(message.bot)
        msg_proc = control.get(message.text)

        async def handle_windows(action: str, handler):
            for window in msg_proc.get(action, []):
                if not self.windows.get(window) and action== 'mount':
                    raise ValueError(f'Specified {window} window in {name} bot not found.')
                await handler(message.bot, message.chat.id, state, window)

        await handle_windows('mount', self.mount_window)
        await handle_windows('unmount', self.unmount_window)

        for linear_view in control.get('linear', []):  # Cant short this boilerplate :(
            view_obj = self.mounts.get(linear_view)
            if not view_obj:
                raise ValueError(f'Specified {linear_view} view in {name} bot not found.')
            await self.draw_view(message.bot, message.chat.id, view_obj)

    # Incoming callback (and action in future) entry point handler:
    async def process_action(self, data: CallbackQuery | list[str, dict] | str, state: FSMContext) -> None:
        await self._set_window_data(state)
        context_data = (await state.get_data())[INTERPRETER_CON_KEY]
        match data:
            # Первые два на самом деле не работают:
            case str():
                link = data
            case list():
                link, data = data
            case CallbackQuery():
                link = data.data


        addr_list = link.split('/')
        match addr_list[0]:
            case 'close_self' | 'cl_sf':
                await self.unmount_window(data.bot, data.message.chat.id, state, data.message.message_id)
            case 'close' | 'cl':
                await self.unmount_window(data.bot, data.message.chat.id, state, addr_list[1])
            case 'open' | 'op':
                await self.mount_window(data.bot, data.message.chat.id, state, addr_list[1])
            case command if command in ['set', 'set_self', 'set_sf']:
                addr = '/'.join(addr_list[1:])
                obj = self.mounts.get(addr) or self.mounts.get('/'.join(addr_list[2:]))

                if callable(obj):
                    obj()
                    return
                def walk_call(obj):
                    for call in obj:
                        if type(call) == list:
                            walk_call(call)
                        elif callable(call):
                            call()

                if get_object_type(obj) == 'scenario':
                    walk_call(obj)
                    return

                print(link)
                window_id = context_data.get(addr_list[1])
                #
                #
                # if command != 'set':
                #     # Case when window not specified:
                #     window_id = data.message.message_id
                #     for key, val in context_data.items():
                #         if val == int(window_id):
                #             view = self.windows[key]['views'].get(addr_list[1])

                # print('/'.join(addr_list[1:]))
                await self.draw_view(
                    data.bot,
                    data.message.chat.id,
                    obj,
                    message_id=window_id
                )
            case _:
                print(link)
                raise ValueError(f'Action {link} has incorrect type: {command}')

    # Displaying view function:
    async def draw_view(self, bot: Bot, chat_id: int, view: list, message_id=None) -> int | None:
        buttons = []
        text = ''

        def add_btns(btn_list: InlineKeyboardButton):
            if len(view) <= 2:
                for btn in btn_list:
                    buttons.append([btn])
            else:
                buttons.append(btn_list)

        def walk_dict(btns: dict):
            return [InlineKeyboardButton(text=name, callback_data=link) for name, link in btns.items()]

        for i, view_elem in enumerate(view):
            # first is text message:
            if i == 0:
                if type(view_elem) == list:
                    ...
                else:
                    text = view_elem
                continue

            btns_group = []

            match view_elem:
                case list():
                    for btn_dict in view_elem:
                        btns_group.extend(walk_dict(btn_dict))
                case dict():
                    btns_group.extend(walk_dict(view_elem))
            add_btns(btns_group)

        # print(buttons)
        keyboards = InlineKeyboardMarkup(inline_keyboard=buttons)
        if message_id:
            await bot.edit_message_text(chat_id=chat_id, message_id=message_id,
                                        text=text, reply_markup=keyboards)
        else:
            return (await bot.send_message(chat_id, text, reply_markup=keyboards)).message_id

    # Processing mounts and unmounts:
    async def mount_window(self, bot: Bot, chat_id: int, state: FSMContext, window_name: str, window_alias: str = None) -> None:
        try:
            view_name = self.windows[window_name].get('initial')
        except KeyError:
            print('Window not found')

        view = self.mounts.get(window_name+'/'+view_name) #!!!!
        if not view:
            raise ValueError(f'{view_name} view not found in {window_name}.')

        if not window_alias:
            await self.unmount_window(bot, chat_id, state, window_name)

        interpreter_data = (await state.get_data())[INTERPRETER_CON_KEY]
        interpreter_data[window_alias or window_name] = await self.draw_view(bot, chat_id, view)

        await state.update_data({INTERPRETER_CON_KEY: interpreter_data})

    async def unmount_window(self, bot: Bot, chat_id: int, state: FSMContext, window_name: str | int) -> None:
        data = (await state.get_data())[INTERPRETER_CON_KEY]
        try:
            # print('trying')
            delete_id = int(window_name)
            for key, value in data.items():
                if value == delete_id:
                    window_name = key
                    break
        except Exception:
            delete_id = data.get(window_name)

        if delete_id:
            del data[window_name]
            await state.update_data(intepr_data=data)
            await bot.delete_message(chat_id, delete_id)
