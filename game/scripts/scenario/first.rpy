label main_menu:
    if persistent.muz_rnd_sr is True:
        if persistent.muz_1_sr is True:
            $ persistent.muz_1_sr = False
            $ persistent.muz_2_sr = True
            jump main_menu_after_rnd
        if persistent.muz_2_sr is True:
            $ persistent.muz_2_sr = False
            $ persistent.muz_3_sr = True
            jump main_menu_after_rnd
        if persistent.muz_3_sr is True:
            $ persistent.muz_3_sr = False
            $ persistent.muz_4_sr = True
            jump main_menu_after_rnd
        if persistent.muz_4_sr is True:
            $ persistent.muz_4_sr = False
            $ persistent.muz_5_sr = True
            jump main_menu_after_rnd
        if persistent.muz_5_sr is True:
            $ persistent.muz_5_sr = False
            $ persistent.muz_6_sr = True
            jump main_menu_after_rnd
        if persistent.muz_6_sr is True:
            $ persistent.muz_6_sr = False
            $ persistent.muz_7_sr = True
            jump main_menu_after_rnd
        if persistent.muz_7_sr is True:
            $ persistent.muz_7_sr = False
            $ persistent.muz_8_sr = True
            jump main_menu_after_rnd
        if persistent.muz_8_sr is True:
            $ persistent.muz_8_sr = False
            $ persistent.muz_1_sr = True
            jump main_menu_after_rnd
    elif True:
        jump main_menu_after_rnd

label main_menu_after_rnd:

    stop sound fadeout 3
    stop music fadeout 3
    window hide

    if persistent.achivka4 and persistent.achivka3 and persistent.achivka5 and persistent.achivka2 and persistent.achivka1 and not persistent.achivka6:
        $ persistent.achivka6 = True
        $ persistent.shetchik_koncovok += 1
        play sound ach_sound
        show achiv6 at ed_get_achievement
        pause 7

    if persistent.muz_1_sr is True:
        play music pizdec fadein 5
        scene menushka
    if persistent.muz_2_sr is True:
        play music bilboards1 fadein 5
        scene menushkasr2
    if persistent.muz_3_sr is True:
        play music bilboards2 fadein 5
        scene menushkasr3
    if persistent.muz_4_sr is True:
        play music bilboards3 fadein 5
        scene menushkasr4
    if persistent.muz_5_sr is True:
        play music bilboards4 fadein 5
        scene menushkasr5
    if persistent.muz_6_sr is True:
        play music bilboards5 fadein 5
        scene menushkasr6
    if persistent.muz_7_sr is True:
        play music bilboards6 fadein 5
        scene menushkasr7
    if persistent.muz_8_sr is True:
        play music bilboards7 fadein 5
        scene menushkasr8

    show overlaymenushki

    with Fade(1.5, 1, 2)

    show overlaymenushki1
    pause 0.3
    call screen main_menu

label splashscreen:

    python:

        if not persistent.set_volumes:
            
            persistent.set_volumes = True
            
            _preferences.volumes['music'] = .65
            _preferences.volumes['sfx'] = 1.0
            _preferences.volumes['voice'] = .65
    if persistent.zastavka_skip is True:
        return
    elif True:
        jump spashcreen1

label spashcreen1:
    play music ctd fadein 2
    $ renpy.pause(3.5, hard=True)
    scene diskbg
    show zatemnenie_light
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with linearblurbolee
    $ renpy.pause(3.5, hard=True)
    show text "{size=50}{font=source/fonts/3.otf}Данная игра не ставит цели кого-то заоскать,\nкак малолетку конченную.\nВсе персонажи выдуманны.\nСовпадения случайны (считать вашей большой фантазией).\nПрежде чем сказать, что тут\nчто-то не так, помни:\nэта игра сделана одним типом\nза компом вечером под пивко.\nТакие дела, блять.{/font}{/size}":
        zoom 0.4 alpha 0
        ease 1.5 zoom 1.0 alpha 1
    pause 12
    show text "{size=50}{font=source/fonts/3.otf}Данная игра не ставит цели кого-то заоскать,\nкак малолетку конченную.\nВсе персонажи выдуманны.\nСовпадения случайны (считать вашей большой фантазией).\nПрежде чем сказать, что тут\nчто-то не так, помни:\nэта игра сделана одним типом\nза компом вечером под пивко.\nТакие дела, блять.{/font}{/size}":
        zoom 1.0 alpha 1
        ease 1.5 zoom 0.4 alpha 0
    pause 3
    stop music fadeout 6
    scene black with linearblurbolee
    $ renpy.pause(1, hard=True)
    python:
        _preferences.volumes['music'] = 1.0
    $ renpy.movie_cutscene('source/videosos/skrimer.webm')
    python:
        _preferences.volumes['music'] = 0.65
    play sound zaelo
    $ renpy.pause(2, hard=True)
    play sound ornulseblanov
    $ renpy.pause(5, hard=True)
    python:
        _preferences.volumes['music'] = 1.0
    $ renpy.movie_cutscene('source/videosos/zastavkaremaster.webm')
    python:
        _preferences.volumes['music'] = 0.65
    $ persistent.zastavka_skip = True
    return

