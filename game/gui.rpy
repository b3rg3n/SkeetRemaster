﻿################################################################################
## Инициализация
################################################################################

## Оператор init offset повышает приоритет инициализации в этом файле над
## другими файлами, из-за чего инициализация здесь запускается первее.
init offset = -2

## Вызываю gui.init, чтобы сбросить стили, чувствительные к стандартным
## значениям, и задать высоту и ширину окна игры.
init python:
    gui.init(1920, 1080)

    style.log_button = Style(style.button)
    style.log_button.child = None
    style.log_button.focus_mask = None
    style.log_button.background  = None

    style.base_font = Style(style.default)
    style.base_font.font  = "source/fonts/BeyneRegular.otf"
    style.base_font.size = 21
    style.base_font.line_spacing = 2

    style.menu_buttons_suka = Style(style.base_font)
    style.menu_buttons_suka.font  = "source/fonts/BeyneRegular.otf"
    style.menu_buttons_suka.size = 50
    style.menu_buttons_suka.kerning = 3
    style.menu_buttons_suka.color = "#ffffff"
    style.menu_buttons_suka.hover_color = "#ff0000"
    style.menu_buttons_suka.selected_color = "#ffffff"
    style.menu_buttons_suka.selected_idle_color = "#f77272"
    style.menu_buttons_suka.selected_hover_color = "#ff0000"
    style.menu_buttons_suka.insensitive_color = "#ffffff"



## Включить проверку на недопустимые или нестабильные свойства в экранах или
## преобразованиях
define config.check_conflicting_properties = True


################################################################################
## Система Динамического GUI
################################################################################

