python early:
    config.allow_duplicate_labels = True

    def check_muzlo_ts(value):
        for k, v in music_list_7dl.items():
            if v == value:
                return k

    def get_playing_ts(channel='music'):
        m = renpy.music.get_playing(channel=channel)
        if m is not None:
            m = parse_music(m)
        return m

    import re

    def parse_music(mus_string):
        return re.sub('<.*?>', '', str(mus_string))

    def widget_music_ts():
        if (not persistent.music_widget_ts):
            globals()['track_checker_blya'] = "empty"
            return
        else:
            
            m = get_playing_ts('music')
            
            
            if m in music_list_7dl.values():
                globals()['track_checker_blya'] = check_muzlo_ts(m)[:50]
            elif m == None:
                globals()['track_checker_blya'] = " "
            else:
                globals()['track_checker_blya'] = "Не прописано название трека"
    config.overlay_functions.append(widget_music_ts)

init -4 python:

    layout.ARE_YOU_SURE = _("Уверен?")
    layout.DELETE_SAVE = _("Точно хочешь забыть?")
    layout.OVERWRITE_SAVE = _("Точно хочешь перезапомнить?")
    layout.LOADING = _("Если вспомнишь - забудешь, что видел после.\nУверен?")
    layout.QUIT = _("Так скоро тикаешь?")
    layout.MAIN_MENU = _("Вернуться на главную?\nЭабудешь всё, что видел.")
    layout.END_REPLAY = _("Остановить повтор?")
    layout.SLOW_SKIP = _("Промотать всё нахуй?")
    layout.FAST_SKIP_UNSEEN = _("Промотать всё до следующего выбора?")
    layout.FAST_SKIP_SEEN = _("Съебать на следующий выбор?")

init -1199 python:
    from os import path

    sr_path = 'source/'
    sr_mus = sr_path + 'muzzon/'
    sr_vid = sr_path + 'videosos/'

    for file in renpy.list_files(): # ФУНКЦИЯ ГОПА АУДИО БЕЗ ДЕФАЙНА
        if sr_path in file:
            file_name = path.splitext(path.basename(file))[0]
            if file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")):
                globals()[file_name] = file

    for i in renpy.list_files(): # ФУНКЦИЯ ГОПА ПНГ И ЖПГ БЕЗ ДЕФАЙНА
        if not i.startswith("source/"):
            continue
        elif i.startswith(sr_path):
            renpy.image("%s" % i[len(sr_path):-4], i)