label start:
    $ persistent.zastavka_skip = True
    play sound maloletka
    if persistent.muz_1_sr is True:
        scene menushka
        show overlaymenushki
    elif persistent.muz_2_sr is True:
        scene menushkasr2
        show overlaymenushki
    elif persistent.muz_3_sr is True:
        scene menushkasr3
        show overlaymenushki
    elif persistent.muz_4_sr is True:
        scene menushkasr4
        show overlaymenushki
    elif persistent.muz_5_sr is True:
        scene menushkasr5
        show overlaymenushki
    elif persistent.muz_6_sr is True:
        scene menushkasr6
        show overlaymenushki
    elif persistent.muz_7_sr is True:
        scene menushkasr7
        show overlaymenushki
    elif persistent.muz_8_sr is True:
        scene menushkasr8
        show overlaymenushki
    show overlaymenushki11
    stop music fadeout 2
    scene black with dissolve2
    pause 0.5

    if config.developer:
        scene nmallblur with ed_night_dis
        play ambience rain_out fadein 5
        scene nmall
        show doshd
        with dissolve2
        $ pps = 0
        "Куда наваливаем?"
        show zatemnenie with dissolve2
        jump scenariogovna1
    else:
        "По управлению... Свайп вверх - вызов недавнего меню."
        "Свайп вправо - скип."
        "Свайп влево - история диалогов."
        "Свайп вниз - скрыть интерфейс."
        "Отмена действия - повторное действие. Ещё раз сделай свайп, кароче."
        "Кнопки на текстбоке выполняют ровно то же самое."
        "Но на мобиле по ним хуй попадёшь."
        "Так что..."
        jump sr_samoe_nachalo_mlya

label scenariogovna1:
    menu:
        "{size=50}В самое начало{/size}":
            $ pps = 1
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump sr_samoe_nachalo_mlya
        "{size=50}На ключевой выбор{/size}":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            scene bergenbook with ed_night_dis
            jump carter5_vibor_suka_nahui
        "{size=50}Выбрать картер{/size}":
            menu:
                "{size=30}The Carter Zero: Сама суть{/size}":
                    stop ambience fadeout 5
                    scene nmallblur
                    hide nmall
                    hide doshd
                    with dissolve2
                    jump carter0
                "{size=30}The Carter One: Постигая основы безумия{/size}":
                    stop ambience fadeout 5
                    scene nmallblur
                    hide nmall
                    hide doshd
                    with dissolve2
                    jump carter1
                "{size=30}The Carter Two: Планапокалипсис{/size}":
                    stop ambience fadeout 5
                    scene nmallblur
                    hide nmall
                    hide doshd
                    with dissolve2
                    jump carter2
                "{size=30}The Carter Three: iNeoony's Revenge{/size}":
                    stop ambience fadeout 5
                    scene nmallblur
                    hide nmall
                    hide doshd
                    with dissolve2
                    jump carter3
                "{size=30}The Carter Four: Rotten Diary{/size}":
                    stop ambience fadeout 5
                    scene nmallblur
                    hide nmall
                    hide doshd
                    with dissolve2
                    jump carter4
                "{size=30}The Carter Five: Взломать Скитецкого{/size}":
                    stop ambience fadeout 5
                    scene nmallblur
                    hide nmall
                    hide doshd
                    with dissolve2
                    jump carter5
                "{size=30}The Carter Six{/size}":
                    menu:
                        "{size=30}Долгий путь домой{/size}":
                            $ pps = 4
                            stop ambience fadeout 5
                            scene nmallblur
                            hide nmall
                            hide doshd
                            with dissolve2
                            jump carter6_loner
                        "{size=30}Всё переплетено{/size}":
                            $ pps = 2
                            stop ambience fadeout 5
                            scene nmallblur
                            hide nmall
                            hide doshd
                            with dissolve2
                            jump carter6_skeetovij
                        "{size=30}Вернуться{/size}":
                            jump scenariogovna1
                "The Carter Seven: Exodus":
                    $ pps = 228
                    stop ambience fadeout 5
                    scene nmallblur
                    hide nmall
                    hide doshd
                    with dissolve2
                    jump carter7
                "{size=30}Вернуться{/size}":
                    jump scenariogovna1
        "{size=50}На финал{/size}":
            $ pps = 0
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump carter_ending
        "{size=50}На хуёвый финал{/size}":
            $ pps = 0
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump carter_ending_bad