init python:
    class DynamicGUISystem:
        """Система для автоматического пересчета размеров GUI элементов"""
        
        def __init__(self):
            # Базовые значения для экрана 1920px
            self.base_screen_width = 1920
            self.base_screen_height = 1025
            
            # Сохраняем оригинальные пропорции
            self.proportions = {
                'dialogue_width': 1116 / 1920,      # 58%
                'dialogue_xpos': 402 / 1920,        # 21%
                'choice_button_width': 1185 / 1920, # 62%
                'slot_button_width': 414 / 1920,    # 21.5%
                'textbox_height': 278 / 1025,       # 27%
                'name_xpos': 360 / 1920,            # 18.7%
                'history_text_width': 1110 / 1920,  # 57.8%
                'nvl_text_width': 885 / 1920,       # 46%
            }
            
            # Инициализируем динамические значения
            self.update_gui_values()
        
        def get_real_window_size(self):
            """Получает реальный размер окна через SDL"""
            try:
                import ctypes
                
                # Получаем SDL dll и указатель на окно
                sdl = renpy.get_sdl_dll()
                win = renpy.get_sdl_window_pointer()
                
                if sdl is None or win is None:
                    return None, None
                
                # Получаем размер окна
                w = ctypes.c_int()
                h = ctypes.c_int()
                
                sdl.SDL_GetWindowSize(win, ctypes.byref(w), ctypes.byref(h))
                
                return w.value, h.value
            except Exception as e:
                print(f"Ошибка получения размера окна через SDL: {e}")
                return None, None
        
        def get_screen_width(self):
            """Получает текущую ширину окна"""
            # Пытаемся получить реальный размер окна
            real_width, _ = self.get_real_window_size()
            if real_width and real_width > 0:
                return real_width
            
            # Fallback к стандартным методам
            try:
                width = renpy.get_physical_size()[0]
                if width and width > 0:
                    return width
            except:
                pass
            
            return getattr(config, 'screen_width', self.base_screen_width)
        
        def get_screen_height(self):
            """Получает текущую высоту окна"""
            # Пытаемся получить реальный размер окна
            _, real_height = self.get_real_window_size()
            if real_height and real_height > 0:
                return real_height
            
            # Fallback к стандартным методам
            try:
                height = renpy.get_physical_size()[1]
                if height and height > 0:
                    return height
            except:
                pass
            
            return getattr(config, 'screen_height', self.base_screen_height)
        
        def calculate_dynamic_value(self, proportion_key, use_height=False):
            """Вычисляет динамическое значение на основе пропорции"""
            if use_height:
                current_screen = self.get_screen_height()
            else:
                current_screen = self.get_screen_width()
            
            proportion = self.proportions.get(proportion_key, 0)
            return int(current_screen * proportion)
        
        def update_gui_values(self):
            """Обновляет все GUI значения на основе текущего размера экрана"""
            # Обновляем ширины
            gui.dialogue_width = self.calculate_dynamic_value('dialogue_width')
            gui.choice_button_width = self.calculate_dynamic_value('choice_button_width')
            gui.slot_button_width = self.calculate_dynamic_value('slot_button_width')
            gui.history_text_width = self.calculate_dynamic_value('history_text_width')
            gui.nvl_text_width = self.calculate_dynamic_value('nvl_text_width')
            
            # Обновляем позиции
            gui.dialogue_xpos = self.calculate_dynamic_value('dialogue_xpos')
            gui.name_xpos = self.calculate_dynamic_value('name_xpos')
            
            # Обновляем высоты
            gui.textbox_height = self.calculate_dynamic_value('textbox_height', use_height=True)
    
    # Создаем экземпляр системы
    dynamic_gui_system = DynamicGUISystem()
    
    # Переменная для отслеживания последнего размера
    last_known_size = [0, 0]
    
    # Функция для принудительного обновления GUI (можно вызывать из игры)
    def refresh_dynamic_gui():
        """Принудительно обновляет все динамические значения GUI"""
        dynamic_gui_system.update_gui_values()
        renpy.restart_interaction()
    
    # Функция для проверки изменений размера окна
    def check_and_update_gui():
        """Проверяет изменение размера окна и обновляет GUI при необходимости"""
        try:
            current_width = dynamic_gui_system.get_screen_width()
            current_height = dynamic_gui_system.get_screen_height()
            
            if (last_known_size[0] != current_width or 
                last_known_size[1] != current_height):
                
                last_known_size[0] = current_width
                last_known_size[1] = current_height
                
                # Обновляем GUI с новыми размерами
                dynamic_gui_system.update_gui_values()
                
                # Принудительно перерисовываем экраны
                renpy.restart_interaction()
                
                # Подробная отладочная информация
                real_w, real_h = dynamic_gui_system.get_real_window_size()
                physical_size = renpy.get_physical_size()
                
                print("=" * 50)
                print(f"ОБНОВЛЕНИЕ GUI:")
                print(f"Реальный размер окна (SDL): {real_w}x{real_h}")
                print(f"Physical size (RenPy): {physical_size}")
                print(f"Используемый размер: {current_width}x{current_height}")
                print(f"Ширина диалога: {gui.dialogue_width}")
                print(f"Ширина кнопок выбора: {gui.choice_button_width}")
                print("=" * 50)
                
        except Exception as e:
            print(f"Ошибка при проверке размера окна: {e}")
    
    # Подписываемся на изменения размера экрана
    def on_screen_resize():
        """Автоматически обновляет GUI при изменении размера экрана"""
        check_and_update_gui()
    
    # Включаем изменяемый размер окна через preferences
    # config.window_resizable не существует в Ren'Py, используем другой подход
    
    # Настраиваем автоматическое обновление при изменении размера
    def auto_update_gui():
        """Автоматически обновляет GUI при изменении размера окна"""
        old_width = getattr(auto_update_gui, 'last_width', config.screen_width)
        current_width = config.screen_width
        
        if old_width != current_width:
            dynamic_gui_system.update_gui_values()
            auto_update_gui.last_width = current_width
    
    # Добавляем callback для проверки изменений размера (отключено, так как может быть слишком частым)
    # config.periodic_callback = auto_update_gui
    
    # Функция для тестирования системы
    def test_dynamic_gui():
        """Тестирует систему динамического GUI с разными размерами"""
        real_w, real_h = dynamic_gui_system.get_real_window_size()
        physical_size = renpy.get_physical_size()
        
        print("=== ТЕСТИРОВАНИЕ ДИНАМИЧЕСКОГО GUI ===")
        print(f"Реальный размер окна (SDL): {real_w}x{real_h}")
        print(f"Physical size (RenPy): {physical_size}")
        print(f"Config размеры: {config.screen_width}x{config.screen_height}")
        print(f"Используемые размеры: {dynamic_gui_system.get_screen_width()}x{dynamic_gui_system.get_screen_height()}")
        print(f"Ширина диалога: {gui.dialogue_width}")
        print(f"Ширина кнопок выбора: {gui.choice_button_width}")
        print(f"Позиция диалога: {gui.dialogue_xpos}")
        print("=========================================")

    # Callback через adjust_view_size - это основной способ отслеживания изменений
    last_viewport_size = [0, 0]
    
    def adjust_view_size_callback(width, height):
        """Вызывается при изменении viewport - это наш главный способ отслеживания"""
        global last_viewport_size
        
        try:
            # Проверяем, действительно ли размер изменился
            if (last_viewport_size[0] != width or last_viewport_size[1] != height):
                last_viewport_size[0] = width
                last_viewport_size[1] = height
                
                print(f"=== ИЗМЕНЕНИЕ РАЗМЕРА VIEWPORT ===")
                print(f"Новый viewport: {width}x{height}")
                
                # Обновляем GUI с новыми размерами
                dynamic_gui_system.update_gui_values()
                
                # Показываем информацию о изменениях
                real_w, real_h = dynamic_gui_system.get_real_window_size()
                print(f"Реальный размер окна: {real_w}x{real_h}")
                print(f"Новая ширина диалога: {gui.dialogue_width}")
                print(f"Новая ширина кнопок: {gui.choice_button_width}")
                print("=" * 40)
                
        except Exception as e:
            print(f"Ошибка в adjust_view_size_callback: {e}")
        
        # Обязательно возвращаем размер
        return (width, height)
    
    # Устанавливаем callback
    config.adjust_view_size = adjust_view_size_callback
    
    # Дополнительно используем interact_callbacks для обновления при взаимодействии
    def interact_callback():
        """Проверяет изменения при каждом взаимодействии"""
        try:
            current_w = dynamic_gui_system.get_screen_width()
            current_h = dynamic_gui_system.get_screen_height()
            
            if (last_known_size[0] != current_w or last_known_size[1] != current_h):
                last_known_size[0] = current_w
                last_known_size[1] = current_h
                dynamic_gui_system.update_gui_values()
                print(f"GUI обновлен через interact_callback: {current_w}x{current_h}")
                
        except Exception as e:
            print(f"Ошибка в interact_callback: {e}")
    
    # Добавляем в список callback'ов взаимодействия
    config.interact_callbacks.append(interact_callback)