init -1001 python:

    renpy.music.register_channel("sound", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound4", "sfx", False)
    renpy.music.register_channel("sound_loop", "voice", True)
    renpy.music.register_channel("sound_loop2", "voice", True)
    renpy.music.register_channel("sound_loop3", "voice", True)
    renpy.music.register_channel("ambience", "voice", True)

    def stop_music():
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music"):
            renpy.music.stop(channel=chnl)

    def stop_sound():
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience"):
            renpy.sound.stop(channel=chnl)

init python:
    import random

    nonunicode = "¡¢£¤¥¦§¨©ª«¬®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖ×ØÙÚÛÜÝÞßàáâãäåæçèéêëìíîïðñòóôõö÷øùúûüýþÿĀāĂăĄąĆćĈĉĊċČčĎďĐđĒēĔĕĖėĘęĚěĜĝĞğĠġĢģĤĥĦħĨĩĪīĬĭĮįİıĲĳĴĵĶķĸĹĺĻļĽľĿŀŁłŃńŅņŇňŉŊŋŌōŎŏŐőŒœŔŕŖŗŘřŚśŜŝŞşŠšŢţŤťŦŧŨũŪūŬŭŮůŰűŲųŴŵŶŷŸŹźŻżŽž"

    def glitchtext(length):
        output = ""
        for x in range(length):
            output += random.choice(nonunicode)
        return output

    em_name = glitchtext(5)

init python:
    import math

    lep1 = SnowBlossom(sr_path + 'lep_1.png', start=3.0, count=20, border=50, xspeed=(50, 85), yspeed=(160, 215), fast=True)
    lep2 = SnowBlossom(sr_path + 'lep_2.png', count=20, yspeed=(120, 165), start=3.0, border=50, xspeed=(75, 125), fast=True)
    lep3 = SnowBlossom(sr_path + 'lep_3.png', start=3.0, count=20, border=50, xspeed=(50, 85), yspeed=(160, 215), fast=True)
    lep4 = SnowBlossom(sr_path + 'lep_4.png', count=20, yspeed=(120, 165), start=3.0, border=50, xspeed=(75, 125), fast=True)
    lep5 = SnowBlossom(sr_path + 'lep_5.png', count=20, yspeed=(120, 165), start=3.0, border=50, xspeed=(75, 125), fast=True)
    renpy.image('lepestki_krutyatsa', LiveComposite((1920, 1080), (0, 0), lep1, (0, 0), lep2, (0, 0), lep3, (0, 0), lep4, (0, 0), lep5))

    snowfg = SnowBlossom(sr_path + 'et_snow.png', start=3.0, count=180, border=50, xspeed=(50, 85), yspeed=(160, 215), fast=True)
    snowbg = SnowBlossom(im.Scale(sr_path + 'et_snow.png', 5, 5), count=180, yspeed=(120, 165), start=3.0, border=50, xspeed=(75, 125), fast=True)
    renpy.image('snezhok', LiveComposite((1920, 1080), (0, 0), snowbg, (0, 0), snowfg))


    def ts_black_sparkles(sh=1):
        if sh == 1:
            renpy.show('ts_eff_sparkles_black', layer='front')
        elif sh == 0:
            renpy.hide('ts_eff_sparkles_black', layer='front')
        renpy.transition(dissolve)

    def ts_orange_sparkles(sh=1):
        if sh == 1:
            renpy.show('ts_eff_sparkles_black1', layer='front')
        elif sh == 0:
            renpy.hide('ts_eff_sparkles_black1', layer='front')
        renpy.transition(dissolve)

    class GrayGlowDot(object):
        
        def __init__(self):
            
            self.sm = SpriteManager(update=self.update)
            
            self.glows = [ ]
            self.rd = "source/piluka.png"
            
            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))
            
            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))
        
        def add(self, d, speed):
            s = self.sm.create(d)
            
            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)
            
            self.glows.append((s, start, speed))
        
        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)
            
            return 0
    renpy.image("piluka", GrayGlowDot().sm)

    class RedGlowDot(object):
        
        def __init__(self):
            
            self.sm = SpriteManager(update=self.update)
            
            self.glows = [ ]
            self.rd = "source/chast1.png"
            
            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))
            
            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))
        
        def add(self, d, speed):
            s = self.sm.create(d)
            
            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)
            
            self.glows.append((s, start, speed))
        
        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)
            
            return 0
    renpy.image("redpart", RedGlowDot().sm)

    class YellowGlowDot(object):
        
        def __init__(self):
            
            self.sm = SpriteManager(update=self.update)
            
            self.glows = [ ]
            self.rd = "source/piluka1.png"
            
            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))
            
            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))
        
        def add(self, d, speed):
            s = self.sm.create(d)
            
            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)
            
            self.glows.append((s, start, speed))
        
        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)
            
            return 0
    renpy.image("piluka_fb", YellowGlowDot().sm)

