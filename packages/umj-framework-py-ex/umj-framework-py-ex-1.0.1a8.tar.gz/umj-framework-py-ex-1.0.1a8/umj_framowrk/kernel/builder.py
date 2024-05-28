from aiogram import Bot
from aiogram.fsm.storage.memory import MemoryStorage, BaseStorage
from dinamic_py_loader import ModuleController
from .interpreter import Interpreter
from .common import get_object_type
from pathlib import Path
from asyncio import run
from dill import dump
from typing import Callable


# Defaults:
ENTRY = 'MAIN'
DEFAULT_STORAGE = MemoryStorage

# Errors:
DICT_FIELD_NOT_SPEC = 'The required dict filed {} is not specified in {}.'
DICT_WRONG_FILED = 'The specified dict field {} is incorrect in {}.'
WRONG_ACTION = 'The specified action in {} is wrong.'
LIST_FIELD_NOT_SPEC = 'The required list filed with index {} is not specified in {}.'
LIST_WRONG_FIELD = 'The specified list field with index {} is incorrect in {}.'
EMPTY_ERR = "The {} element can't be empty in {}."


class Builder():
    '''
    Is used to process notation to create bundle object.
    Can dump it in file using umjpd format.
    '''

    def __init__(self, source: Path | str | dict, start_interpreter: bool = None, bundle_path: Path | str = None):
        print('Starting to init builder.')

        module = ModuleController(source) if not type(source) == dict else {ENTRY: source}

        self.source = module.get(ENTRY)
        if not self.source:
            raise ValueError(f"Entry point not found, {ENTRY} global dict should be specified.")

        self.name = self.source.get('_name') or module.name
        self.version = self.source.get('_version') or '1.0.0'

        self.bots = self._mount_bots()

        self.call_before = self.source.get('_call_bef')
        self.call_after = self.source.get('_call_aft')

        self.windows_initials = self._parse_windows()   # Is used to mount windows in interpreter
                                               # There is no need to parse global views - they mounts automatically
        self.bundle = {}
        self.links_base = {}   # used to process same buttons names
        self._generate_bundle(self.source)

        if bundle_path:
            self._dump_bundle(bundle_path)

        print('Builder successfully initiated.')

        if start_interpreter:
            interpreter = Interpreter(self.get_bundle())
            interpreter.start()

    # Bots processing:
    def _mount_bots(self) -> dict[str, tuple[str, BaseStorage, dict]]:
        bots = self.source.get('_bots')
        if not bots:
            raise ValueError(DICT_FIELD_NOT_SPEC.format('_bots', ENTRY))

        return {
            name: self._mount_bot(name, settings)
            for name, settings in bots.items()
        }

    def _mount_bot(self, name: str, settings: list | str) -> list[str, str, object, dict]:
        storage = DEFAULT_STORAGE()
        key = settings

        if type(settings) == list:
            if len(settings) == 0:
                raise ValueError(EMPTY_ERR.format('settings list', f'_bots.{name} bot'))
            key = settings[0]
            storage = settings[1] if len(settings) > 1 else storage

        try:
            bot = Bot(token=key)
            run(bot.get_me())
        except:
            raise ValueError('{name} bot has incorrect token.')

        cmd_bindings = self.source.get(name)
        if not cmd_bindings:
            print(f'Bot {name} was initialised but not used')

        # The probem is Bot or Dispather objects cant be dumped with picle/dill:
        return [key, storage, cmd_bindings]

    # Parses global windows
    def _parse_windows(self):
        windows = {}
        for key, val in self.source.items():
            try:
                windows[key] = val
            except:
                pass
        return windows

    # Processing bundle walk:
    def _generate_bundle(self, module) -> None:
        for name, elem in module.items():
            if name[0] != '_' and name not in self.bots.keys():
                self._bundle_object(elem, name)

    # Lets to find component throughout namespace:
    def _bundle_related(self, link: str, prefix: str):
        # try:
        #     elements = link.replace(' ', '').split('/')
        #     for i, elem in enumerate(elements):
        #         keys = elem.split('.')
        #         print(keys)
        #         obj = self.bundle.get(keys[0])
        #         if obj:
        #             new_pref = '/'.join(keys)
        #             for key in keys:
        #                 obj = obj[key]
        #             self._bundle_object(obj, prefix=new_pref)
        #             elements[i] = new_pref
        #     return '/'.join(elements)
        # except KeyError:
        #     raise ValueError(DICT_WRONG_FILED.format(''))
        # return new_pref
        return prefix

    # Bundles any component:
    def _bundle_object(self, obj: dict | list | str | Callable, prefix: str) -> str | None:
        # Checks  element's type, bundles is and walks in.
        # Can return string to check action or mount in-build generated elements:
        obj_type = get_object_type(obj)

        match obj_type:
            case 'window':
                self._bundle_window(obj, prefix)
                return

            case 'view':
                self.bundle[prefix] = self._bundle_view(obj, prefix)
                return

            case 'scenario':
                self.bundle[prefix] = self._bundle_scenario(obj, prefix)
                return

            case 'action':
                link = self._bundle_related(obj, prefix)
                return self._format_action(obj, link)

            case 'func':
                try:
                    result = obj()  # to allow functional in-build generation
                    if result:
                        self._bundle_object(result, prefix=prefix)
                    else:
                        self.bundle[prefix] = obj
                except:
                    self.bundle[prefix] = obj
                print( 'set/'+ prefix)
                return 'set/'+ prefix
            case _:
                raise ValueError(f'{prefix} structure has incorrect format: {obj}.')

    # walking window:
    def _bundle_window(self, window: dict, prefix: str) -> None:
        views = window.get('views')
        if not views:
            raise ValueError(DICT_FIELD_NOT_SPEC.format('view', f'{prefix} window'))

        for name, view in views.items():
            link = prefix + '/' + name
            self.bundle[link] = self._bundle_view(view, link)

    # Updating links base to protect same buttons names errors:
    def _process_same_name_btn(self, prefix, btn_name) -> str:
        if prefix not in self.links_base:
            self.links_base[prefix] = set()

        btn_names = self.links_base[prefix]
        while btn_name in btn_names:
            btn_name += '_1'
        btn_names.add(btn_name)

        return btn_name

    # Walking view:
    def _bundle_view(self, view: list, prefix: str) -> dict:
        # Should be changed to process media!
        # Doesn't interpreter structure format, only creates buttons callbacks data:
        for i, elem in enumerate(view):
            match elem:
                case list():
                    # Checking list mesia:
                    if i == 0:
                        for i, sub_elem in enumerate(elem):
                            if i > 0 and not Path(sub_elem).resolve().is_file():
                                raise ValueError(LIST_WRONG_FIELD.format(i, f'{prefix}[{0}]'))
                    else:
                        self._bundle_view(view, prefix)
                case dict():
                    for btn_name, val in elem.items():
                        btn_name = self._process_same_name_btn(prefix, btn_name)

                        link = prefix + '/' + btn_name
                        calback_str = self._bundle_object(val, link)
                        elem[btn_name] = (calback_str or 'set/'+  link)    # calback_str only if there is action str or name key
        return view

    # Walking scenario:
    def _bundle_scenario(self, scenario: list, prefix: str) -> list:
        for i, elem in enumerate(scenario):
            match elem:
                case str():
                    elem = self.bundle_bundle_related(elem, prefix)
                    scenario[i] = self._format_action(elem)
                case list():
                    self._bundle_scenario(elem, prefix)
        return scenario

    def _format_action(self, alias: str, prefix: str) -> str:
        alias = alias.replace(' ', '')
        alias = alias.rstrip('/').lstrip('/')

        def proc_native(native_action):
            elem = native_action.split('/')

            if elem[0] not in [
                'set', 'set_self', 'set_sf',
                'open', 'op', 'close', 'cl', 'close_self', 'cl_sf',
                'action', 'act', 'act_self', 'act_sf'
            ]:
                raise ValueError(WRONG_ACTION.format(prefix))
            return native_action

        if alias.find('->') != -1:
            first, second = alias.split('->')
        else:
            return proc_native(alias)

        match second:
            case 'close' | 'cl':
                action_type = 'close_self' if not first else 'close'
            case 'open' | 'op':
                action_type = 'open'
            case _:
                action_type = 'set' if first else 'set_self'

        return action_type + ('/' + first if first else '') + '/' + second

    # Bundle processing:
    def get_bundle(self) -> dict:
        return {
            '_name': self.name,
            '_version': self.version,
            '_cal_bef': self.source.get('_cal_bef', []),
            '_call_aft': self.source.get('_cal_aft', []) + self.source.get('_cal', []),
            '_windows_initials': self.windows_initials,
            '_bots': self.bots,
            '_bundle': self.bundle
        }

    # Dumping:
    def _dump_bundle(self, path: Path | str) -> None:
        path = Path(path).resolve() / f'{self.name}-{self.version}.umjpd'

        file_data = self.get_bundle()
        with open(path, 'wb') as file:
            dump(file_data, file)