################################################################################
## Конфигурируемые Переменные GUI
################################################################################


## Цвета #######################################################################
##
## Цвета текста в интерфейсе.

## Акцентный цвет используется в заголовках и подчёркнутых текстах.
define gui.accent_color = '#ffffff'

## Цвет, используемый в текстовой кнопке, когда она не выбрана и не наведена.
define gui.idle_color = '#888888'

## Small_color используется в маленьком тексте, который должен быть ярче/темнее,
## для того, чтобы выделяться.
define gui.idle_small_color = '#aaaaaa'

## Цвет, используемых в кнопках и панелях, когда они наведены.
define gui.hover_color = '#ff0000'

## Цвет, используемый текстовой кнопкой, когда она выбрана, но не наведена.
## Кнопка может быть выбрана, если это текущий экран или текущее значение
## настройки.
define gui.selected_color = '#ffffff'

## Цвет, используемый текстовой кнопкой, когда она не может быть выбрана.
define gui.insensitive_color = '#8888887f'

## Цвета, используемые для частей панелей, которые не заполняются. Они
## используются не напрямую, а только при воссоздании файлов изображений.
define gui.muted_color = '#510000'
define gui.hover_muted_color = '#7a0000'

## Цвета, используемые в тексте диалогов и выборов.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'


## Шрифты и их размеры #########################################################

## Шрифт, используемый внутриигровым текстом.
define gui.text_font = "source/fonts/nvl_font.ttf"#DejaVuSans.ttf"

## Шрифт, используемый именами персонажей.
define gui.name_text_font = "source/fonts/nvl_font.ttf"

## Шрифт, используемый текстом вне игры.
define gui.interface_text_font = "source/fonts/BeyneRegular.otf"

## Размер нормального текста диалога.
define gui.text_size = 45