init python:

    def reg_char(id, name, who_color, what_color = "#fff", pref = "", suf = ""):
        global Character
        gl = globals()
        
        gl[id] = Character( name, color=who_color, what_color=what_color, drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000", what_prefix=pref, what_suffix=suf )

    reg_char("th", '', "#18FFEB", pref="«", suf="»")
    reg_char("th1", ' ', "#dd9933", "#42AAFF", pref="«", suf="»")
    reg_char("th2", ' ', "#dd9933", "#FF5252", pref="«", suf="»")
    reg_char("th3", ' ', "#dd9933", "#FF8000", pref="«", suf="»")
    reg_char("th4", ' ', "#dd9933", "#008080", pref="«", suf="»")
    reg_char("skt", 'Дима Скит', "#008080")
    reg_char("oldskt", 'Папа Скит', "#008080")
    reg_char("dobby", 'Доберман', "#77dd77")
    reg_char("cld", 'ColdFSociety', "#00008b")
    reg_char("lxrd", 'deadlylxrd', "#ffffff")
    reg_char("lxrd1", 'Клон Вади', "#ffff00")
    reg_char("mrz", 'В. Морозко', "#ffffff")
    reg_char("lxrd2", 'К. Морозко', "#ffff00")
    reg_char("brg", 'Вечный', "#ff0000")
    reg_char("nn", 'iNeoony', "#ff9baa")
    reg_char("barmn", 'Бармен', "#ff0000")
    reg_char("vsn", 'Вишневский', "#c8ffc8")
    reg_char("joz", 'JoZeF', "#00f800")
    reg_char("dmn", 'Диман', "#d2691e")
    reg_char("shg", 'Шепiд', "#ff4500")
    reg_char("semp", 'Семпай', "#77dd77")
    reg_char("strlk", 'Стрелок', "#77dd77")
    reg_char("razrab", 'Разраб', "#800000")
    reg_char("lis", '???', "#c8ffc8")
    reg_char("avlm", 'Авелайм', "#808000")
    reg_char("melles", 'Melles1991', "#ffff00")
    reg_char("vchn", 'Вечный', "#ff0000")
    reg_char("rmzn", 'Рамазанчик', "#ffff00")
    reg_char("galenin", 'Илюша', "#ffd700")
    reg_char("bergen1", 'Семпай', "#ffff00")
    reg_char("shv", 'Швiлли', "#c8ffc8")
    reg_char("vas", 'Василиса', "#FF8000")
    reg_char("vastg", 'Василиса (в тг)', "#FF8000")
    reg_char("par1", 'Парниша', "#bb8282")
    reg_char("par2", 'Парниша', "#c2b466")
    reg_char("par3", 'Парниша', "#a48f5d")
    reg_char("rcn", 'Ракун', "#ffff00")
    reg_char("oguzok", 'Огузок', "#c2b466")
    reg_char("ovr", 'Оверлорд', "#c2b466")
    reg_char("eva", 'Ева', "#FFC0CB")
    reg_char("foma", 'Фома', "#c2b466")
    reg_char("mt", 'Мент', "#bb8282")
    reg_char("mt1", 'Мент', "#c2b466")
    reg_char("ivt1", 'Иветта', "#ff0000", "#ff0000")
    reg_char("golosone", 'Голоса', "#008000", "#008000")
    reg_char("golostwo", 'Голоса', "#77dd77", "#77dd77")
    reg_char("golosthree", 'Голоса', "#00fa9a", "#00fa9a")
    reg_char("rmcj", 'Женёк', "#ffff00")
    reg_char("luka", 'Лукавый', "#ff0000")
    reg_char("golos", 'Голос', "#00008b")
    reg_char("rgn", 'Рагнарёк', "#ffff00")
    reg_char("chc", 'Чиконя', "#ff4500")
    reg_char("pchr", 'Император', "#b3ff00")
    reg_char("sezam", 'Сезамчик', "#00ff80")
    reg_char("nmor", 'Настя', "#ff0040")
    reg_char("perdila", 'Пердила1977', "#ff7300")
    reg_char("andt", 'Ондатра', "#FFC0CB")
    reg_char("sxns", 'Санёчек', "#ffd700")
    reg_char("shb", 'ShelbyHell', "#00008b")

init:

    default persistent.music_widget_ts = True
    default track_checker_blya = "empty"

    define nvlivt = Character (u'Иветта:', kind=nvl, color = "#ff0000", what_color="FFFFFF",)
    define nvlvas = Character (u'Василиса:', kind=nvl, color = "#FF8000", what_color="FFFFFF",)
    define nvllxrd = Character (u'Вадим:', kind=nvl, color = "#ffffff", what_color="FFFFFF",)
    define nvlbazar = Character (u' ', kind=nvl, color = "#dd9933", what_color="FFFFFF",)
    define nvlskt = Character (u'Скит:', kind=nvl, color = "#008080", what_color="FFFFFF",)
    define nvltn = Character (u'Тунец:', kind=nvl, color = "#c8ffc8", what_color="FFFFFF",)
    define nvlstr = Character (u'Стрелок:', kind=nvl, color = "#ff0000", what_color="FFFFFF",)
    define nvlshv = Character (u'Саня:', kind=nvl, color = "#c8ffc8", what_color="FFFFFF",)
    define nvlvhcn = Character (u'Вечный:', kind=nvl, color = "#ff0000", what_color="FFFFFF",)
    define nvlcld = Character (u'Колд:', kind=nvl, color = "#00008b", what_color="FFFFFF",)
    define nvllis = Character (u'???:', kind=nvl, color = "#c8ffc8", what_color="FFFFFF",)
    define nvlsemp = Character (u'Семпай:', kind=nvl, color = "#77dd77", what_color="FFFFFF",)
    define nvlluka = Character (u'Лукавый:', kind=nvl, color = "#ff0000", what_color="FFFFFF",)
    define nvlvsn = Character (u'Юра:', kind=nvl, color = "#c8ffc8", what_color="FFFFFF",)
    define nvlvchn = Character (u'Вечный:', kind=nvl, color = "#ff0000", what_color="FFFFFF",)
    define nvlpchr = Character (u'Император:', kind=nvl, color = "#c8ffc8", what_color="FFFFFF",)

    image menushka = Movie(fps=60, size = (1920, 1080), play=sr_vid + "menu/mn1.webm")
    image menushkasr2 = Movie(fps=60, size = (1920, 1080), play=sr_vid + "menu/mn2.webm")
    image menushkasr3 = Movie(fps=60, size = (1920, 1080), play=sr_vid + "menu/mn3.webm")
    image menushkasr4 = Movie(fps=60, size = (1920, 1080), play=sr_vid + "menu/mn4.webm")
    image menushkasr5 = Movie(fps=60, size = (1920, 1080), play=sr_vid + "menu/mn5.webm")
    image menushkasr6 = Movie(fps=60, size = (1920, 1080), play=sr_vid + "menu/mn6.webm")
    image menushkasr7 = Movie(fps=60, size = (1920, 1080), play=sr_vid + "menu/mn7.webm")
    image menushkasr8 = Movie(fps=60, size = (1920, 1080), play=sr_vid + "menu/mn8.webm")
    image burnint = Movie(fps=60, size = (1920, 1080), play=sr_vid + "burnint.webm")
    image roofburn = Movie(fps=60, size = (1920, 1080), play=sr_vid + "roofburn.webm")
    image squareanim = Movie(fps=60, size = (1920, 1080), play=sr_vid + "es.webm")
    image bunkerson = Movie(fps=60, size = (1920, 1080), play=sr_vid + "bunker.webm")
    image menushka1 = Movie(fps=60, size = (1920, 1080), play=sr_vid + "menushka1.webm")
    image vadimka_torch = Movie(fps=60, size = (1920, 1080), play=sr_vid + "vadimka_torch.webm")
    image ld_vid = Movie(fps=60, size = (1920, 1080), play=sr_vid + "LEGENDARY_DREEFT.ogv")
    image neon = Movie(fps=60, size = (1920, 1080), play=sr_vid + "neon.webm")

###ПЫЛЬ ИЗ ДОКИ
    image dust1:
        "source/dust1.png"
        subpixel True
        parallel:
            alpha 1.00
            6.0
            linear 1.0 alpha 0.35
            1.0
            linear 1.0 alpha 1.0
            repeat
        parallel:
            alpha 0
            linear 2.0 alpha 1.0
            10.0
            linear 2.0 alpha 0
            repeat
        parallel:
            xoffset 100 yoffset -100
            linear 14.0 xoffset -100 yoffset 100
            repeat

    image dust2:
        "source/dust2.png"
        subpixel True
        parallel:
            alpha 1.00
            6.0
            linear 1.0 alpha 0.35
            1.0
            linear 1.0 alpha 1.0
            repeat
        parallel:
            alpha 0
            linear 2.0 alpha 1.0
            28.0
            linear 2.0 alpha 0
            repeat
        parallel:
            xoffset 100 yoffset -100
            linear 32.0 xoffset -100 yoffset 100
            repeat

    image dust3:
        "source/dust3.png"
        subpixel True
        parallel:
            alpha 1.00
            6.0
            linear 1.0 alpha 0.35
            1.0
            linear 1.0 alpha 1.0
            repeat
        parallel:
            alpha 0
            linear 2.0 alpha 1.0
            13.0
            linear 2.0 alpha 0
            repeat
        parallel:
            xoffset 100 yoffset -100
            linear 17.0 xoffset -100 yoffset 100
            repeat

    image dust4:
        "source/dust4.png"
        subpixel True
        parallel:
            alpha 1.00
            6.0
            linear 1.0 alpha 0.35
            1.0
            linear 1.0 alpha 1.0
            repeat
        parallel:
            alpha 0
            linear 2.0 alpha 1.0
            15.0
            linear 2.0 alpha 0
            repeat
        parallel:
            xoffset 100 yoffset -100
            linear 19.0 xoffset -100 yoffset 100
            repeat

    image ts_sparkle_black:
        "source/sparkle_black.png"
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        alpha 0.9 zoom 0.75
        pause 3
        ease 3 alpha 0
    image ts_eff_sparkles_black:
        SnowBlossom(ImageReference("ts_sparkle_black"), 50, 50, (15, 30), (25, 125))
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        rotate 180
    image ts_sparkle_black1:
        "source/sparkle_black1.png"
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        alpha 0.9 zoom 0.75
        pause 3
        ease 3 alpha 0
    image ts_eff_sparkles_black1:
        SnowBlossom(ImageReference("ts_sparkle_black1"), 50, 50, (15, 30), (25, 125))
        anchor (0.5, 0.5)
        align (0.5, 0.5)
        rotate 180

    $ style.credits = Style(style.default)
    $ style.credits.font  = "source/fonts/3.otf"
    $ style.credits.color = "#fff"
    $ style.credits.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.credits.drop_shadow_color = "#000"
    $ style.credits.italic = False
    $ style.credits.bold = False
    $ style.credits.text_align = 0.5
    $ style.credits.xmaximum = 0.8

    image credits = ParameterizedText(style = "credits", size = 50)

    define sr_credits = "\n\n\n\n\n\nСпасибо за прохождение.\n\nЭта новелла делалась практически три года.\nЭто был сложный период в моей жизни.\nРазработка много раз замораживалась...\nМного раз отменялась...\nНо всё же...\nЯ был бы не я, если бы не доделал этот <<шедевр>>.\n\n\nОсобый респект выражаю этим браткам:\nЖенёк <<rmcj>>\nПавел <<Pechorsky>>\nВадим <<deadlylxrd>>\nНикита <<ColdFSociety>>\n\n\nБез них эта игра бы просто не вышла.\n\n\n\nВозможно, мы скоро увидимся.\nБудь на связи.\n\n\n\n\n\n\nКОНЕЦ.\n\n\n\n(c) BERGEN 2022-2024"

    default persistent.bazarbig = True
    default persistent.zastavka_skip = False
    default persistent.set_volumes = False

    default persistent.muz_rnd_sr = True
    default persistent.muz_1_sr = False
    default persistent.muz_2_sr = False
    default persistent.muz_3_sr = False
    default persistent.muz_4_sr = False
    default persistent.muz_5_sr = False
    default persistent.muz_6_sr = False
    default persistent.muz_7_sr = False
    default persistent.muz_8_sr = True

    default persistent.achivka1 = False
    default persistent.achivka2 = False
    default persistent.achivka3 = False
    default persistent.achivka4 = False
    default persistent.achivka5 = False
    default persistent.achivka6 = False