label sr_samoe_nachalo_mlya:
    nvl clear
    nvlbazar "Обычно,{w=0.2} такие истории начинаются с <<жили,{w=0.2} были>>,{w=0.2} но в нашем случае:{w} <<сидели,{w=0.2} пили и не закусывали>>."
    nvlbazar "Да,{w=0.2} это история про одного Новошахтинского заводилу."
    nvl clear
    nvlbazar "Но чего ходить вокруг да около?"
    extend " Пиздуй смотреть заставку."
    nvl clear
    python:
        _preferences.volumes['music'] = 1.0
    $ renpy.movie_cutscene('source/videosos/opening.webm')
    python:
        _preferences.volumes['music'] = 0.65
    pause 2
    play music lw fadein 3
    scene nmallblur at sr_pokachivanie
    #with ed_night_dis
    scene nmall at sr_pokachivanie
    show doshd
    show zatemnenie
    with dissolve2
    $ MND_Chapter("BERGEN представляет")
    scene laba at sr_pokachivanie
    show lordsprclon4 at sr_pokachivanie
    show zatemnenie
    with ed_night_dis
    $ MND_Chapter("Визуальную новеллу")
    scene tolkanmall at sr_pokachivanie
    show ivettaspr at sr_pokachivanie
    show zatemnenie
    with ed_night_dis
    $ MND_Chapter("Skitetsky REMASTER")
    scene domint at sr_pokachivanie
    show zatemnenie
    with ed_night_dis
    $ MND_Chapter("В главных ролях:")
    scene bar100 at sr_pokachivanie
    show bergennorm at sr_pokachivanie
    show zatemnenie
    with ed_night_dis
    $ MND_Chapter("BERGEN")
    scene avtobusgorit at sr_pokachivanie
    show kazahspr at sr_pokachivanie
    show zatemnenie
    with ed_night_dis
    $ MND_Chapter("iNeoony")
    scene sovenok at sr_pokachivanie
    show coldspr1 at sr_pokachivanie
    show zatemnenie
    with ed_night_dis
    $ MND_Chapter("ColdFSociety")
    scene domint at sr_pokachivanie
    show deadlylxrd at sr_pokachivanie
    show zatemnenie
    with ed_night_dis
    $ MND_Chapter("Deadlylxrd")
    scene skitserun at sr_pokachivanie
    show zatemnenie
    with ed_night_dis
    $ MND_Chapter("skittels15")
    scene buhaem at sr_pokachivanie
    show zatemnenie
    with ed_night_dis
    $ MND_Chapter("И многие другие...")
    scene bergdomint1 at sr_pokachivanie
    show zatemnenie
    show ddoser:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'ddoser'
        parallel:
            xzoom 1
            linear 1.97 xzoom 5
            linear 1.71 xzoom -3
            linear 1.07 xzoom 1
        parallel:
            yzoom 1
            linear 1.97 yzoom 1
            linear 0.97 yzoom -3
            linear 1.81 yzoom 1
        parallel:
            zoom 1
            linear 1.97 zoom 1
            linear 0.97 zoom 1
    with Pause(4.85)
    show ddoser:
        xzoom 1 yzoom 1 zoom 1
    $ MND_Chapter("Приятного проходения блять")
    stop music fadeout 5
    jump carter0