## Размер имён персонажей.
define gui.name_text_size = 45

## Размер текста в пользовательском интерфейсе.
define gui.interface_text_size = 33

## Размер заголовков в пользовательском интерфейсе.
define gui.label_text_size = 36

## Размер текста на экране уведомлений.
define gui.notify_text_size = 24

## Размер заголовка игры.
define gui.title_text_size = 75


## Главное и игровое меню. #####################################################

## Изображения, используемые в главном и игровом меню.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Диалог ######################################################################
##
## Эти переменные контролируют, как диалог появляется на отдельной строчке.

## Высота текстового окна, содержащего диалог.
define gui.textbox_height = 278

## Местоположение текстового окна по вертикали экрана. 0.0 — верх, 0.5 — центр и
## 1.0 — низ.
define gui.textbox_yalign = 1.0


## Местоположение имени говорящего персонажа по отношению к текстовому окну.
## Это могут быть целые значения в пикселях слева и сверху от начала окна или
## процентное отношение, например, 0.5 для центрирования.
define gui.name_xpos = 360
define gui.name_ypos = 0

## Горизонтальное выравнивание имени персонажа. Это может быть 0.0 для
## левоориентированного, 0.5 для центрированного и 1.0 для правоориентированного
## выравнивания.
define gui.name_xalign = 0.5

## Ширина, высота и границы окна, содержащего имя персонажа или None, для
## автоматической размерки.
define gui.namebox_width = None
define gui.namebox_height = None

## Границы окна, содержащего имя персонажа слева, сверху, справа и снизу по
## порядку.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Если True, фон текстового окна будет моститься (расширяться по эффекту
## плитки). Если False, фон текстового окна будет фиксированным.
define gui.namebox_tile = False


## Размещение диалога по отношению к текстовому окну. Это могут быть целые
## значения в пикселях слева и сверху от текстового окна или процентное
## отношение, например, 0.5 для центрирования.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## Максимальная ширина текста диалога в пикселях.
define gui.dialogue_width = 1116

## Горизонтальное выравнивание текста диалога. Это может быть 0.0 для
## левоориентированного, 0.5 для центрированного и 1.0 для правоориентированного
## выравнивания.
define gui.dialogue_text_xalign = 0.0


## Кнопки ######################################################################
##
## Эти переменные, вместе с файлами изображений в gui/button, контролируют
## аспекты того, как отображаются кнопки.

## Ширина и высота кнопки в пикселях. Если None, Ren'Py самостоятельно
## рассчитает размер.
define gui.button_width = None
define gui.button_height = None

## Границы каждой стороны кнопки в порядке слева, сверху, справа, снизу.
define gui.button_borders = Borders(6, 6, 6, 6)

## Если True, фон изображения будет моститься. Если False, фон изображения будет
## линейно масштабирован.
define gui.button_tile = False

## Шрифт, используемый кнопкой.
define gui.button_text_font = gui.interface_text_font

## Размер текста, используемый кнопкой.
define gui.button_text_size = gui.interface_text_size

## Цвет текста в кнопке в различных состояниях.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## Горизонтальное выравнивание текста в кнопке. (0.0 — лево, 0.5 — по центру,
## 1.0 — право).
define gui.button_text_xalign = 0.0


## Эти переменные переписывают настройки различных видов кнопок. Пожалуйста,
## посмотрите документацию по gui для просмотра всех вариаций кнопок и для чего
## каждая из них нужна.
##
## Эти настройки используются стандартным интерфейсом:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Вы также можете добавить собственные настройки, добавляя правильно
## именованные переменные. Например, вы можете раскомментировать следующую
## строчку, чтобы установить ширину кнопок навигации.

# define gui.navigation_button_width = 250


## Кнопки Выбора ###############################################################
##
## Кнопки выбора используются во внутриигровых меню.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Кнопки Слотов ###############################################################
##
## Кнопка слотов — особый вид кнопки. Она содержит миниатюру и текст,
## описывающий слот сохранения. Слот сохранения использует файлы из gui/button,
## как и другие виды кнопок.

## Кнопка слота сохранения.
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Ширина и высота миниатюры, используемой слотом сохранения.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Количество колонок и рядов в таблице слотов.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Позиционирование и Интервалы ################################################
##
## Эти переменные контролируют позиционирование и интервалы различных элементов
## пользовательского интерфейса.

