## Данный файл содержит настройки, способные изменить вашу игру.
##
## Строки, начинающиеся  с двух '#' — комментарии, и вы не должны их
## раскомментировать. Строки, начинающиеся с одной '#' — комментированный код,
## который вы можете раскомментировать, если посчитаете это нужным.


## Основное ####################################################################

## Читаемое название игры. Используется при установке стандартного заголовка
## окна, показывается в интерфейсе и отчётах об ошибках.
##
## Символы "_()", окружающие название, отмечают его как пригодное для перевода.

define config.name = _("SkeetRemaster")

define config.default_textshader = "zoom"
default preferences.gl_powersave = False

define config.layers = [ 'master', 'transient', 'screens', 'overlay', 'front' ]

define config.image_cache_size = 64
define config.predict_statements = 50
define config.menu_clear_layers = ["front"]
## Определяет, показывать ли заголовок, данный выше, на экране главного меню.
## Установите на False, чтобы спрятать заголовок.

define gui.show_name = False


## Версия игры.

define config.version = "1.0"
define sr_version = "2.10.2024"

## Текст, помещённый в экран "Об игре". Поместите текст между тройными скобками.
## Для отделения абзацев оставляйте между ними пустую строку.

define gui.about = _p("""Сваял эту хуету {a=https://www.t.me/b3rg3n}BERGEN{/a}.
""")


## Короткое название игры, используемое для исполняемых файлов и директорий при
## постройке дистрибутивов. Оно должно содержать текст формата ASCII и не должно
## содержать пробелы, двоеточия и точки с запятой.

define build.name = "SkeetRemaster"


## Звуки и музыка ##############################################################

## Эти три переменные управляют, среди прочего, тем, какие микшеры показываются
## игроку по умолчанию. Установка одной из них в False скроет соответствующий
## микшер.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True


## Чтобы разрешить игроку тестировать громкость на звуковом или голосовом
## каналах, раскомментируйте строчку и настройте пример звука для прослушивания.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Раскомментируйте следующую строчку, чтобы настроить аудиофайл, который будет
## проигрываться в главном меню. Этот файл продолжит проигрываться во время
## игры, если не будет остановлен, или не начнёт проигрываться другой аудиофайл.

# define config.main_menu_music = "main-menu-theme.ogg"


## Переходы ####################################################################
##
## Эти переменные задают переходы, используемые в различных событиях. Каждая
## переменная должна задавать переход или None, чтобы указать на то, что переход
## не должен использоваться.

define config.enter_transition = cLinearBlur(0.5)
define config.exit_transition = cLinearBlur(0.5)
define config.intra_transition = ImageDissolve("source/wipeleft.png", 0.5, ramplen=64)
define config.after_load_transition = MultipleTransition([False, ImageDissolve("source/wipeleft.png", 0.5, ramplen=64), Solid("#000"), Pause(0.25), Solid("#000"), ImageDissolve("source/wipeleft.png", 0.5, ramplen=64), True])
define config.end_game_transition = Fade(1.5, 1, 2)
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Переменная, устанавливающая переход, когда старт игры не существует. Вместо
## неё используйте функцию with после показа начальной сценки.


## Управление окнами ###########################################################
##
## Эта строка контролирует, когда появляется диалоговое окно. Если "show" — оно
## всегда показано. Если "hide" — оно показывается, только когда представлен
## диалог. Если "auto" — окно скрыто до появления оператора scene и показывается
## при появлении диалога.
##
## После начала игры этот параметр можно изменить с помощью "window show",
## "window hide" и "window auto".

define config.window = "auto"


## Переходы, используемые при показе и скрытии диалогового окна

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Стандартные настройки #######################################################

## Контролирует стандартную скорость текста. По умолчанию, это 0 — мгновенно,
## в то время как любая другая цифра — это количество символов, печатаемых в
## секунду.

default preferences.text_cps = 50


## Стандартная задержка авточтения. Большие значения означают долгие ожидания, а
## от 0 до 30 — вполне допустимый диапазон.

default preferences.afm_time = 15


## Директория сохранений #######################################################
##
## Контролирует зависимое от платформы место, куда Ren'Py будет складывать файлы
## сохранения этой игры. Файлы сохранений будут храниться в:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>.
##
## Этот параметр обычно не должен изменяться, а если и изменился, должен быть
## текстовой строчкой, а не выражением.

define config.save_directory = None


## Иконка ######################################################################
##
## Иконка, показываемая на панели задач или на dock.

define config.window_icon = "gui/window_icon.png"


## Настройка Дистрибутива ######################################################
##
## Эта секция контролирует, как Ren'Py строит дистрибутивные файлы из вашего
## проекта.

init python:

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.md', None)
    build.classify('**.rpyb', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**.rar', None)
    build.classify('**.zip', None)
    build.classify('**.7z', None)
    build.classify('game/mod_assets/scripts/.vscode/**', None)
    build.classify('game/cache/**', None)
    build.classify('game/tl/**', None)
    build.classify('game/renpy-ActionEditor3-master/**', None)

    build.archive("sr_engine", "all")
    build.archive("sr_image", "all")
    build.archive("sr_audio", "all")
    build.archive("sr_video", "all")
    build.archive("sr_font", "all")

    build.classify("game/**.jpg", "sr_image")
    build.classify("game/**.jpeg", "sr_image")
    build.classify("game/**.webp", "sr_image")
    build.classify("game/**.png", "sr_image")

    build.classify("game/**.rpyc", "sr_engine")
    build.classify("game/**.rpy", "sr_engine")

    build.classify("game/**.pyc", "sr_engine")
    build.classify("game/**.py", "sr_engine")

    build.classify("game/**.wav", "sr_audio")
    build.classify("game/**.mp3", "sr_audio")
    build.classify("game/**.ogg", "sr_audio")

    build.classify("game/**.otf", "sr_font")
    build.classify("game/**.ttf", "sr_font")

    build.classify("game/**.webm", "sr_video")
    build.classify("game/**.ogv", "sr_video")
    build.classify("game/**.ogm", "sr_video")

    build.documentation('*.html')
    build.documentation('*.txt')