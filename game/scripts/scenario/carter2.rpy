label carter2:
    $ pps = 12
    play music frosty
    scene sovenok with ed_night_dis
    scene sovenokblur with dissolve2
    $ MND_Chapter("The Carter Two:")
    $ MND_Chapter("Планапокалипсис")
    scene sovenok with dissolve2
    nvl clear
    nvlbazar "Ты говорил -{w=0.2} я слушал."
    nvlbazar "Так было всегда."
    nvlbazar "До одного момента."
    nvl clear
    nvlbazar "Какова цена ошибки?"
    nvlbazar "Каждый эту фразу понимает по-разному."
    nvlbazar "Как по мне -{w=0.2} если ты долбоёб,{w=0.2} то и ответишь соответствующе."
    nvlbazar "И наши святая троица пошла против дяди Димы совершенно не представляя,{w=0.2} что он может высрать в ответ."
    nvl clear
    nvlbazar "Не буду сразу выкидавать все козыри на стол."
    nvlbazar "Начнём с Дамирки Неони."
    nvl clear
    nvlbazar "Скит закинул его в бесконечное лето."
    nvlbazar "Каким образом?"
    nvlbazar "Блять ты заебал нахуй сказку интересную портить блядь ебанько{nw}"
    nvl clear
    nvlbazar "А попал он именно в подобие рута Мику."
    nvlbazar "Интригует,{w=0.2} правда?{w} Ахаха."
    nvl clear
    nvlbazar "Так вот наш Kossack очнулся в автобусе после драммы с тремя голосами."
    nvlbazar "А что было дальше мы с вами сейчас и узнаем."
    nvl clear
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Неони:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    scene int_bus_night
    show unblink
    pause 1
    nn "Хорошо вчера побухал..."
    nn "Ща в школу пойду..."
    window hide
    pause 2
    nn "Не понял." with vpunch
    nn "Какого хуя?" with vpunch
    "Дамирка огляделся и понял,{w=0.2} что попал в бесконечное лето."
    "Он знал об этой игре по рассказам Вечного."
    "Так что шансов у него было мало."
    $ say_poplil = True
    scene anim pizda_ot_skita with dissolve2:
        subpixel True
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        parallel:
            ease 4.4 zoom 2.1
        parallel:
            ease 4.4 xpos 0.45
        block:
            linear 20 rotate 360
            rotate 0
            repeat
    "Весь мир перед глазами Дамирки начал плыть."
    nn "Что{w=0.2}.{w=0.2}.{w=0.2}."
    "Он просто не знал,{w=0.2} что в такой ситуации делать."
    "Он стоял и ахуевал."
    "Ну,{w=0.2} как стоял..."
    "Лежал и корчился." with vpunch
    nn "Пи{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}здец{w=0.2}.{w=0.2}.{w=0.2}."
    "Это всё что он смог выдавить из себя."
    "Помимо лужи блевотины."
    "Лысая малышка не щадит никого." with vpunch
    window hide
    pause 1
    scene int_bus_night with flash
    "Однако,{w=0.2} его быстро отпустило."
    nn "Ебануться..."
    window hide
    pause 1
    "Окончательно придя в себя,{w=0.2} Дамирка возле сидения обнаружил ствол."
    nn "АХУЕТЬ!" with vpunch
    "Это была автоматическая винтовка M4A1 с расцветкой Сайрекс."
    window hide
    play sound dostalstvol
    show m1:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            ypos 2.0
            linear 0.30 ypos 1.0
    with Pause(0.60)
    show m1:
        ypos 1.0
    window show
    nn "Да тут по-богатому..."
    nn "Кем бы ты ни был,{w=0.2} от души,{w=0.2} братишка!" with vpunch
    window hide
    play sound ubralstvol
    show m1:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            ypos 1.0
            linear 0.21 ypos 2.0
    with Pause(0.60)
    show m1:
        ypos 2.0
    hide m1
    window show
    "Дамирка повесил ствол на плечо."
    "После чего поспешно ретировался на улицу."
    stop music fadeout 5
    window hide
    scene int_bus_night:
        align (0.5, 0.5) zoom 1
        ease 1.2 align (0.7, 0.4) zoom 1.5
    pause 1
    scene sovenok with vpunch
    nn "Ну типа."
    "Дамирка разглядывал эти ебучие ворота."
    nn "Похожи на те самые скитовые ворота."
    nn "Которые Вадимка вынес вперёд{w=0.2}.{w=0.2}.{w=0.2}.{w} Дверями?"
    nn "гы" with vpunch
    window hide
    play music sexmetal
    pause 1
    "Около ворот лежало три магазина для винтовки."
    "Дамирка поднял их."
    window hide
    pause 1
    "Он стоял и глазел как баран на новые ворота."
    "Впрочем,{w=0.2} так и было."
    "До одного момента."
    window hide
    pause 1
    "Дамирка услышал сзади какое-то копошение."
    "Он обернулся."
    scene ext_bus_night
    show slzombar
    with pushright
    window hide
    play sound da_ti_zaebal
    pause 1
    play sound dostalstvol
    show m1:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            ypos 2.0
            linear 0.30 ypos 1.0
    with Pause(0.60)
    show m1:
        ypos 1.0
    play sound osechka
    hide m1
    show m1:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            pos (0.5, 1.0)
            linear 0.08 pos (0.53, 1.05)
            linear 0.08 pos (0.5, 1.0)
    with Pause(0.60)
    show m1:
        pos (0.5, 1.0)
    play sound blyat
    pause 0.5
    hide m1
    play sound mone
    show m2:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'm2'
        parallel:
            ypos 1.0
            linear 0.20 ypos 1.07
    with Pause(0.60)
    show m2:
        ypos 1.07
    hide m2
    play sound mtwo
    show m3:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'm3'
        parallel:
            pos (0.5, 1.07)
            linear 0.16 pos (0.6, 1.0)
    with Pause(0.60)
    show m3:
        pos (0.6, 1.0)
    hide m3
    play sound mthree
    show m4:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'm4'
        parallel:
            pos (0.5, 1.15)
            linear 0.16 pos (0.5, 1.0)
    with Pause(0.60)
    show m4:
        pos (0.5, 1.0)
    hide m4
    play sound mfour
    show m5:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'm5'
        parallel:
            xpos 0.5
            linear 0.16 xpos 0.75
            linear 0.16 xpos 0.5
        parallel:
            ypos 1.0
            linear 0.40 ypos 1.06
    with Pause(0.60)
    show m5:
        pos (0.5, 1.04)
    hide m5
    show m1:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            ypos 1.06
            linear 0.16 ypos 1.0
    with Pause(0.60)
    show m1:
        ypos 1.0
    hide m1
    play sound strelnul
    hide slzombar
    show slzombar1
    show m1:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            pos (0.5, 1.0)
            linear 0.08 pos (0.6, 1.15)
            linear 0.08 pos (0.5, 1.0)
    with Pause(0.60)
    show m1:
        pos (0.5, 1.0)
    hide slzombar1
    hide m1
    show slzombar1:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.7 ypos 2.0
    show m1
    play sound padenie
    pause 1
    hide slzombar1
    nn "Фух мля..."
    "Дамирка одним хедшотом вынес эту мразь."
    "Потом он опомнился,{w=0.2} ведь могут и со стороны ворот полезть хуебесы."
    "Дамирка развернулся,{w=0.2} и{w=0.2}.{w=0.2}.{w=0.2}."
    scene sovenok
    with pushleft
    nn "Вроде никого."
    play sound fnaf 
    show us_dead:
        xalign 0.5 yalign 0.5
        linear 0.3 zoom 5.5
    with vpunch
    $ renpy.pause(0.3)
    hide us_dead with dspr
    play sound2 padenie
    scene nebo1 with vpunch
    window hide
    pause 0.4
    play sound neeet
    with vpunch
    pause 0.4
    with vpunch
    pause 0.4
    with vpunch
    pause 0.4
    with vpunch
    pause 0.4
    play sound bm16_shoot
    scene nebo2 with vpunch
    window hide
    pause 0.8
    play sound padenie
    stop music fadeout 3
    scene nebo with vpunch
    cld "ВСТАВАЙ!" with vpunch
    scene sovenok
    show coldspr1
    with pushup
    play music flowers
    cld "Ебать ты лох,{w=0.2} брателло."
    nn "Колд, {w=0.2}ты?" with vpunch
    cld "Именно."
    cld "Пришёл спасти твою сраку."
    nn "Вовремя однако."
    cld "Мог и раньше." with vpunch
    cld "Просто хотел посмотреть на ебло твоё ахуевающее." with vpunch
    nn "Ну ты и мудила."
    nn "Я там чуть не усрался."
    cld "Ахаха." with vpunch
    cld "Ладно,{w=0.2} нам пора валить отсюда нахуй."
    cld "Это,{w=0.2} конечно, {w=0.2}остатки зомбарей."
    cld "Вечный и Вадимка тут уже постарались."
    cld "Тут вообще такая заваруха была, {w=0.2}пока тебя не было." with vpunch
    scene ext_road_night
    show coldspr1
    with pushright
    nn "Почему нам не съебаться на автобусе?"
    cld "Диман пробовал."
    cld "Как итог -{w=0.2} не заводится."
    nn "И он тут был?"
    cld "Да."
    cld "Там история просто под чай с пельменями."
    cld "Вечному воспоминание подменили."
    cld "Он думал,{w=0.2} что выехал со своим братом в другой конец города до девушки брата,{w=0.2} после чего уснул в 99 лиазике."
    cld "Но на деле всё оказалось куда серъёзнее."
    cld "Ебучий Скит..." with vpunch
    cld "И откуда у него такие силы только,{w=0.2} а?"
    stop music fadeout 5
    cld "Ну так вот{w=0.2}.{w=0.2}.{w=0.2}."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Вечного:")
    hide zatemnenie with dissolve2
    window hide
    pause 1
    play music sirius fadein 2
    pause 2
    scene act1komnata with ed_earth_draw
    "Наше унылое чудо сидело за компом." with dissolve2
    "Лениво потягиваюсь оно сделало последний глоток лимонной аскании."
    play sound drink
    window hide
    pause 0.6
    stop sound
    "Оно оглядело комнату."
    brg "Снова я втыкаю в никуда."
    "Да ну нахуй? {w=0.2}Неужели доходить начинает?"
    brg "Ща ещё малень поебланю и сяду за написание сюжета."
    "А,{w=0.2} нет."
    window hide
    pause 1
    brg "Сколько там сигарет осталось?"
    brg "Надеюсь,{w=0.2} что Саня не все спыхал."
    "Оно лениво посмотрело в пачку."
    "Там оставалась -{w=0.2} аж целая одна сигарета."
    brg "Надо пойти покурить."
    "И оно двинуло на балкон."
    play sound ssanayadver
    window hide
    pause 3
    scene akt1ciga1 with ed_alpha_diss_fast
    window hide
    pause 3
    brg "Последняя..."
    "Оно...{w} Ладно,{w=0.2} знаю,{w=0.2} заебал с этим Оно..."
    "Кароче:{w=0.2} Вечный подкурил ластовую сигу."
    play sound ciga0
    scene akt1ciga2 with ed_earth_draw
    play sound ciga1
    window hide
    pause 2
    "Он делает глубокую тягу."
    play sound kashel
    window hide
    pause 1.4
    brg "Крепкие,{w=0.2} сука..."
    scene akt1ciga4 with ed_night_dis
    brg "Пепельница уже почти вся полная..."
    scene akt1ciga3 with ed_night_dis
    "Пока Вечный курил, {w=0.2}он думал о сюжете финальной обновы."
    brg "Если бы это не было бы слишком локльно,{w=0.2} можно было бы и в воркшоп..."
    brg "Но..."
    brg "Похуй.{w=0.2} Всё равно я это доделаю."
    brg "Уже скольким обещал."
    window hide
    play sound ciga1
    pause 2
    scene akt1ciga5 with ed_night_dis
    play sound ciga2
    window hide
    pause 2
    stop sound
    scene akt1ciga6 with ed_earth_draw
    "Вечный пошел садиться обратно за комп."
    play sound ssanayadver
    window hide
    pause 3
    scene akt1ciga7 with ed_alpha_diss_fast
    window hide
    pause 3
    "На ноуте был открыт Notepad с первыми набросками текста."
    "Руки уже потянулись к клавиатуре,{w=0.2} как..."
    play sound pda1
    scene akt1ciga7 with vpunch
    window hide
    pause 1.5
    brg "Блять,{w=0.2} я очконул..."
    "Он проверил уведомления на телефоне."
    "Ему написал старый добрый..."
    vsn "Здарова."
    play sound pda1
    vsn "Свободен сегодня?"
    "Ответ не заставил себя долго ждать."
    brg "Ясен хуй."
    brg "Предлагаешь пойти куда,{w=0.2} чтоль?"
    play sound pda1
    vsn "Именно."
    th1 "Бля,{w=0.2} надо звук выключить,{w=0.2} громко сука."
    vsn "Прикатывай до меня."
    vsn "Тебя будет ждать не кислый такой сюрприз."
    brg "Выдвигаюсь."
    scene act1komnata with ed_earth_draw
    brg "Не судьба мне сегодня сесть за написание."
    scene act1komnata with vpunch
    shv "Забеись поспал."
    brg "Да ёбана."
    play sound smehshvilli
    "Швилли начал заливаться."
    stop music fadeout 5
    brg "Это ещё что за нахуй?"
    shv "Тебе мой смех не нравится?"
    window hide
    pause 0.5
    brg "Ладно,{w} похуй."
    window hide
    pause 0.7
    brg "Че снилось-{w=0.2}то хоть?"
    shv "Хм..."
    "Швилли погрузился в воспоминания."
    play sound fb
    play music crysis3epilogue fadein 2
    scene roofburn
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with flash
    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1
    with dissolve

    shv "Идите к папочке!" with dissolve2
    play sound dostal
    show SVD_wovystr_LW0607:
        ypos 0.25
        ease 0.5 ypos 0.05

    brg "Саня,{w=0.2} стреляй блеать!"
    $ _window_hide(dissolve)

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607

    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    $ renpy.pause (1)

    $ _window_show(dissolve)
    shv "Заряжаюсь!"
    window hide
    pause 0.5
    play sound gamaz
    pause 1
    stop sound
    "Вечный с криком влетел внутрь здания, {w=0.2}в то время когда Саня не мог сосредодочиться и попасть в голову зомбарю."
    shv "Еблан,{w=0.2} ты что делаешь?!"
    "Швилли полетел за ним."
    $ _window_hide(dissolve)

    scene burnint
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with ed_alpha_diss_fast
    play sound dostal
    show SVD_wovystr_LW0607:
        ypos 0.25
        ease 0.5 ypos 0.05

    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1
    with dissolve

    $ renpy.pause (2, hard=True)

    show bergen with dissolve:
        xpos 0.1
        zoom 1.5
        ypos -0.25

    $ _window_show(dissolve)
    brg "Прощай...{w=0.2} Швилли...{w=0.2} нет, Саня...{w=0.2} увидимся там,{w=0.2} где окажемся."
    $ _window_hide(dissolve)
    hide bergen
    play sound gamaz
    show bergen:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.7 ypos 2.0
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.7 ypos 2.0
    pause 1
    stop sound
    $ _window_show(dissolve)
    "Гниль вцепилась в шею Вечному."
    play sound suka1
    shv "СУКА!" with vpunch
    play sound suka2
    shv "СУКААААА!" with vpunch
    play sound suka3
    shv "СУКА{w=0.1}А{w=0.1}А{w=0.1}А{w=0.1}А{w=0.1}А!" with vpunch
    window hide
    hide SVD_wovystr_LW0607
    play sound clipin
    show SVD_wovystr_LW0607:
        ypos 0.0
        ease 0.5 ypos 0.5

    pause 1
    hide SVD_svystrel_LW0607
    play sound clipout
    show SVD_wovystr_LW0607:
        ypos 0.5
        ease 0.5 ypos 0.05

    pause 1
    "Швилли перезарядил СВД."
    scene burnint
    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1

    show layer master at VHS(0.83, 0.83, 0.77, 1.0)

    $ _window_hide(dissolve)

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607

    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center


    $ _window_show(dissolve)
    shv "сдохните...{w} Сдохните...{w} СДОХНИТЕ!"
    $ _window_hide(dissolve)

    stop music fadeout 3
    pause (0.4)

    show slzombar:
        xpos 0.1
        ease 0.4 zoom 1.7 xpos 0.5

    play sound noj1
    show sl_blkg_LW0607 with hpunch
    show dark_LW0607
    show blood_LW0607
    hide sl_blkg_LW0607
    with ed_flash_red
    $ say_pizdec = False
    play sound smehshvilli2
    pause 0.32
    play sound smehshvilli3
    pause 0.32
    play sound smehshvilli2
    pause 0.75
    stop sound
    play sound fb
    scene akt1ciga7 with flash
    pause 1
    "Вернувшись в реальность,{w=0.2} он ответил." with dissolve2
    shv "Да не, {w}нихуя интересного..."
    play music fools fadein 2
    window hide
    pause 1
    shv "Ты идёшь щас куда?"
    brg "Только собирался выдвигаться."
    brg "А что?"
    shv "Я тоже выдвигаюсь."
    shv "На 99 поедем?"
    brg "Он туда недоижжяит."
    shv "Ну похуй,{w} прогуляешься."
    brg "Да ты ахуел."
    brg "Да и с каких пор ты решил оставить такси и погонять на лиазике?"
    window hide
    pause 1
    shv "Ну, блять{w=0.2}.{w=0.2}.{w=0.2}.{w} Сложная экономическая ситуация."
    brg "Хах."
    brg "Я тебя понял."
    window hide
    pause 2
    scene vishel1 with ed_night_dis
    "Вот они уже стоят в лифте."
    window hide
    pause 1
    "Теперь они на первом этаже."
    play sound liftsuka
    window hide
    pause 2
    scene vishel2 with ed_night_dis
    brg "Какой прекрасный день!"
    brg "Запахи говна из под свежескошенной обосраной собаками травы неприятно щекочут ноздри."
    brg "Хочеться блевануть."
    shv "Ну а хули ты хотел?"
    brg "Вот то-то ж и оно."
    scene vishel2:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat
    "Они двинули к остановке."
    scene vishel3 with ed_night_dis:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat
    shv "Мне надо сегодня будет кое-что проверить."
    window hide
    pause 1
    brg "Что именно?"
    window hide
    pause 1
    shv "Да есть тут одна диллема..."
    shv "Мне будет грустно,{w} если она подтвердится."
    window hide
    pause 1
    scene vishel4 with ed_night_dis:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat
    brg "Будешь ловить рофлан грустинки?"
    shv "Конечно."
    window hide
    pause 1
    scene vishel5 with ed_night_dis:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat
    brg "А меня Вишневский вызывает."
    brg "Нахуя?{w} Я так и не понял."
    window hide
    pause 1
    brg "Надеюсь,{w} на что-то стоящее."
    window hide
    pause 1
    scene vishel6 with ed_night_dis:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat
    "Они почти пришли."
    window hide
    pause 1
    "Вдалеке показался подъезжающий лиазик."
    brg "Бля..."
    shv "Успеем."
    "Они они рванули,{w} буд-то убегали от злого доберманчика."
    scene vishel6 at ed_running_fast
    window hide
    pause 2
    scene vishel7 at ed_running_fast
    window hide
    pause 2
    scene vishel8 at ed_running_fast
    window hide
    pause 2
    scene vishel9 at ed_running_fast
    window hide
    pause 2
    scene liazik99 with vpunch
    play sound ustal
    window hide
    pause 2
    shv "Успели..."
    stop music fadeout 5
    window hide
    pause 1
    brg "Да..."
    show blink
    stop sound
    "Он закрыл глаза,{w} чтоб лучше перевести дыхание."
    play sound avtobus11
    window hide
    pause 9
    "Ииии..."
    window hide
    pause 1
    play sound avtobus12
    scene int_bus
    show unblink
    window hide
    pause 13
    play sound baran
    scene int_bus with vpunch
    window hide
    pause 1
    th1 "Чё бля происходит?" with dissolve2
    hide unblink
    window hide
    pause 1
    play sound manda
    scene int_bus with vpunch
    "Вечный решил подойти ближе."
    scene int_bus:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat

    window hide
    pause 2
    scene int_bus
    show dimanspr at right
    play sound bochka
    dmn "Да ехай блять ебучая бочка!"
    play sound supersmeh
    window hide
    pause 1
    window hide
    pause 0.5
    play sound dimann
    brg "Диман!"
    window hide
    play music rastncbp
    pause 1
    dmn "А ты ещё откуда взялся?"
    brg "Честно?"
    brg "А ну хер его знает."
    window hide
    pause 1
    brg "Я со Швильком ехал..."
    window hide
    pause 1
    brg "Бля..."
    brg "А где Швилли?"
    dmn "Я тут только тебя вижу."
    th2 "Пиздец, без Сани тут будет грустно."
    window hide
    pause 1
    brg "Я тут спросить хотел."
    brg "Ты чё орёшь сука?!"
    window hide
    pause 1
    dmn "Да эта ебучая бочка не заводится нихера!"
    dmn "А меня за этим и послали."
    brg "Кто?"
    dmn "Мёртвый Лорд."
    window hide
    pause 1
    brg "Колокольчик нигде не отозвался."
    dmn "Ну блять,{w=0.3} Вадимка,{w=0.2} во!"
    brg "Понятно."
    window hide
    pause 1
    dmn "Зайди к нему тогда,{w} мне ещё возиться и возиться с этой хуйнёй!"
    brg "Где его найти хоть?"
    dmn "В здании клубов должен быть."
    window hide
    pause 1
    th1 "Я чё блять..."
    th1 "В бесконечное лето попал?"
    "Вечный посмотрел в окно."
    brg "Ахуеть..."
    dmn "Что?"
    brg "Да я в окно наконец додумался посмотреть..."
    window hide
    pause 1
    dmn "Тебя только это удивляет?"
    brg "Да нет."
    brg "В ориге же как было..."
    brg "Semen попадал в лагерь из будущего и из зимы."
    brg "А я,{w=0.2} сука,{w=0.2} с лета приехал."
    brg "Да и ты явно не похож на Славю."
    window hide
    pause 1
    "Диман о чём-то задумался."
    dmn "Всё,{w=0.2} иди до Вадимки,{w=0.2} мне ещё работать надо."
    brg "Увидимся."
    "Вечный двинул наружу."
    scene int_bus:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat

    show dimanspr at right:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat

    window hide
    pause 1.5
    scene ext_bus with ed_earth_draw:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat

    window hide
    pause 1
    scene ext_bus
    window hide
    pause 0.5
    brg "И когда я успел только..." with dissolve2
    scene ext_camp_entrance_day with pushleft
    brg "Оказаться в игре,{w=0.2} сука!?"
    window hide
    pause 1
    stop music fadeout 4
    th1 "Это же один большой сюжет..."
    th1 "Который написал один больной на голову человек..."
    th1 "Смешно..."
    play music ctamus fadein 2
    window hide
    pause 2
    scene ext_bus with pushright
    show dimanspr at right
    dmn "У нас ебейшие проблемы!"
    "Вечный обернулся на крики этого полоумного."
    dmn "Хватай винтовку и смотри в оба!"
    dmn "Сейчас сюда целая орава приползёт нахуй!"
    window hide
    pause 0.5
    play sound dostal
    show shstvol1:
        ypos 0.25
        ease 0.5 ypos 0.05

    "Вечный взял в руки G36."
    brg "Повеселимся?"
    dmn "Нас сожрут нахуй!"
    dmn "Какое веселье?!"
    th1 "Диман чёта паникует попусту."
    th1 "Всё равно пока никого нет."
    scene ext_road_day with pushright
    play ambience zattack
    dmn "Смотри!"
    window hide
    show slzombar:
        subpixel True default
        parallel:
            Null(233.0, 720.0)
            'slzombar'
        parallel:
            xpos -1.0
            linear 0.35 xpos 0.2
    with Pause(0.60)
    show slzombar:
        xpos 0.2
    window show
    "Первый зомбарь был уже очень близко."
    "Но,{w=0.2} как вы понимаете,{w=0.2} Вечный так просто не помрёт."
    play sound dostal
    show shstvol1:
        ypos 0.25
        ease 0.5 ypos 0.05

    $ _window_hide(dissolve)

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11

    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1
    hide slzombar
    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    hide slzombar
    hide shstvol1
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show shstvol1
    play sound padenie
    pause 1
    scene ext_road_day
    show shstvol1
    brg "Первый зомбарь готов."
    play sound gotovgad
    dmn "Хорошо приложил гада!"
    "В магазине осталось 26 патронов."
    dmn "Но это ещё не все!"
    window hide
    pause 1
    dmn "Смотри!"
    window hide
    show slzombar:
        subpixel True default
        parallel:
            Null(233.0, 720.0)
            'slzombar'
        parallel:
            xpos -1.0
            linear 0.35 xpos 0.2
    with Pause(0.60)
    show slzombar:
        xpos 0.2
    window show

    brg "Вижу!"

    $ _window_hide(dissolve)

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11

    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1
    hide slzombar
    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    hide slzombar
    hide shstvol1
    stop ambience
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show shstvol1
    stop music fadeout 3
    play sound padenie
    pause 1
    brg "Второй зомбарь готов."
    play music surface fadein 2
    scene ext_bus with pushleft
    show dimanspr at right
    dmn "Давай ствол и беги в лагерь,{w=0.2} я задержу остальных!"
    dmn "Ты там гораздо нужнее!"
    brg "Хорошо."
    brg "А почему второго ствола нет?"
    dmn "Да потому что блеать никто не ожидал тебя тут увидеть."
    brg "Ладно,{w=0.2} я побежал!"
    scene ext_bus at ed_running_fast
    show dimanspr at ed_running_fast
    window hide
    pause 2
    scene ext_camp_entrance_day at ed_running_fast with pushleft
    window hide
    pause 1
    scene ext_clubs_day at ed_running_fast
    window hide
    pause 1
    play sound sukispasite
    scene ext_clubs_day with vpunch
    th2 "Это из клубов."
    th1 "У меня ствола нет,{w=0.2} хули мне туда лезть?"
    th2 "Да может кого шкафом придавило."
    th "Ладно,{w=0.2} была не была!"
    play sound door_break
    scene int_clubs_male_day_baza
    show sheped_grust at right
    show slzombar:
        xpos 0.1
    with vpunch
    play ambience zattack
    "В клубах сидел наш старый знакомый."
    shg "Помоги брат!"
    shg "Зомбарь отжал у меня ПМ!"
    "Вечный заметил ПМ возле своих ног."
    play sound dostal
    show pistolpm1:
        ypos 0.25
        ease 0.5 ypos 0.05

    "Вечный взял пистолет."
    play sound pomogite
    window hide
    pause 2
    play sound idu1
    pause 2.5

    play sound pmshot111
    show pistolpm11
    hide pistolpm1
    $ renpy.pause (0.05)
    show pistolpm1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide pistolpm11

    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound pmshot111
    show pistolpm11
    hide pistolpm1
    $ renpy.pause (0.05)
    show pistolpm1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide pistolpm11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound pmshot111
    show pistolpm11
    hide pistolpm1
    $ renpy.pause (0.05)
    show pistolpm1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide pistolpm11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound pmshot111
    show pistolpm11
    hide pistolpm1
    $ renpy.pause (0.05)
    show pistolpm1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide pistolpm11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    hide slzombar
    hide pistolpm1
    stop ambience
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show pistolpm1
    play sound padenie
    pause 1
    stop music fadeout 3
    brg "Вот и всё."
    window hide
    hide pistolpm1
    play sound ubralstvol
    show pistolpm1:
        ypos 0.05
        ease 0.5 ypos 1.0
    hide sheped_grust
    show sheped at right
    window show
    "Вечный убрал ствол и отдал его Депешу."
    shg "По гроб жизни должен буду!"
    hide pistolpm1
    play music cctvcut
    brg "В лагере есть есть зомби?"
    shg "Да хз."
    shg "Я по датчикам смотрел когда,{w=0.2} то видел какие-то три приближающиеся объекта."
    brg "То есть,{w=0.2} зомбарей было всего трое?"
    shg "Получается."
    brg "И всех троих грохнул я."
    brg "Совпадение?"
    shg "А остальные два где были?"
    brg "Со стороны дороги пёрли."
    brg "Благо Диман помог."
    shg "Как,{w=0.2} если он даже стрелять не умеет?"
    brg "Ну так ствол-то у него был."
    shg "Ну,{w=0.2} тоже верно."
    window hide
    stop music fadeout 4
    pause 1
    brg "А ты как тут оказался вообще?"
    shg "Это долгая история."
    brg "Я никуда не тороплюсь."
    shg "Ну... Слушай."
    play music ripper fadein 2
    hide sheped
    show dust1
    show dust2
    show dust3
    show dust4
    with linearblurbolee
    nvl clear
    nvlbazar "Вот знаешь... Так бывает..."
    nvlbazar "Каждый должен к чему-то стремиться. Очевидные вещи, говоришь? Именно. Но соль – в другом."
    nvlbazar "Есть тут один паца… Пожилая гаргулья… Так вот: он воспринял это утверждение буквально, да настолько, что добился всего того, что хотел. С этого момента поподробнее…"
    nvlbazar "Жил, был, не тужил – один паца… Гошаном его звали. С самого детства он имел пристрастии к копрофилии. Какое интригующее начало, ага? Ха-ха…"
    nvl clear
    nvlbazar "У него была тян – звали её Джокершей. Она имела те же фетиши, что и Гошан. Встретились они при очень странных и угарных обстоятельствах: Гошан работал в ТРЦ «Стрекоза» профессиональным сантехником – менял трубы, ремонтировал смыв параши (который, к слову, там часто ломался), да делал прочую хуйню."
    nvlbazar "У той самой тян случился приступ рвения очка (шава на манеже передаёт привет), после чего она буквально на жопной тяге долетела до ТРЦ, где минут 5, бегая, искала парашу."
    nvlbazar "Буквально запрыгнув на парашу, где в полёте были скинуты штаны с кружевными труселями, она начала процесс эякуляции через жопу. Блаженству не было предела."
    nvlbazar "Однако, минут через десять – эйфория быстро сошла на нет: в том толчке не было бумаги… И тут наступает процесс кульминации истории."
    nvl clear
    nvlbazar "Гошан был неподалёку – чинил кран возле умывальника… И, увидев, что в парашу на жопной тяге летит красивая тян, начал возбуждаться. Услышав звуки эякуляции через очко – его «скала» затвердела так, что ей можно было колоть алмазы. Ну и, соответственно – он начал дрочить."
    nvlbazar "Кончив за 29 секунд, он было хотел вернуться к работе, как вдруг – услышал тихие, матные, очень злобные причитания из кабинки. Тянка причитала, мол: «уёбки, сука, ненавижу вас, блиять!!!11! Кто всю бумагу в толкан запихал? Как жопку мою драгоценную вытереть, да смыть теперь это говно??!??!»."
    nvlbazar "Взяв свою решимость и волю в кулак, да зашёл в ту кабинку, где причитала тянка. Это была картина маслом: раком, с голой жопой, которая вся в кале, стояла тянка. И Гошан, ебать: со словами «айм сорри, мэн» достал свой питон и начал вставлять."
    nvlbazar "Хуй был весь в говне, но тянус против не была (ахуеть ужас блять). После процесса пришлось обоим мыться в раковине: тянус мыла очко, а Гошан мыл питона. Потом, правда, у него инфекция пошла, но он её вылечил."
    nvl clear
    nvlbazar "Во все следующие разы говяного совокупляния Гошан юзал защиту. Нет, не презерватив – он напяливал три пакета на хуй, ведь в инете он вычитал, что – чем толще защита – тем дольше не будешь кончать. Ебанько он, кароче. "
    nvlbazar "Так вот – одним майским вечером он думал устроить со своей тян обряд говяного экзорцизма – засасывать друг друга везде, при этом обмазавшись экскриментами. И-и-и… Казалось бы – всё должно было пойти по плану, но как бы не так…"
    nvlbazar "Когда он с букетом роз прыгал в свой «толкано-мобиль», ему везде мерещился его старый знакомый – дядя Дима Скит. Причём – не просто мерещился, а предлагал пойти с ним. Гошан понял, что хуйня идея, и, дабы заглушить эти галюны – осушил чекушку 0.25 водки «5 озёр» и запил всё это дело «ягодной асканией»."
    nvl clear
    nvlbazar "В таком состоянии он сел за руль своей левитирующей параши. В чём проблема, спросите вы?"
    nvlbazar "Он летел со скоростью 228 километров в час, да не вписался в поворот – на улице «Фрунзенская», у него, в Волгограде – стояла общественная параша. Засранная вся. Вот прям в говне всё было…"
    nvlbazar "Ну и – Гошанчик въехал прямо в двери на своей хуйне – лишь его ебло выглядывало из толчка, слёзно молящее вытащить оттуда его… Но никто не вытащил."
    nvlbazar "Жижа из говна и ссанины поглощала Гошана в темноту очка с головой… Но в последний момент он увидел знакомое ебало…"
    nvl clear
    stop music fadeout 3
    nvlskt "Ты пойдёшь со мной?"
    nvlbazar "Спросил его Дима."
    nvlbazar "И Гошан согласился."
    show sheped at right
    hide dust1
    hide dust2
    hide dust3
    hide dust4
    with linearblurbolee
    shg "Вот такие дела."
    play sound doebaliuzhe
    window hide
    pause 13
    "Вкинув рофляный оск, Вечный вспомнил,{w=0.2} зачем он пришел к клубам."
    brg "Не знаешь,{w=0.2} где найти Мёртвого Лорда?"
    shg "Зачем он тебе?"
    brg "Диман посоветовал его найти."
    window hide
    pause 1
    shg "Вообще,{w=0.2} он может быть где угодно."
    shg "Но для начала я бы советовал тебе проверить музклуб."
    shg "Если ещё помнишь, {w=0.2}где это."
    brg "Я тебя понял."
    window hide
    pause 1
    "И Вечный двинул искать Мертвого Лорда в музклуб."
    "Ну а сейчас..."
    play music highschool fadein 3
    scene int_catacombs with ed_earth_draw
    strlk "Заколебало уже тут париться..." with dissolve2
    strlk "Только телеэфиры меня и спасают."
    "Стрелок включил телевизор."
    window hide
    pause 1
    stop music fadeout 2
    "Включив единственный ловящий тут канал,{w=0.2} началась реклама."
    play sound reklama1
    window hide
    pause 18
    stop sound
    play music highschool fadein 3
    strlk "Обожаю эту хуйню!"
    "Такая реклама всегда поднимала настроение."
    "Наверное потому,{w=0.2} что он ещё не думал о том..."
    "Что все эти смехуёчки превратились в реальную деградацию."
    window hide
    pause 1
    "А может и думал."
    "Но ему было похуй."
    "Это же Стрелок."
    window hide
    pause 1
    "После рекламы началась его любимая передача..."
    "Comedy Sheped."
    "Там ведущий рассказывает свои ахуительные истории."
    "Сопровождая их нереальным ором."
    razrab "Где-то это уже было, {w}не?"
    th1 "Иди нахуй отсюда."
    razrab "У{w=0.2}-у{w=0.2}-у{w=0.2},{w=0.2} сука{w=0.2}({w=0.2}9"
    window hide
    pause 1
    strlk "Началось!"
    stop music fadeout 2
    scene comedysheped with flash
    play sound tv1
    window hide
    pause 86
    stop sound
    play sound supersmeh
    scene int_catacombs with vpunch
    window hide
    pause 2
    strlk "До слёз,{w} сука!" with dissolve2
    window hide
    pause 2
    "Но тут стрелку пришло голосовое сообщение."
    window hide
    play sound pda3
    pause 0.5
    "Где полетели конкретные оски, с просьбой подняться."
    "Незамедлительно последовал ответ,{w=0.2} тоже гска."
    window hide
    play sound pda3
    pause 0.5
    "Где было доложено, мол: <<Сука, щас поднимусь, заебал>>."
    strlk "Сука,{w=0.2} тащиться к этому дцпешнику..."
    lis "Ради чего?"
    strlk "Вопрос остаётся открытым."
    "У него был целый гарем в этом мега подвале."
    th1 "Да и почему был?"
    "Стрелок создал себе всё для хорошей жизни."
    "И в этой хорошей жизни нет места всяким Семпаям."
    "Ну а сейчас..."
    scene black with ed_night_dis
    play sound fb
    scene squareanim with flash
    play music goloederevo fadein 3
    "Вечный сидел на лавочке и наслаждался видами." with dissolve2
    th "Эхх..."
    window hide
    pause 1
    th "Сколько модов было мной пройдено..."
    window hide
    pause 1
    th "БвС,{w=0.2} Пацанское лето,{w=0.2} 7ДЛ,{w=0.2} Саманта,{w=0.2} прочий треш..."
    th "Но это не главное..."
    window hide
    pause 1
    th "А как я впервые лето проходил?"
    th "Ебааа..."
    window hide
    pause 1
    th "И ведь все правильно сделал!" with vpunch
    th "Ну,"
    play sound podik
    extend " почти..."
    "Вечный затянулся ахуенной морозной жижей из миникана."
    "И кайфанул."
    th "А ведь когда лето впервые проходил,"
    play sound podik
    th " я ж ещё даже курить не начал..."
    window hide
    pause 1
    th "Насколько ж давно это было..."
    window hide
    pause 1
    th "Всё таки самый любимый момент -{w=0.2} с шахтами."
    th "И я хер его знает,{w=0.2} почему."
    window hide
    pause 1
    "Можно бесконечно гоняться хер пойми за кем."
    "С неизвестными целями."
    "Но одно Вечный знал точно -"
    play sound podik
    brg "Надо насладиться моментом."
    brg "Такая возможность выпадает {w=0.2}(если и выпадает){w=0.2} очень редко."
    window hide
    pause 1
    "Вечный ещё бы долго так просидел..."
    "Прокручивая очень старые,{w=0.2} очень добрые,{w=0.2} ностальгичные моменты."
    stop music fadeout 3
    "Как вдруг..."
    lis "Вечный!"
    scene black with ed_night_dis
    play sound fb
    scene int_old_building_night with flash
    play music pridengahpidor2 fadein 2
    strlk "Так,{w=0.2} а сейчас нужно сюрприз обойти..." with dissolve2
    window hide
    pause 2
    strlk "Ну вот и всё,{w=0.2} ебать."
    strlk "Где там это чучело?"
    "Стрелок вышел из здания."
    scene ext_old_building_night_moonlight
    show strelok
    with pushright
    window hide
    pause 1
    play sound chenado
    pause 1
    bergen1 "Да ниче особенного."
    bergen1 "Ты же понимаешь,{w=0.2} что это место под защитой?"
    strlk "Нет, {w=0.2}нихуя.{w=0.2} Я забыл о том,{w=0.2} что сам же её поставил."
    strlk "Дружище."
    play sound doebaliuzhe
    window hide
    pause 13
    bergen1 "Хм."
    bergen1 "Я сделаю вид,{w=0.2} что этого не было."
    bergen1 "Если ты ебальник завалишь и перестанешь возмущаться."
    bergen1 "И тогда может быть твоя жопка не будет изнасилована моим песюном."
    "Жопка Стрелка начала плавиться."
    strlk "Да ты ахуел!" with vpunch
    play sound dostal
    "Но когда Семпай достал ствол,{w=0.2} весь батхёрд сошёл на нет."
    window hide
    pause 1
    bergen1 "Ладно."
    bergen1 "Завтра сюда прибудет очень интересный персонаж."
    bergen1 "Если не забыл,{w=0.2} что на меня твоя защита не дейтсвует,{w=0.2} а ещё должен понимать,{w=0.2} что для завтрашнего гостя её нужно будет отключить."
    strlk "Сегодня чтоль?"
    bergen1 "Нет."
    bergen1 "Завтра и отключим."
    strlk "Ну, {w=0.2}хули{w=0.2}, пошли тогда в бункер."
    bergen1 "У меня как раз медовуха есть пол литра."
    strlk "Да ну нахуй?"
    bergen1 "Да-да,{w=0.2} пошли уже."
    stop music
    scene int_catacombs
    $ renpy.movie_cutscene("source/videosos/afewmomentslater.webm")
    play music pridengahpidor1
    scene int_catacombs with flash
    show strelok
    bergen1 "Ну что ж..."
    bergen1 "Неплохо ты тут устроился..."
    lis "Это ещё что за хрен?"
    strlk "Давай потом,{w=0.2} а?"
    strlk "От желания глотнуть медовухи аж челюсти сводит."
    bergen1 "Хм."
    bergen1 "Хорошо."
    "Семпай заметил,{w=0.2} что Стрелок имел в виду кого-то другого."
    "Но сделал вид что не заметил."
    window hide
    pause 1
    bergen1 "Лови медовуху!"
    show blazer at spizdil
    pause 2
    hide blazer with dissolve
    play sound otkrilblazer
    pause 1
    play sound na_popei
    pause 1.5
    "Стрелок сделал глоток."
    window hide
    pause 1
    strlk "Есть курить..."
    strlk "Я как снова в 2019..."
    bergen1 "Курить нету,{w=0.2} есть только подик."
    strlk "Да это образно говоря."
    strlk "Так-то я в завязке уже третий месяц."
    bergen1 "Понял тебя."
    bergen1 "А я попарю этот tance черного цвета 2020 века."
    play sound podik
    strlk "Ха-ах..."
    play sound na_popei
    extend " Вовремя ты ж появился,{w=0.2} однако..."
    "Стрелок сделал большой глоток."
    bergen1 "Да."
    play sound na_popei
    extend " Сука,{w=0.2} мне оставь, {w=0.2}а!"
    "Стрелок протягивает священную бутыль Семпаю."
    window hide
    pause 1
    bergen1 "Я хотел снова Врата Штейна пересмотреть..."
    play sound na_popei
    extend " Второй сезон, {w=0.2}как в старые добрые..."
    "Семпай делает большой глоток, {w=0.2}затем делает тягу на поде."
    play sound podik
    extend " Ту самую жижку бруско гранат."
    bergen1 "Добивай."
    "Семпай протягивает бутыль священого нектара."
    strlk "А чё так?"
    bergen1 "Да не лезет уже."
    "И стрелок добивает бутыль."
    play sound na_popei
    extend " Одним большим глотком."
    window hide
    pause 1
    strlk "Ох,{w=0.2} лягу,{w=0.2} пожалуй."
    strlk "Заебался за день."
    bergen1 "Давай."
    bergen1 "Ты только не засни!"
    strlk "А, {w=0.2}ок."
    window hide
    show blink
    stop music fadeout 3
    pause 3
    play music menu11
    hide blink
    scene black
    play sound slonik
    window hide
    pause 1.5
    scene bunkerson
    show pahom:
        xpos 0.1
        ypos 0.0
    show unblink
    window hide
    pause 44.5
    hide pahom
    show pahom1:
        xpos 0.1
        ypos 0.0
    pause 23
    play sound dostal
    show SVD_wovystr_LW0607:
        ypos 0.25
        ease 0.5 ypos 0.05

    pause 1
    play sound vystrel_LW06071
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607
    hide pahom1
    show pahom2:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    show hitmarkermlg_LW0607:
        ypos 0.0 xpos 0.28

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    pause 0.90
    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.015 xpos 0.28

    pause 0.125
    hide hitmarkermlg_LW0607
    hide pahom2
    hide SVD_wovystr_LW0607
    show pahom3:
        anchor (0.5, 0.5)
        pos (0.3, 0.5)
        ease 1.0 rotate 150 xpos 0.3 ypos 2.0
    show SVD_wovystr_LW0607
    pause 0.125
    play sound padenie
    pause 1
    stop music fadeout 3
    scene black with ed_earth_draw
    window hide
    pause 1
    play sound vstavai
    play music pridengahpidor1
    scene int_catacombs
    show strelok
    show unblink
    window hide
    pause 2
    bergen1 "Чё приснилось хоть?"
    "Стрелок вспомнил свой сон."
    window hide
    pause 1
    strlk "Там такая хуета,{w=0.2} тебе лучше не знать."
    window hide
    pause 1
    razrab "А сейчас мы вернемся к Вечному."
    stop music fadeout 3
    scene black with ed_night_dis
    window hide
    pause 1
    play sound fb
    scene squareanim with flash
    play music goloederevo fadein 3
    lis "Вечный!" with dissolve
    th1 "Кто там такой настрный только..."
    "Вечный обернулся."
    window hide
    show avelimespr:
        subpixel True default
        parallel:
            Null(754.0, 724.0)
            'avelimespr'
        parallel:
            ypos 2.0
            linear 1.00 ypos 1.0
    with Pause(1.10)
    show avelimespr:
        ypos 1.0
    window show
    avlm "Здарова,{w=0.2} заебал."
    brg "А,{w=0.2} ты."
    window hide
    pause 1
    avlm "А ты тут какими судьбами?"
    brg "Попал сюда я при невыясненных обстоятельствах."
    brg "Зачем?"
    play sound herznaet
    window hide
    pause 3
    brg "Как отсюда выбраться?"
    brg "Кхм." with vpunch
    brg "Аналогично."
    avlm "Да-а..."
    avlm "Не повезло тебе."
    brg "Мне никогда не везло."
    window hide
    pause 1
    "Повисло молчание."
    window hide
    pause 1
    avlm "Я че пришёл-то..."
    window hide
    pause 1
    avlm "Не поможешь пройти к одному очень интересному месту?"
    avlm "Старый лагерь зовётся оно."
    brg "А почему я?"
    brg "А как же Диман?"
    avlm "Нахуй его."
    avlm "Да и ты,{w=0.2} помнитcя,{w=0.2} говорил,{w=0.2} что лето проходил по 500 раз на дню."
    avlm "А я и решил, {w=0.2}что ты в этом ебучем лагере каждый уголок знаешь."
    brg "Сначала дойдём до музклуба."
    brg "Мертвий Лорд должен ждать меня там."
    brg "По крайнеё мере, мне так сказал Депеш."
    avlm "Ты уверен,{w=0.2} что он там?"
    brg "Нет." with vpunch
    brg "Но вариантов лучше у меня нет."
    avlm "Может,{w=0.2} он в старом{nw}"
    brg "Не может." with vpunch
    brg "Мы или идёт сначала в музклуб, {w=0.2}или ты просто пойдёшь нахуй." with vpunch
    "У Авелайма не оставалось выбора."
    avlm "Веди."
    play sound door_open
    scene int_musclub_day
    show avelimespr at right
    with ed_lap
    foma "Здарова бандиты." with vpunch
    brg "И тебе не хворать,{w=0.2} Фома."
    brg "Какими судьбами ты тут?"
    foma "Да вот школу,{w=0.2} в которой я работал,{w=0.2} закрыли."
    foma "А тут вакансия физрука была."
    foma "Вот я и решил податься в хлебные края."
    brg "Занимательно."
    brg "Слушай,{w=0.2} а ты не видел тут Мертвиго Лорду?"
    foma "Такой патлач и бородач одновременно?" with vpunch
    brg "Да."
    "Вечный немного орнул с такого точного описания Вадима Морозова."
    foma "Был недавно."
    foma "Искал какого-{w=0.2}то типа в белой пятнистой куртке..."
    foma "Погоди." with vpunch
    foma "Так это ж получается,{w=0.2} что он тебя искал?"
    brg "Походу."
    foma "Он был тут полчаса назад."
    foma "Сказал,{w=0.2} что отправится к какому-{w=0.2}то старому лагерю."
    foma "Честно,{w=0.2} я в рот не ебу,{w=0.2} где это."
    foma "Но он должен быть там."
    avlm "А я тебе говорил..."
    brg "Ладно,{w=0.2} бывай,{w=0.2} Фома!" with vpunch
    foma "Ну как проветритесь,{w=0.2} заходите."
    "И они двинули по направлению к старому лагерю."
    "По пути рассматривая окресности."
    play sound door_open
    scene ext_playground_day
    show avelimespr
    with ed_night_dis
    avlm "Это местная спортплощадка?"
    brg "Да."
    brg "А ты обход территории не делал шоль,{w=0.2} как попал сюда?"
    avlm "Нет, {w=0.2}мне похуй было."
    brg "Я тебя понял."
    "И они двинули дальше."
    scene ext_path_sunset
    show avelimespr
    with ed_night_dis
    brg "Я думал,{w=0.2} что будет чуть ближе."
    avlm "Да я тоже так думал."
    brg "Ладно.{w=0.2} Похуй."
    "Они двинули дальше."
    scene ext_path2_day_posral with ed_night_dis
    play sound polzasral
    window hide
    pause 2
    avlm "Чё там?"
    brg "Там говно."
    brg "Куча говна."
    brg "Огроменная куча говна."
    show avelimespr with dissolve
    avlm "Да я уже учуял."
    brg "И кто мог столько насрать..."
    play sound fb
    scene int_clubs_male_day_baza
    show sheped_grust at right
    show slzombar:
        xpos 0.1
    with flash
    window hide
    pause 2
    play sound fb
    scene ext_path2_day_posral with flash
    brg "Хотя..."
    brg "Я,{w=0.2} походу понял,{w=0.2} кто столько насрал."
    avlm "И кто же?"
    brg "Да ты всё равно его не знаешь."
    window hide
    pause 1
    razrab "А я вам,{w=0.2} пожалуй,{w=0.2} покажу,{w=0.2} как всё было на самом деле."
    stop music fadeout 3
    scene black with ed_night_dis
    play sound fb
    play music bilbordi fadein 3
    scene ext_path_day at ed_running_fast with flash
    play sound begtrava
    melles "Прижало-то как,{w=0.2} блять!"
    "Бедная жопка буквально трещала по швам."
    "Димочке было очень больно."
    "Он не знал,{w=0.2} где можно сбилдить новый чидори кернел."
    "И поэтому пришлось выбирать рандомное место."
    scene ext_path2_day with ed_flash_red
    stop sound
    melles "Всё,{w=0.2} пиздец,{w=0.2} больше не могу..."
    "А что было дальше..."
    window hide
    play sound perdun
    pause 1
    play sound rid1
    pause 0.6
    play sound rid2
    pause 0.7
    play sound rid3
    pause 0.6
    play sound rid4
    pause 0.7
    play sound rid5
    pause 1
    play sound rid6
    pause 0.9
    play sound rid7
    pause 1
    play sound rid8
    pause 1
    scene ext_path2_day_posral with dissolve2
    window hide
    pause 1
    "...Вы только что сами узнали."
    melles "Хорошо-то как..."
    play sound shepedtrava
    window hide
    pause 1
    melles "Кто здесь?"
    "На поляну вышел наш старый знакомый."
    "Далее от его лица."
    scene ext_path2_day_posral
    show melles_spr
    with flash
    shg "Ты ахуел?" with vpunch
    shg "Не,{w=0.2} ну ты внатуре ахуел!!" with vpunch
    shg "Тут я посрать должен был!"
    "Шепед тоже пританцовывал."
    "Бедный."
    shg "Да за такое..."
    shg "Я всем расскажу,{w=0.2} что это ты насрал!" with vpunch
    shg "Вот!" with vpunch
    window hide
    pause 0.5
    "Но Димочка не растерялся и выдал свою коронную фразу."
    melles "Ты никому ничего не скажешь..."
    play sound mellesbazarit
    window hide
    pause 4
    shg "Я тебя услышал..."
    stop music fadeout 3
    scene black with ed_night_dis
    play sound fb
    scene ext_path2_day_posral with flash
    avlm "А,{w=0.2} может,{w=0.2} знаю?" with dissolve2
    brg "Хм."
    brg "Не исключено."
    stop music fadeout 5
    window hide
    pause 3
    brg "Почти пришли."
    "Обойдя огромную каху,{w=0.2} они двинули дальше."
    window hide
    pause 2
    play music pritheme fadein 2
    play sound shepedtrava
    scene ext_old_building_sunset with ed_earth_draw
    play sound nameste
    window hide
    pause 1.5
    "Вечному на говнозвон приходит голосовое сообщение." with dissolve
    window hide
    pause 1
    show smska:
        subpixel True xpos 0.5 default
        parallel:
            Null(603.0, 724.0)
            'smska'
        parallel:
            ypos 2.0
            linear 1.00 ypos 1.0
    with Pause(1.10)
    show smska:
        pos (0.5, 1.0)
    play sound zona_a
    pause 8
    hide smska
    show smska:
        subpixel True default
        parallel:
            Null(603.0, 724.0)
            'smska'
        parallel:
            ypos 1.0
            linear 1.00 ypos 2.0
    with Pause(1.10)
    show smska:
        ypos 2.0
    brg "Не понял..."
    hide smska
    "Вечный отошел на безопасное расстояние."
    brg "Ты куда меня завёл?" with vpunch
    window hide
    pause 1
    "Вечный огляделся."
    window hide
    pause 1
    "Но Авелайма нигде не было."
    window hide
    play sound hernyakakayato
    pause 1
    show smska:
        subpixel True xpos 0.5 default
        parallel:
            Null(603.0, 724.0)
            'smska'
        parallel:
            ypos 2.0
            linear 1.00 ypos 1.0
    with Pause(1.10)
    show smska:
        pos (0.5, 1.0)
    play sound zona_a_off
    pause 3
    hide smska
    show smska:
        subpixel True default
        parallel:
            Null(603.0, 724.0)
            'smska'
        parallel:
            ypos 1.0
            linear 1.00 ypos 2.0
    with Pause(1.10)
    show smska:
        ypos 2.0
    brg "И?"
    hide smska
    "Тем временем в бункере..."
    stop music fadeout 5
    scene black with ed_earth_draw
    play sound fb
    play music chrnthme fadein 2
    scene int_catacombs
    show strelok
    with flash
    strlk "Защита отключена." with dissolve2
    strlk "Дальше что?"
    bergen1 "Ты не торопись."
    bergen1 "Лорд сделает всё красиво."
    bergen1 "Совсем скоро мы станем едины!"
    bergen1 "Как раньше..."
    strlk "Как до 2022 года?"
    bergen1 "Да!" with vpunch
    strlk "Скит,{w=0.2} конечно,{w=0.2} тоже молодец блять." with vpunch
    strlk "И нахуя он нас разделил?" with vpunch
    window hide
    pause 1
    bergen1 "Мы ему конкретно с забором подосрали." with vpunch
    window hide
    pause 1
    strlk "Поделом этой сучаре!" with dissolve
    window hide
    pause 1
    bergen1 "Вот и я про то же."
    window hide
    pause 1
    "Стрелку не нашлось, {w=0.2}что и сказать."
    bergen1 "Ну вот и всё."
    bergen1 "Решено!" with vpunch
    bergen1 "Ждём Лорда."
    stop music fadeout 6
    bergen1 "Он знает,{w=0.2} как эта херня работает."
    "Тем временем Диман и Депеш."
    scene black with ed_night_dis
    play sound fb
    play music lovewooman fadein 2
    scene int_clubs_male_day_baza
    show sheped
    with flash
    shg "Ты смотри!" with dissolve2
    "Шепед показал экран монитора Диману."
    shg "На лагерь прёт целая орава!"
    shg "Причём со стороны старого корпуса."
    play sound skolkoihzdes
    dmn "Как думаешь, {w=0.2}сколько их здесь?"
    play sound desyat
    shg "Десять?"
    play sound bolshe
    lxrd "Их тут гораздо больше." with vpunch
    play music mdknmus
    window hide
    pause 3
    show deadlylxrd:
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos -1.0
            linear 0.45 xpos 0.15
    with Pause(0.60)
    show deadlylxrd:
        xpos 0.15
    lxrd "Здарова,{w=0.2} дцпешники." with dissolve
    dmn "Здарова, {w=0.2}заебал."
    shg "Как жизнь пожилая?"
    lxrd "Неплохо."
    dmn "Чем вообще занимаешься?"
    lxrd "Да вот."
    window hide
    pause 0.7
    lxrd "Мне из трёх дцпешников нужно сделать одного."
    lxrd "Да направить его на путь истинный."
    shg "Он не в старом лагере, {w=0.2}случайно?"
    lxrd "Да."
    lxrd "А что?"
    window hide
    pause 1
    shg "Да туда ща орава зомбей прёт."
    dmn "Суда по датчикам,{w=0.2} скоро будет на месте."
    window hide
    pause 1
    lxrd "Хуёво."
    shg "И что делать будем?"
    lxrd "А сделаем так -"
    play sound fb
    scene ext_old_building_night_moonlight with flash
    extend " уже темно,{w=0.2} конечно,{w=0.2} но сражаться мы ещё сможем."
    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1
    with dissolve

    lxrd "Зомбарей будет тонна,{w=0.2} нам нужно крупнокалиберное оружие..." with dissolve2
    dmn "Есть СВД с экспансивными пулями."
    lxrd "Ну вот и отлично."
    lxrd "Возьмёшься отщёдкивать зомбей?"
    window hide
    pause 1
    dmn "Бля{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} Я стрелять не умею..."
    window hide
    pause 0.5
    lxrd "Мда...{w=0.2} А ты,{w=0.2} Депеш?"
    shg "Стрелять-то да.{w=0.2}.{w=0.2}.{w=0.2} Но вот попасть уже будет сложнее..."
    window hide
    pause 1
    lxrd "Ладно."
    extend " Хоть на что-то вы способны."
    dmn "Всегда рады!"
    lxrd "План такой:"
    show bergen at right
    with dissolve
    extend " нам нужно,{w=0.2} чего бы это не стоило, {w=0.2}спасти Вечного и его пиздабратию."
    hide bergen with dissolve
    lxrd "А ещё,{w=0.2} мы скорее всего успеем туда до прибытия зомбей."
    play sound dostal
    show SVD_wovystr_LW0607:
        ypos 0.25
        ease 0.5 ypos 0.05

    lxrd "А если нет -{w=0.2} Депеш,{w=0.2} пробуй стрелять!"
    $ _window_hide(dissolve)

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607

    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    extend " Не убьёшь,{w=0.2} так заставишь ползти медленее."
    lxrd "А там посмортим,{w=0.2} может Вечный стрелять умеет."
    shg "Я тебя услышал."
    window hide
    pause 0.5
    dmn "А мне что делать?"
    lxrd "Старайся глазами найти Вечного."
    dmn "Хорошо."
    play sound fb
    scene int_clubs_male_day_baza
    show sheped
    show deadlylxrd at left
    with flash
    pause 0.5
    play sound pogudeli
    lxrd "Ну, чё тупим?{w=0.6} Всё, погудели." with vpunch
    "И они в темпе вальса начали собираться."
    scene int_clubs_male2_dildo with pushright
    play sound dostal
    show SVD_wovystr_LW0607:
        ypos 0.25
        ease 0.5 ypos 0.05

    "Депеш взял свд в подсобке."
    scene int_clubs_male_day_baza with pushleft
    play sound dostal
    show shstvol1:
        ypos 0.25
        ease 0.5 ypos 0.05

    "Диман крутил в руках свою старую добрую G36."
    window hide
    pause 1
    "А Лорд думал,{w=0.2} как по-быстрому добраться к старому корпусу."
    "В общем,{w=0.2} каждый был занят своим делом."
    stop music fadeout 5
    "Тем временем Вечный..."
    scene black with ed_night_dis
    play sound fb
    play music leilamus fadein 4
    scene ext_old_building_sunset with flash
    window hide
    play sound torsmisnet
    pause 4
    play sound door_open
    scene int_old_building_night with pushleft
    brg "Темно здесь,{w=0.2} однако."
    window hide
    pause 0.5
    "Вечный заметил люк."
    brg "Почему нет?"
    scene int_catacombs
    show strelok at right
    with pushleft
    "Далее от лица Стрелка."
    strlk "Слышишь?"
    bergen1 "Кто-то идёт..."
    play sound door_open
    window hide
    show bergen:
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'bergen'
        parallel:
            xpos -1.0
            linear 0.45 xpos 0.25
    with Pause(0.60)
    show bergen:
        xpos 0.25
    window show
    "В конмату залетает Вечный."
    brg "Эээ..."
    brg "Привет?"
    window hide
    pause 0.5
    strlk "Ну типа привет."
    brg "Я вас где-то уже видел..."
    bergen1 "Да мы тебя тоже."
    brg "И где же?"
    "Вечный начал осмаривать комнату."
    "В его взор попала панель управления."
    "Вечный осмотрел панель."
    "За его движениями внимательно следил Семпай."
    strlk "Ну как это откуда..."
    strlk "Нас Дима Скит разделил." with vpunch
    brg "Чего?" with vpunch
    strlk "Когда вы втроём протаранили забор,{w=0.2} Скит распсиховался и разделил тебя на нас троих."
    strlk "Ещё эта сучара подтёрла тебе память."
    strlk "Ты не ехал никуда с Саней."
    strlk "Хотя он тоже тут есть."
    strlk "Шоп он не подпортил тебе воспоминания,{w=0.2} Скит и ему память подтёр."
    strlk "Мы нашли его в атобусе до тебя."
    strlk "Он прихуел немного,{w=0.2} конечно..."
    strlk "Но мы дали ему чайку со снотворным и уложили спать."
    strlk "Шоп не мешался."
    brg "И где он?"
    bergen1 "Он в{w=0.2}.{w=0.2}.{w=0.2}.{nw}"
    strlk "Об этом позже." with vpunch
    strlk "Скит проебался."
    strlk "В этом бункере есть устройство,{w=0.2} что чисто теоретически должно собрать нас воедино."
    strlk "Но это чисто теоретически."
    strlk "Нас может и на атомы разнести."
    strlk "Улавливаешь суть?"
    brg "И вы двое зассали,{w=0.2} типа?" with vpunch
    brg "Ахаха..."
    strlk "Нет."
    strlk "Нам нужен был ты для объеденения."
    brg "И что мешает сделать это сейчас?"
    strlk "Нам нужен Лорд для более чёткой консультации."
    strlk "Проще говоря,{w=0.2} я в душе не ебу,{w=0.2} чё там нажимать блять."
    strlk "Вот так вот."
    window hide
    pause 0.5
    "В этот момент Вечный заметил одну инетересную кнопку..."
    "Собрать Legion OS."
    "Семпай лишь успел крикнуть..."
    play sound stoimlya
    window hide
    pause 1
    "А Вечный..."
    "Ему что-то подсказывало,{w=0.2} что эту кнопку нужно нажать."
    "Что-то вроде чуйки."
    extend " Называйте как хотите."
    "А в итоге..."
    extend " Вечный не раздумывая нажал её."
    stop music
    play sound vibrosgvna
    scene int_catacombs:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 0.10 pos (0, 0)
            parallel:
                ease 0.10 pos (30,30)
                ease 0.10 pos (0, 0)
                ease 0.10 pos (-25,25)
                repeat

    show tripsMVWWW777:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 0.10 pos (0, 0)
            parallel:
                ease 0.10 pos (30,30)
                ease 0.10 pos (0, 0)
                ease 0.10 pos (-25,25)
                repeat
    with dissolve
    window hide
    pause 4
    strlk "Что случилось-то бляяяя...." with vpunch
    play sound vibrosgvna2
    window hide
    pause 4
    bergen1 "Почти..." with vpunch
    play sound vibrosgvna3
    pause 4
    play sound padenie
    scene int_catacombs
    show dark_LW0607
    show blood_LW0607
    with vpunch
    window hide
    pause 0.6
    play sound coldazvuk
    scene int_catacombs
    show dark_LW0607
    show blood_LW0607
    pause 3.75
    scene black
    window hide
    pause 2
    scene int_catacombs
    play music dumaet
    play sound lesnikstart
    show unblink
    window hide
    pause 9
    th "Бляяя..." with dissolve
    th "Кто здесь?"
    th1 "Молодец,{w=0.2} сука."
    th1 "Теперь мы одно целое."
    th2 "Я никогда не пойму,{w=0.2} чё ж тебе так не нравится?"
    th1 "Да всё пока заебись." with dissolve
    th "А чей это голос был?"
    th1 "Твой."
    stop music fadeout 5
    th2 "Ну,{w=0.2} или кого-то из нас."
    th "Ладно."
    th "Это уже не важно."
    scene black with ed_night_dis
    play sound fb
    scene ext_old_building_night_moonlight
    show deadlylxrd at right
    show sheped at left
    with flash
    play music crysis2 fadein 3
    "Далее от лица Димана." with dissolve
    lxrd "Зомбари близко..."
    lxrd "Мы должны вытащить Вечного до их прибытия..."
    dmn "Времени у нас почти не осталось..."
    shg "Нам остаётся надеяться лишь на то,{w=0.2} что в бункере есть оружие..."
    lxrd "Что там есть хоть кто-то,{w=0.2} кто умеет нормально стрелять..."
    "Они зашли внутрь."
    play sound door_open
    scene int_old_building_night
    show deadlylxrd at right
    show sheped at left
    with pushleft
    dmn "Ты же помнишь,{w=0.2} где тут вход?"
    lxrd "Обижаешь."
    play sound door_open
    scene int_catacombs
    show bergennorm
    show deadlylxrd at right
    show sheped at left
    with pushleft
    "Они ахуели от того,{w=0.2} что увидели."
    "Посреди конматы сидел тип,{w=0.2} который был похож на всех троих."
    lis "Долго же вы."
    "Стрелок,{w=0.2} Вечный и Семпай наконец собрались в одного единого дцпешника."
    "Он сразу решил проверить,{w=0.2} на месте ли его старые кенты?"
    th "Чмошники, {w=0.2}отзовитесь!"
    th1 "Чё надо?"
    th2 "Я тут."
    "Теперь они уж точно одно целое."
    window hide
    pause 0.5
    shg "Интересное имечко ты себе придумал..."
    vchn "Заткнись,{w=0.2} Шепед." with vpunch
    "И Шепед язык в жопе потерял."
    stop music fadeout 5
    window hide
    pause 1
    vchn "А теперь у меня к вам вопрос -"
    extend " где Швилли?" with vpunch
    window hide
    pause 0.5
    play music otec fadein 4
    lxrd "Это мы у тебя должны спросить."
    lxrd "Может,{w=0.2} он в конце шахты?"
    extend " В той части,{w=0.2} что под лагерем?" with vpunch
    shg "Под лагерем?"
    extend " Они там разве есть?"
    lxrd "Конечно."
    extend " Ты лето вообще давно проходил?"
    shg "Никогда."
    lxrd "Понятно."
    vchn "Пошли." with vpunch
    "И они двинули в конец шахты."
    play sound door_break
    scene int_catacombs_hole
    show bergennorm
    show deadlylxrd at right
    show sheped at left
    with pushleft
    shg "Не зря фонарик взял..."
    "Депеш предусмотрительно в подсобке взял фонарь,{w=0.2} который ручной тягой заряжается."
    dmn "Далеко там идти?"
    vchn "Если в оригинале долго ходил,{w=0.2} то и воспоминание будет соответствующее."
    vchn "А я даже в первый раз наугад верно прошел и быстро."
    lxrd "Везёт же некоторым."
    "Они двинули дальше."
    scene int_mine
    show bergennorm
    show deadlylxrd at right
    show sheped at left
    with pushleft
    vchn "Ностальгировать и по баянистым местам ходить будем."
    scene int_mine_halt
    show bergennorm
    show deadlylxrd at right
    show sheped at left
    with pushleft
    vchn "Это святые места."
    vchn "Я даже хз,{w=0.2} что тут и рассказывать..."
    lxrd "Пацанское лето помнишь?"
    scene int_mine_coalface
    show bergennorm
    show deadlylxrd at right
    show sheped at left
    with pushleft
    vchn "А,{w=0.2} ты про то,{w=0.2} как в одном из рутов тут прятали пионерок?"
    lxrd "А ты всё ещё помнишь сюжет..."
    dmn "Ахуеть,{w=0.2} даже я забыл!"
    scene int_mine_crossroad
    show bergennorm
    show deadlylxrd at right
    show sheped at left
    with pushleft
    vchn "Вот она -{w=0.2} та легендарная развилка."
    lxrd "Именно тут начинающие летофаги харкаются и матерятся."
    stop music fadeout 5
    vchn "Да."
    vchn "Но мы пойдём дальше."
    window hide
    pause 0.5
    vchn "Почти пришли."
    play music jamaikamus fadein 2
    scene int_mine_door
    show bergennorm
    show deadlylxrd at right
    show sheped at left
    with pushleft
    vchn "Ну что ж..."
    vchn "За этой дверью, {w=0.2}вероятно,{w=0.2} находится Швилли."
    vchn "А вот живой или мертвый,{w=0.2} уже вопрос интересный."
    lxrd "Заходим?"
    vchn "А ты прямо хочешь?"
    lxrd "Не для того мы сюда пёрлись,{w=0.2} что бы просто тут стоять и втыкать в дверь."
    lxrd "Открывай!" with vpunch
    "И вечный открыл дверь."
    play sound door_break
    scene int_mine_room
    show bergennorm
    show deadlylxrd at right
    show porrigeshv
    show sheped at left
    with pushleft
    pause 1
    vchn "Ты хив!" with vpunch
    extend " Ахуеть..."
    shv "Дэбил,{w=0.2} ты ж меня тут и закрыл."
    th "Кто из вас гандонов это сделал?" with vpunch
    th1 "Ну йобана..."
    th1 "Иначе бы он просто где-то проебался."
    th1 "Нам пришлось..."
    th2 "Тебе." with vpunch
    extend " Не нам."
    th "Ладно.{w=0.2} Забыли."
    lxrd "Там зомбари пойдут на старый лагерь."
    lxrd "Мож тут вылезем?"
    shv "Закрыто, {w=0.2}я пытался."
    dmn "Вечный,{w=0.2} попробуй!" with vpunch
    vchn "Да ебать,{w=0.2} ща пойду и ебалом проломлю эту ссаную решетку,{w=0.2} да?"
    dmn "А мож получится!"
    vchn "Ну ты загадочный..."
    scene int_mine_exit_night_light with pushleft
    "Далее от лица Вечного."
    th "Не, {w=0.2}хуй я тут чё сделаю..."
    "Послышалось копошение сверху."
    vchn "Э БЛЯ!" with vpunch
    extend " Есть кто?"
    "Спустя пару секунд за решеткой нарисовалось знакомое еблище."
    scene int_mine_exit_night_light_ramazan with dissolve
    play sound hellomotherfucker
    window hide
    pause 1
    vchn "Дружище,{w=0.2} откроешь решёточку?"
    rmzn "Я попробую."
    window hide
    pause 0.5
    rmzn "Кстати,{w=0.2} а ты знаешь,{w=0.2} что самсунг уделывает ксяоми?"
    play sound nezn1
    window hide
    pause 2
    rmzn "Знаешь, {w=0.2}какие телефоны круче чем ванплас?"
    play sound nezn2
    window hide
    pause 1
    rmzn "Знаешь, {w=0.2}какие телефоны долго держат батарею?"
    play sound nezn3
    window hide
    pause 1
    rmzn "Знаешь, {w=0.2}какие телефоны самые лучшие?"
    play sound nezn4
    window hide
    pause 4
    play sound ramazanperdun
    pause 11
    play sound padenie
    scene int_mine_room
    show deadlylxrd at right
    show porrigeshv
    show sheped at left
    show dimanspr
    show dark_LW0607
    show blood_LW0607
    with vpunch
    pause 0.6
    play sound ramazansmeh
    pause 4
    lxrd "Беги,{w=0.2} малолетка конченная,{w=0.2} пока он не встал!"
    hide dark_LW0607
    hide blood_LW0607
    with dissolve
    vchn "Сука мразь мелкая..."
    vchn "Найду,{w=0.2} в очко лампочку вкручу..."
    window hide
    pause 1
    lxrd "Ладно,{w=0.2} двинули?"
    vchn "Малолетка не даст открыть решетку,{w=0.2} даже если Шепед натянет свой противогаз."
    vchn "Так что нам идти обратно только если."
    dmn "Мляяя...."
    dmn "Там зомбари как раз уже должны были подоспеть..."
    vchn "Ну, {w=0.2}пиздец."
    vchn "А что делать?"
    window hide
    pause 1
    "И они двинули назад."
    "Далее от лица Димана."
    stop music
    $ renpy.movie_cutscene("source/videosos/afewmomentslater.webm")
    play music mdknmus fadein 3.5
    scene int_catacombs
    show bergennorm
    show deadlylxrd at right
    show sheped at left
    show porrigeshv
    with dissolve
    lxrd "Вы слышали?"
    hide bergennorm
    hide deadlylxrd at right
    hide sheped at left
    hide porrigeshv
    with dissolve
    play ambience zattack
    dmn "Смотри!"
    window hide
    show slzombar:
        subpixel True default
        parallel:
            Null(233.0, 720.0)
            'slzombar'
        parallel:
            xpos -1.0
            linear 0.35 xpos 0.2
    with Pause(0.60)
    show slzombar:
        xpos 0.2
    window show

    "Первый зомбарь был уже очень близко."
    "Но,{w=0.2} Диман не растерялся и начал шмалять."
    play sound dostal
    show shstvol1:
        ypos 0.25
        ease 0.5 ypos 0.05

    $ _window_hide(dissolve)

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11

    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1
    hide slzombar
    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    hide slzombar
    hide shstvol1
    stop ambience
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show shstvol1
    play sound padenie
    pause 1
    lxrd "Красава,{w=0.2} Димас."
    extend " А говорил, {w=0.2}что стрелять не умеешь."
    dmn "Теперь умею."
    hide shstvol1
    play sound ubralstvol
    show shstvol1:
        ypos 0.0
        ease 0.5 ypos 0.5

    pause 0.6
    hide shstvol1
    "Димас опустил ствол."
    play sound volinichehlit
    lxrd "Рано волыны чехлить,{w=0.2} пацаны!"
    show bergennorm with dissolve
    vchn "Выходим?"
    dmn "Пошли."
    window hide
    pause 0.5
    vchn "Хотя подожди."
    vchn "Депеш,{w=0.2} ты,{w=0.2} наверное,{w=0.2} дай Саньку СВД."
    shv "Всё лучше -{w=0.2} чем ничего."
    stop music fadeout 5
    "Шепед отдал СВД Швилли."
    window hide
    pause 0.5
    "Далее от лица Вечного."
    hide bergennorm with dissolve
    play music nerocrackmus fadein 5
    play sound razebal
    window hide
    pause 1.5
    show rmznspr1 with vpunch
    pause 1
    play sound obana
    pause 0.7
    play sound xanatebe
    vchn "Хана тебе,{w=0.2} дядя!"
    lxrd "Ща у малелотки ебало битое будет,{w=0.2} чекайте инфо!"
    hide rmznspr1
    hide blink
    show hernya_kakaya_toMVWWW777 with flash
    play music nerocrackmus1
    show rmznspr:
        zoom 3.0
        ypos 0.0
        xpos 0.05
        pause (0.38)
        linear 0.09 ypos -0.07
        linear 0.09 ypos 0.0
        pause (0.19)
        repeat

    show dlya_ebalaMVWWW777:
        xpos 1.0
        ypos 1.0
        linear 0.20 xpos -0.0 ypos -0.0
        pause (0.40)
        linear 0.15 xpos 1.0 ypos 1.0
        pause (1.0)
        repeat





    show dlya_ebalaleftMVWWW777:
        xpos -1.0
        ypos 0.5
        pause (1.0)
        linear 0.20 xpos -0.0 ypos -0.0
        pause (0.40)
        linear 0.15 xpos -1.0 ypos 0.5

        repeat



    $ renpy.pause (0.39)


    window show
    vchn "Смешно тебе, сука!?" with vpunch
    vchn "Пердун сука!" with vpunch
    rmzn "Ай прастите больше не буду!!!" with vpunch
    vchn "Сначала я тебе ебало начищу!!" with vpunch

    window hide
    pause 1
    hide hernya_kakaya_toMVWWW777 with dissolve
    hide dlya_ebalaMVWWW777
    hide dlya_ebalaleftMVWWW777
    hide rmznspr
    with dissolve
    stop sound
    "Вечный делает финальный хук в ебло толстой малолетней гниды."
    window hide
    show rmznspr with dissolve:
        xpos 0.05 ypos -0.27 zoom 3.0
        pause (0.38)
        linear 0.19 ypos -0.32
        linear 0.19 ypos -0.23
        linear 0.19 ypos -0.20
        linear 0.19 ypos -0.27
        pause (0.19)

    show dlya_ebalaMVWWW777:
        xpos 1.0
        ypos 1.0
        linear 0.20 xpos -0.0 ypos -0.0
        pause (0.50)
        linear 0.15 xpos 1.0 ypos 1.0

    play sound udarMVWWW777
    $ renpy.pause (0.5)
    hide hernya_kakaya_toMVWWW777 with dissolve
    show rmznspr with dissolve:
        xpos 0.05 ypos -0.27 zoom 3.0
        pause (0.2)
        linear 1.0 ypos 1.5
    play sound padenie
    pause 1
    play sound fatalitysound
    pause 2
    window show
    stop music fadeout 5
    vchn "И так будет с каждой конченной малолеткой блеать!" with vpunch
    window hide
    pause 1
    vchn "Кароче блеать."
    vchn "Предлагаю такой расклад:"
    play music theorem fadein 2
    extend " наверх идём мы с Швилли и Рамазанчиком." with vpunch
    rmzn "Нииеееттт!!!" with vpunch
    rmzn "Позязя нинада!!!" with vpunch
    vchn "Ты у меня сука первым на корм зомбарям пойдешь..." with vpunch
    "Вечный пнул Рамазанчика."
    rmzn "Ай,{w=0.2} бля!!!" with vpunch
    window hide
    pause 0.5
    play sound voprosiizzala
    pause 2
    stop music fadeout 4
    rmzn "Я протестую,{w=0.2} сукаааа{w=0.2}а{w=0.2}а{nw}"
    vchn "Раз ни у кого вопросов нет,{w=0.2} мы выдвигаемся!"
    "И они втроем вылезли наверх."
    play sound door_open
    $ say_pizdec = True
    play music redcatgandon fadein 3
    scene burnint
    with pushleft
    vchn "Какого хера тут всё горит?"
    rmzn "Я бежал сюда...{w=0.3} Плакал,{w=0.2} просто рыдал как сучка..."
    rmzn "И поджог за собой дверь." with vpunch
    vchn "Ты ебанутый?"
    rmzn "Ну,{w=0.2} они же в огонь не полезут,{w=0.2} да?"
    "Далее от лица Швилли."
    play ambience zattack
    shv "Смотри!"
    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1
    with dissolve

    vchn "Саня, {w=0.2}у тебя же есть СВД!" with vpunch
    window hide
    play sound valiskatinu
    pause 2
    shv "Приступаю!" with vpunch


    $ _window_hide(dissolve)


    play sound dostal
    show SVD_wovystr_LW0607:
        ypos 0.25
        ease 0.5 ypos 0.05

    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1
    with dissolve

    $ renpy.pause (2, hard=True)

    $ _window_show(dissolve)
    rmzn "О нет,{w=0.2} меня тут сожрут ща!" with vpunch
    "Саня не спешил стрелять."
    window hide
    pause 0.5
    "И в итоге гниль сожрала Рамазанчика уебанчика."
    $ _window_hide(dissolve)
    hide rmznspr1
    play sound gamaz
    show rmznspr1:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.7 ypos 2.0
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.7 ypos 2.0
    pause 1
    stop sound
    $ _window_show(dissolve)
    "Вот так и погибают чмошники."
    window hide
    pause 0.5
    "О чём это я?"
    "Ах,{w=0.2} да..."
    scene burnint
    show SVD_wovystr_LW0607
    play sound zattack
    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1
    vchn "Гаси их,{w=0.2} ну!"
    "И Швилли открыл огонь."
    $ _window_hide(dissolve)

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607

    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    hide slzombar
    hide SVD_wovystr_LW0607
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show SVD_wovystr_LW0607
    play sound padenie
    pause 1
    hide slzombar
    shv "Один готов!"
    vchn "Продолжай!"
    "У Вечного не было ствола,{w=0.2} шоп пострелять."
    "Вот так вот."

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45
    hide sl_zombie_sprite3_LW0607
    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    hide slzombar
    hide SVD_wovystr_LW0607
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show SVD_wovystr_LW0607
    play sound padenie
    pause 1
    hide slzombar
    shv "Второй готов!"
    vchn "Продолжай!"

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45
    hide sl_zombie_sprite4_LW0607
    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center


    hide slzombar
    hide SVD_wovystr_LW0607
    stop ambience
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show SVD_wovystr_LW0607
    play sound padenie
    pause 1
    hide slzombar
    $ renpy.pause (1)

    $ _window_show(dissolve)
    shv "Поcледний готов!"
    vchn "Красава!"
    window hide
    pause 0.4
    vchn "Валим отсюда!" with vpunch
    "Они вышли наружу,{w=0.2} удачно миновав огонь."
    scene roofburn
    show SVD_wovystr_LW0607
    with pushleft
    "Швилли решил перезарядить СВД."
    hide SVD_wovystr_LW0607
    play sound clipin
    show SVD_wovystr_LW0607:
        ypos 0.0
        ease 0.5 ypos 0.5

    pause 1
    hide SVD_svystrel_LW0607
    play sound clipout
    show SVD_wovystr_LW0607:
        ypos 0.5
        ease 0.5 ypos 0.05

    pause 1
    "Швилли перезарядил СВД."
    window hide
    pause 0.5
    "Вечный решил прервать молчание после того,{w=0.2} как кому-то отписался в телефоне."
    window hide
    show bergennorm:
        subpixel True xpos 0.25 default
        parallel:
            Null(508.0, 733.0)
            'bergennorm'
        parallel:
            xpos 0.25 ypos 2.0
            linear 0.40 xpos 0.25 ypos 1.0
    with Pause(0.60)
    show bergennorm:
        pos (0.25, 1.0)
    window show
    vchn "Я написал,{w=0.2} чтоб они выходили."
    vchn "Лорд сказал,{w=0.2} что выведет группу другим путём."
    shv "Как?{w=0.2} Шахта закрыта же."
    vchn "Он сказал,{w=0.2} что когда я Рамазанчика хуярил,{w=0.2} с него ключ от решетки выпал."
    vchn "С пидорка этого."
    shv "Хех."
    stop music fadeout 4
    vchn "У тебя есть варианты,{w=0.2} как свалить?"
    vchn "Просто они уже ушли своей тайной тропой с этого богом забытого места."
    window hide
    pause 0.5
    play music soldatmusssic fadein 2
    hide SVD_wovystr_LW0607
    play sound ubralstvol
    show SVD_wovystr_LW0607:
        ypos 0.0
        ease 0.5 ypos 0.5

    pause 0.6
    hide SVD_wovystr_LW0607
    shv "Пока ты хуярил этого додика,{w=0.2} я кое-кому написал..."
    shv "И этот человек сейчас на машине ждёт нас у ворот лагеря."
    window hide
    pause 0.5
    vchn "Я походу понял,{w=0.2} про кого ты говоришь."
    shv "Так вот нам бы ускориться..."
    window hide
    pause 0.5
    shv "Ибо на территории лагеря сейчас небось полно зомбарей..."
    window hide
    pause 0.5
    shv "Да и заждался он."
    window hide
    pause 0.5
    vchn "Ну,{w=0.2} как в старые добрые,{w=0.2} на перегонки?"
    hide bergennorm with flash
    "Не дав ответить Швилли,{w=0.2} Вечный рванул вперёд."
    shv "Всё равно догоню,{w=0.2} ска!" with vpunch
    "И швилли тоже рванул."
    play sound begtrava
    $ say_pizdec = False
    scene roofburn at ed_running_fast
    scene ext_path_night at ed_running_fast
    with pushleft
    window hide
    pause 2
    scene ext_playground_night at ed_running_fast
    with pushleft
    window hide
    pause 2
    scene ext_square_night at ed_running_fast
    with pushleft
    window hide
    pause 2
    scene ext_clubs_night at ed_running_fast
    with pushleft
    window hide
    pause 2
    scene ext_bus_night at ed_running_fast
    with pushleft
    window hide
    pause 2
    stop sound fadeout 2
    scene goscar
    show dark_LW0607
    with pushleft
    play sound ustal
    "Швилли задыхался, {w=0.2}но был первым."
    shv "Привет...{w=0.2} Илюш..."
    galenin "Здарова,{w=0.2} заебал."
    "Швилли пытался отдышаться."
    window hide
    stop sound fadeout 3
    pause 0.5
    "Вскоре прибежал и Вечный."
    window hide
    show bergennorm:
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'bergennorm'
        parallel:
            xpos -1.0
            linear 0.45 xpos 0.15
    with Pause(0.60)
    show bergennorm:
        xpos 0.15
    window show
    play sound ustal
    vchn "И куда ж ты...{w=0.3} Такой быстрый...{w=0.3} А?"
    vchn "Привет,{w=0.2} Илюш..."
    galenin "Тебе тоже привет."
    window hide
    stop sound fadeout 3
    pause 0.5
    shv "Да я просто всё это время не парил."
    shv "Зарядку экономил для этого случая."
    window hide
    pause 0.5
    "Швилли уже отдышался и поэтому мог позволить себе тягу на поде."
    window hide
    play sound podik
    pause 2
    shv "Заебись."
    "Вечный парить не захотел."
    window hide
    pause 0.5
    galenin "Поехали?"
    vchn "Точно что..."
    window hide
    pause 0.5
    shv "Я тебе ща такую историю расскажу,{w=0.2} ты не поверишь..."
    window hide
    pause 0.5
    galenin "Смотря что за история."
    window hide
    stop music fadeout 5
    pause 1
    "И они прыгнули в тачку Ильяса и укатили в надвигающийся рассвет."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Неони:")
    hide zatemnenie with dissolve2
    scene ext_road_night
    show coldspr1
    with ed_night_dis
    play music grock
    cld "Вот такая вот история."
    nn "Нихуёво."
    "Неоня заметил,{w=0.2} что они идут уж слишком долго."
    "Он оглянулся и увидел в 5 метрах от себя лагерь."
    cld "Да ёбаный насос!"
    cld "Надо было взять координаты у Ильяса."
    cld "Без них мы отсюда не уйдём."
    nn "Чё делать-то блять?"
    cld "Не паникуй."
    "И они начали звать на помощь через рацию,{w=0.2} найденную в пупке у Колда."
    show zatemnenie with dissolve2
    $ MND_Chapter("Тем временем пацаны:")
    hide zatemnenie with dissolve2
    play sound fb
    scene black with flash
    scene ext_road_night at ed_bus_move
    show volga at ed_bus_move
    with ed_night_dis
    galenin "Бля чуваки."
    galenin "Чёта рация шипит."
    "Из рации наконец начала доноситься нормальная речь блять."
    play sound cold_help
    window hide
    pause 24
    galenin "А я ведь предупреждал..."
    shv "Кто там?"
    galenin "Колд."
    window hide
    play sound neony_help
    pause 5
    galenin "Ловите схему, заебали."
    window hide
    play sound cold_vibralis
    pause 19
    galenin "Вас забирать?"
    galenin "Я ща недалеко."
    cld "Было б неплохо."
    galenin "Ща заедем."
    cld "Конец связи."
    stop music fadeout 5
    galenin "Мостись,{w=0.2} Вечный!" with vpunch
    galenin "Там твои братки скоро сядут."
    scene black with ed_night_dis
    play music hott fadein 3
    scene buhaem
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with ed_night_dis
    nvl clear
    nvlbazar "Вот так они всей бригадой выбрались из ловушки Скита."
    nvlbazar "И поехали на тачке Ильяса бухать в Курск."
    nvl clear
    nvlbazar "Диман и Депеш ушли в скайнет."
    nvlbazar "Диман обещал научить его играть в CS GO."
    nvl clear
    nvlbazar "Ильяс и Саня Швилли поехали развлекаться к тёлкам в Искру."
    nvlbazar "Надо же как-то снять напряжение после такого-то дерьма."
    nvl clear
    nvlbazar "Ну а Вадимка,{w=0.2} Колд, {w=0.2}Неоня и Вечный поехали на хату Вечного,{w=0.2} дабы испить священный нектар..."
    nvlbazar "Под названием лысая головка."
    nvlbazar "Это нечто вроде самопального Revo."
    nvlbazar "Алкогольный энергетик."
    nvl clear
    nvlbazar "Мешаем пиво и ягуар желтый или любой другой."
    nvlbazar "Самый чёткий на моей памяти был белый медведь и красный драйв."
    nvlbazar "Меня тогда развезло и я полетел исполнять солнышко на качели."
    nvl clear
    nvlbazar "Не о том разговор."
    nvl clear
    nvlbazar "Неоня нахуярился и уснул."
    nvlbazar "Вечный и Колд начали исполнять караоке,{w=0.2} Вадимка куда-то ушёл."
    nvl clear
    stop music fadeout 3
    play sound fb
    scene coldbuhaet with flash
    cld "Ну,{w=0.2} давай ГрОб споём шоль?"
    vchn "А хуле нет!" with vpunch
    show zatemnenie with dissolve2
    $ MND_Chapter("Тем временем Вадимка:")
    hide zatemnenie with dissolve2
    play sound fb
    scene vannaya with flash
    lxrd "Не срёться нихуя{w=0.2}.{w=0.2}.{w=0.2}."
    lxrd "Ну и ладно."
    lxrd "Пора бы и тоже в караоке спеть."
    "Вадимка начал слезать с параши."
    show zatemnenie with dissolve2
    $ MND_Chapter("Тем временем Пацаны:")
    hide zatemnenie with dissolve2
    play sound fb
    scene coldbuhaet with flash
    window hide
    play sound grobtopcover
    pause 31
    stop sound
    scene morozovcover with vpunch
    lxrd "Сорян,{w=0.2} посоны."
    lxrd "Это я выключил гроб{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    lxrd "Пришло моё время исполнять."
    lxrd "Этот кавер посвещаятся моей бывшей."
    lxrd "Кхм." with vpunch
    window hide
    play sound otrignul
    pause 3
    "Вадимка пару раз рыгнул в микрофон,{w=0.2} тем самым его проверив."
    lxrd "Погнали,{w=0.2} хули." with vpunch
    window hide
    play sound face
    pause 30
    stop sound fadeout 5
    "Вадимка закончил свой кавер."
    vchn "Это было великолепно."
    cld "Ты не мог раньше заткнуться?" with vpunch
    cld "У меня из ушей малафья полилася."
    cld "Пиздец." with vpunch
    play sound zarevu
    window hide
    pause 3
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    nvl clear
    nvlbazar "Вот так они и отдыхали."
    nvlbazar "Разрисовали ебало неони зубной пастой."
    nvlbazar "Или это был cum?{nw}"
    nvl clear
    nvlbazar "Впрочем,{w=0.2} не важно."
    nvlbazar "Вот так и заканчивается этот эпизод этой одной большой и длинной истории."
    nvlbazar "Вот так вот."
    nvl clear
    nvlbazar "Будьте хорошими малолетками и не срите на парты в школе."
    nvl clear
    show zatemnenie with dissolve2
    $ MND_Chapter("Конец второго картера...")
    scene black with ed_night_dis
    jump carter3