## Местоположение левого края навигационных кнопок по отношению к левому краю
## экрана.
define gui.navigation_xpos = 60

## Вертикальная позиция индикатора пропуска.
define gui.skip_ypos = 15

## Вертикальная позиция экрана уведомлений.
define gui.notify_ypos = 68

## Интервал между выборами в меню.
define gui.choice_spacing = 33

## Кнопки в секции навигации главного и игрового меню.
define gui.navigation_spacing = 6

## Контролирует интервал между настройками.
define gui.pref_spacing = 15

## Контролирует интервал между кнопками настройки.
define gui.pref_button_spacing = 0

## Интервал между кнопками страниц.
define gui.page_spacing = 0

## Интервал между слотами.
define gui.slot_spacing = 15

## Позиция текста главного меню.
define gui.main_menu_text_xalign = 1.0


## Рамки #######################################################################
##
## Эти переменные контролируют вид рамок, содержащих компоненты
## пользовательского интерфейса, когда наложения или окна не представлены.

## Генерируем рамки.
define gui.frame_borders = Borders(6, 6, 6, 6)

## Рамки, используемые в частях экрана подтверждения.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Рамки, используемые в частях экрана пропуска.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Рамки, используемые в частях экрана уведомлений.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## Должны ли фоны рамок моститься?
define gui.frame_tile = False


## Панели, Полосы прокрутки и Ползунки #########################################
##
## Эти настройки контролируют вид и размер панелей, полос прокрутки и ползунков.
##
## Стандартный GUI использует только ползунки и вертикальные полосы прокрутки.
## Все остальные полосы используются только в новосозданных экранах.

## Высота горизонтальных панелей, полос прокрутки и ползунков. Ширина
## вертикальных панелей, полос прокрутки и ползунков.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## True, если изображения панелей должны моститься. False, если они должны быть
## линейно масштабированы.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Горизонтальные границы.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Вертикальные границы.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## Что делать с непрокручиваемыми полосами прокрутки в интерфейсе. "hide" прячет
## их, а None их показывает.
define gui.unscrollable = "hide"


## История #####################################################################
##
## Экран истории показывает диалог, который игрок уже прошёл.

## Количество диалоговых блоков истории, которые Ren'Py будет хранить.
define config.history_length = 1000

## Высота доступных записей на экране истории, или None, чтобы задать высоту в
## зависимости от производительности.
define gui.history_height = None

## Дополнительное пространство добавляемое между записями экрана истории.
define gui.history_spacing = 0

## Местоположение, ширина и выравнивание заголовка, показывающего имя говорящего
## персонажа.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## Местоположение, ширина и выравнивание диалогового текста.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## Режим NVL ###################################################################
##
## Экран режима NVL показывает диалог NVL персонажей.

## Границы фона окна NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## Максимальное число показываемых строк в режиме NVL. Когда количество строчек
## начинает превышать это значение, старые строчки очищаются.
define gui.nvl_list_length = 3

## Высота доступных строчек в режиме NVL. Установите на None, чтобы строчки
## динамически регулировали свою высоту.
define gui.nvl_height = None

## Интервал между строчками в режиме NVL, если gui.nvl_height имеет значение
## None, а также между строчками и меню режима NVL.
define gui.nvl_spacing = 100

## Местоположение, ширина и выравнивание заголовка, показывающего имя говорящего
## персонажа.
define gui.nvl_name_xpos = 250
define gui.nvl_name_ypos = 5
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## Местоположение, ширина и выравнивание диалогового текста.
define gui.nvl_text_xpos = 260
define gui.nvl_text_ypos = 11
define gui.nvl_text_width = 1600
define gui.nvl_text_xalign = 0.0

## Местоположение, ширина и выравнивание текста nvl_thought (текст от лица
## персонажа nvl_narrator).
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## Местоположение кнопок меню NVL.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Локализация #################################################################

## Эта настройка контролирует доступ к разрыву линий. Стандартная настройка
## подходит для большинства языков. Список доступных значений можно найти на
## https://www.renpy.org/doc/html/style_properties.html#style-property-language

define gui.language = "unicode"
