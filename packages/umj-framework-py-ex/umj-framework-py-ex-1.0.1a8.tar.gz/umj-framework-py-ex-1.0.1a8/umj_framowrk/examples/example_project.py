from umj_framowrk import Builder
from umj_framowrk import Interpreter


MAIN = {
    '_name': 'project1',
    '_version': '1.0.0',
    '_bots': {
        'MyBot': 'token',
    },
    'MyBot': {
        '/start': {
            'mount': ['window1', 'window2'],
            'unmount': ['help_window'],
        },
        '/help': {
            'mount': ['help_window']
        },
        '/understand': {
            'unmount': ['help_window']
        }
    },
    'global_scenario': [
        lambda: print('Первый вызов из глобального сценария'),
        lambda: print('Второй вызов из глобального сценария'),
    ],
    'global_view': [
        '''Глобальный вид''', {
            'Запуск глобального сценария': 'window2 -> global_scenario',
            'Закрыть себя': '-> close',
            'Установить в первом окне первый вид.': 'window1 -> Info1',
            'Установить во втором окне первый вид.': 'window2 -> Info1'
        }
    ],
    'help_window': {
        'initial': 'hlp',
        'views': {
            'hlp': [
                '''Окно помощи''', {
                    'Закрыть':  'help_window -> close',
                },
            ],
        }
    },
    'window1': {
        'initial': 'Info1',
        'views': {
            'Info1': [
                '''Первый вид первого окна''', {
                    'Вперед':  'window1 -> Info2',
                    'Целевая кнопка': lambda: print('Целевая кнопка первого вида первого окна выполнена'),
                    'Открытие вложенного вида':   [
                        '''Текст внутреннего вложеннного вида''', {
                            'Установить первый вид': 'set/window1/Info1',
                            'Установить второй вид': 'set/window1/Info2',
                            'Установить третий вид': 'set/window1/Info3'
                        }
                    ],
                    # 'Запуск глобального сценария': '-> global_scenario',
                    'Проверка мнб':
                        lambda: [
                            '''Внутри внутреннего возврата''', {
                                'BTN_ВОЗВРАТ':  'set/window1/Info2/',
                                'BTN_ВОЗВРАТ2': lambda: print('Целевая кнопка первого вида первого окна')
                            }
                        ]
                },
            ],
            'Info2': [
                '''Второй вид первого окна''', {
                    'Вперед': 'set/window1/Info3',
                    'Назад к первому виду': 'set/window1/Info1',
                    'Установить первый вид во втором окне': 'set/window2/Info1'
                }, {}
            ],
            'Info3': [
                '''Третий вид первого окна''', {
                    'Открыть копию себя': 'op/window1',
                    'Открыть копию второго окна': 'open/window2',
                    'Закрыть себя': 'cl_sf'
                }, {}
            ]
        }
    },
    'window2': {
        'initial': 'Info1',
        'views': {
            'Info1': [
                '''Первый вид второго окна''', {
                    'Открыть глобальный элем.': 'window2 -> global_view',
                    'Вперед': 'window2 -> Info2',
                    'Открыть первый вид в первом окне': 'window1->Info1',
                }, {}
            ],
            'Info2': [
                '''Второй вид второго окна''', {
                    # 'Открыть внешний view': 'window2 -> global_info',
                    'Закрыть себя': 'window2 -> close'
                }, {}
            ]
        }
    },
}


builder = Builder(MAIN, bundle_path='../', ) #  start_interpreter=True builder.get_bundle()
interpreter = Interpreter('./project1-1.0.0.umjpd')
interpreter.start()

# print('started')
# print(interpreter.bundle)
