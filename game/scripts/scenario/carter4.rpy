label carter4:
    $ pps = 14
    play music living fadein 5
    scene domintnight
    with ed_night_dis
    show zatemnenie with dissolve2
    $ MND_Chapter("The Carter Four:")
    $ MND_Chapter("Rotten Diary")
    hide zatemnenie with dissolve2
    nvlbazar "Я сидел и просто харкал в потолок,{w=0.2} ожидая,{w=0.2} что харча начнёт падать вниз -{w} мне в кармашек."
    nvlbazar "Просто делать было больше нечего."
    nvlbazar "И тут мне на мобилу приходит сообщение в тг."
    nvl clear
    nvlcld "Жду тебя снаружи.{w} Надо встретиться."
    nvl clear
    nvlbazar "На дворе была уже ночь."
    nvlbazar "Скит и Василиса уже легли спать."
    nvlbazar "Один я,{w=0.2} долбоёб,{w=0.2} хуйнёй маялся."
    nvlbazar "Делать было нечего."
    nvlbazar "Пришлось выходить."
    nvl clear
    play sound door_open
    scene nightdvor
    show coldsprnight
    with ed_lap
    vchn "Здарова.{w} Ну так чё там у тебя?"
    cld "Как продвигается наша миссия?" with vpunch
    vchn "Пока всё идёт по плану."
    vchn "Скит ещё не подозревает, в какой он заднице." with vpunch
    cld "Это хорошо,{w=0.2} бро."
    cld "Но меня терзают смутные сомнения насчёт этой Василисы." with vpunch
    vchn "Она же вроде клон,{w=0.2} что сделал Казах,{w=0.2} не?"
    cld "Это понятно."
    cld "Я про её истинно-{w=0.2}арийское происхождение."
    cld "Никто не знает,{w=0.2} кто она и откуда." with vpunch
    vchn "Да я всё понимаю,{w=0.2} братиш."
    vchn "Просто загвоздка вот в чём -{w} она ничего не помнит об оригинале."
    cld "Это она тебе так сказала?" with vpunch
    "И тут Вечный понял, что он редкосный идиот."
    cld "И у тебя не закралось сомнений по поводу ровности её базара?"
    vchn "Теперь закрались."
    vchn "Но в лоб спрашивать бесполезно,{w=0.2} братиш,{w=0.2} сам же знаешь."
    cld "Тут ты прав."
    cld "Но у меня и на этот счёт есть идея."
    cld "Она может и не рассказывала,{w=0.2} но могла записать." with vpunch
    vchn "Мобилы у неё нет."
    vchn "Это я бы точно заметил."
    cld "Необязательно на мобиле."
    cld "Мб нашла дома у скита ежедневник и начала выплёскивать туда все свои переживания."
    cld "Пока меня ебашил Скит,{w=0.2} сука."
    vchn "А ведь ты прав."
    vchn "И чё я раньше об этом не подумал?"
    cld "Меня тот же вопрос мучает."
    vchn "Как тело твоё кста?" with vpunch
    cld "Этот сосунок не смог дамага нанести толком."
    cld "Петушара в тягу ебашил и по нервам."
    cld "Боль была жесткая."
    cld "Я притворился мёртвым,{w=0.2} лишь бы лысая успокоилась." with vpunch
    cld "И нахуя ты мне сказал один патрон взять?"
    vchn "Ты бы ему просто башку отстрелил."
    vchn "Ограничимся одним клоном Ракуна пока."
    cld "Сука,{w=0.2} ты ответишь за эту потасовку." with vpunch
    cld "Мог бы и помочь."
    vchn "Я бы точно спалился перед Димочкой."
    vchn "Очевидно же."
    vchn "Я,{w=0.2} конечно,{w=0.2} догадывался,{w=0.2} что Скитовского научили драться на районе,{w=0.2} но чтоб так..."
    vchn "Он же лохом ебаным кажется со стороны."
    vchn "Это ослажняет нашу задачу,{w=0.2} братиш." with vpunch
    cld "Да кто ж спорит."
    cld "Осталось надеяться,{w=0.2} что Казах и Вадимка придут и отомстят за меня."
    cld "Они по-{w=0.2}любому по камерам мою {b}<<смерть>>{/b} видели."
    cld "Тебе пока не стоит попадаться им на глаза."
    cld "Как только нароешь инфы про эту {b}<<Василису>>{/b},{w=0.2} делай ноги оттуда."
    cld "Как можно быстрее."
    cld "Почуят неладное -{w} нам обоим пизда." with vpunch
    cld "С обоих фронтов,{w=0.2} бро."
    cld "Шутки закончились." with vpunch
    cld "Пора делать реальные дела."
    vchn "Я тебя услышал."
    vchn "Ещё раз сорян за Лысую."
    vchn "Я рили такого говна не ждал."
    cld "Удачи."
    play sound door_open
    scene domintnight with ed_lap
    "И они разошлись."
    "Вечный пошёл домой к Скиту -{w} рыть инфу о Василисе."
    "Пошарив по столу,{w=0.2} за газетами он нашёл нечто одалённо напиманающее дневник."
    window hide
    play sound dostal
    show diary:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'diary'
        parallel:
            ypos 2.0
            linear 0.50 ypos 1.0
    with Pause(0.60)
    show diary:
        ypos 1.0
    vchn "Походу,{w=0.2} это он и есть."
    vchn "Тот самый дневник Василисы."
    hide diary
    play sound ubralstvol
    show diary:
        ypos 0.0
        ease 0.5 ypos 1.5

    pause 0.6
    hide diary
    "Открыв его,{w=0.2} он увидел на первой странице единственную надпись большим шрифтом."
    show zatemnenie with dissolve2
    $ MND_Chapter("Слушай сюда, дорогой мой.")
    $ MND_Chapter("Пока не поздно, положи его на место.")
    $ MND_Chapter("Иначе сделаю с тобой то,")
    $ MND_Chapter("Что не успела тогда в туалете.")
    hide zatemnenie with dissolve2
    stop music fadeout 5
    vchn "Это Скиту адресовано чтоль?"
    vchn "Лично я провалами в памяти не страдаю."
    vchn "Такое бы точно не забыл."
    vchn "Ха.{w} Надо будет у Скита спросить потом,{w=0.2} хы." with vpunch
    play music saveme
    nvl clear
    nvlvas "Дорогой дневник и бла-{w=0.2}бла-{w=0.2}бла."
    nvl clear
    nvlvas "Я не могу больше молчать."
    nvlvas "Рассказат Скитецкому всю правду ={w} убить себя."
    nvlvas "Закопать глубже некуда."
    nvlvas "Вечному тоже не стоит."
    nvlvas "Он меня возненавидит."
    nvl clear
    nvlvhcn "Какое интригующее начало..."
    nvl clear
    nvlvas "Я всё прекрасно помню."
    nvlvas "Это буквально мешает мне жить."
    nvlvas "Я сделана из натуральной психопатки."
    nvlvas "Не зря Неоня её прикопал на пустыре."
    nvl clear
    nvlvas "С самого детства были проблемы с социализацией."
    nvlvas "Меня не просто считали странной..."
    nvlvas "Буквально издевались."
    nvl clear
    nvlvas "Ещё в школе...{w} Всегда была изгоем..."
    nvlvas "Однако апогеем всей этой истории стал переломный момент в детском лагере {b}<<Совёнок>>{/b}."
    nvl clear
    nvlvhcn "Бля а не тот ли это лагерь,{w=0.2} в который нас отправил Дима Скит с пацанвой?"
    nvlvhcn "История приобретает новые обороты..."
    nvlvhcn "Если всё действительно так связано..."
    nvl clear
    stop music fadeout 3
    vchn "В пизду." with vpunch
    vchn "Не хочу об этом думать."
    play music prxjek
    "Вечный захлопнул дневник и убрал на место."
    vchn "Я силишком трезвый для этого дерьма." with vpunch
    vchn "Надо пойти проветриться."
    vchn "Не могу я эту чушь на горячую голову читать."
    "Вечный проверил счёт в {b}<<сбербанк онлайн>>{/b} и увидел там пару соток."
    vchn "На малыша не хватит...{w} Придётся брать коктейльчики..."
    play sound door_open
    scene nightdvor with ed_lap
    "Он накинул свою любимую чёрную рубашку и,{w=0.2} взяв {b}<<Brusko Minican Plus>>{/b},{w=0.2} отправился на улицу."
    "Ночной Новошахтинск опьяняюще действовал на разум Вечного."
    "Он сделал глубокую тягу на {b}<<миникане>>{/b} с жижкой {b}<<Brusko Таёжный Морс 50мг>>{/b} и начал релаксировать."
    "Прохладный весенний ветер снимал нарастающее напряжение."
    scene nvnight with ed_lap
    vchn "Подумать только... {w}Если всё реально {b}НАСТОЛЬКО{/b} связано..."
    vchn "Это же пиздос..." with vpunch
    vchn "Скит не так прост,{w=0.2} каким кажется."
    vchn "И это очень парашно по отношению к нашему плану."
    vchn "Если всё пойдёт по пизде..."
    "Вечный решил не думать о всём этом говне,{w=0.2} после чего зашел в шарашку и,{w=0.2} взяв там три шота {b}<<аналога лысого малыша>>{/b},{w=0.2} отправился обратно."
    scene nightdvor with ed_lap
    "По пути он опрокинул в себя один из лимонных шотов."
    "Вернулся обратно он достаточно быстро,{w=0.2} ведь ночь-{w=0.2}то не резиновая."
    play sound door_open
    scene domintnight
    show vasilisanight
    with ed_lap
    "Когда он зашёл в хату,{w=0.2} его встретила Василиса."
    vas "Ну и куда это мы уходим в два часа ночи?" with vpunch
    vas "А?" with vpunch
    vas "К тёлкам своим небось бегаешь?" with vpunch
    "Вечный немного сильно так прихуел с резкого приступа {b}<<женской логики>>{/b}."
    vchn "Я ходил..."
    vchn "За бухлом." with vpunch
    vas "Тебе настолько херово,{w=0.2} что ты начал пить?" with vpunch
    "Василиса прониклась жалостью к нему."
    "В то же время Вечный тихо угорал внутри своего разума с этого {b}<<тувинского цирка>>{/b}."
    "Василиса нежно обняла Вечного."
    vas "Бедный мой..."
    vas "Погоди." with vpunch
    vas "У тебя ещё осталось бухло?"
    "Вечный сразу всё понял."
    "Не стал отнекиваться.{w} В соло бухать ему никогда не нравилось."
    "В такие моменты начинает {b}<<свистеть фляга>>{/b}."
    "Поэтому он отдал третий шот Василисе."
    "У него остался второй шот."
    hide vasilisanight
    window hide
    show vasilisanight:
        subpixel True default
        parallel:
            Null(640.0, 640.0)
            'vasilisanight'
        parallel:
            xpos 0.5
            linear 1.00 xpos -0.3
            linear 1.00 xpos 1.3
            linear 1.00 xpos 0.5
            repeat
    window show
    vas "Ур{w=0.2}-а{w=0.2}-а{w=0.2}-а!" with vpunch
    vas "Пойдём буха{w=0.2}-а{w=0.2}-а{w=0.2}-ать!" with vpunch
    "Кружилась вокруг него Василиса."
    "Вечный почти словил вертолёты."
    hide vasilisanight
    window hide
    show vasilisanight:
        subpixel True default
        parallel:
            Null(640.0, 640.0)
            'vasilisanight'
        parallel:
            xpos -0.3
            linear 0.39 xpos 0.5
    with Pause(0.60)
    show vasilisanight:
        xpos 0.5
    window show
    vchn "УСПОКОЙСЯ,{w=0.2} БЛЯДЬ!" with vpunch
    "Почти криком осадил её Вечный."
    vas "Ну ладно.{w} Чё бухтеть-{w=0.2}то..."
    play sound door_open
    scene kuhnyanight
    show vasilisanight
    with ed_lap
    "После пары секунд затупа они пошли на кухню."
    "Думать об этом было поздно,{w=0.2} но всё же..."
    "Не разбудили ли они Скитецкого?"
    "Вечному уже влом было бы идти в шарашку за четвёртым шотом."
    "Да и бабки кончились. {w}Капитально."
    vchn "Ну и мусорка сука." with vpunch
    "И тут Василиса мастерски пародирует один малоизвестный пёрл."
    window hide
    play sound ozon
    pause 5
    vchn "Хы."
    stop music fadeout 5
    "Эта фраза отдалась эхом в голове Вечного."
    "Причем именно оригинал."
    "Голосом Озона."
    "Ну а потом они начали опрокидывать оставшиеся шоты."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Димы:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    scene domint with ed_night_dis
    play music mnd_gluhar_utro
    "Дело было 18 июня."
    "За окном шёл дождь."
    "Дима лежал и пердел у себя на диване дома в Новошахтинске."
    "Ковяряясь в носу,{w=0.2} он думал о вечном."
    "Как он в детстве металолом пиздил со склада..."
    "Как он в первый раз засадил свой {b}dick{/b} одной прекрасной девочке..."
    "Он уже и не помнит,{w=0.2} насколько давно это было."
    "Ведь после того раза ему больше не перепадало."
    "По-{w=0.2}началу он держался молодцом и тестировал прошивки,{w=0.2} работал на складе..."
    "Потом его это заебало и он ушел со склада работать на фабрику и начал оскать школьников в телеграме."
    "Он извергал столько желчи,{w=0.2} сколько нельзя увидеть в реальности."
    "Это всё вам для понимания того,{w=0.2} насколько Скит едкая сука."
    "А ведь по-{w=0.2}началу всё было хорошо..."
    "Но он сам выбрал свой путь."
    "Многолетка ебучая." with vpunch
    stop music fadeout 3
    "Скит думал,{w=0.2} что ничего не могло испортить этот день."
    "И он ошибался."
    play sound door_zvonok
    play music madelina fadein 2
    skt "Да сука{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    skt "Я же никого сегодня не жду{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Странно всё это{w=0.2}.{w=0.2}.{w=0.2}."
    "И Скит поплёлся открывать дверь."
    "Он только подошёл к двери,{w=0.2} как вдруг..."
    play music madelina1
    play sound door_break
    scene padik
    show morozko
    mrz "С НОВЫМ ГОДОМ,{w=0.2} СУКА!" with vpunch
    window hide
    show dlya_ebalaMVWWW777:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'dlya_ebalaMVWWW777'
        parallel:
            pos (1.0, 1.5)
            linear 0.20 pos (0.5, 1.0)
    with Pause(0.30)
    show dlya_ebalaMVWWW777:
        pos (0.5, 1.0)
    play sound sfx_punch_washstand
    hide dlya_ebalaMVWWW777
    show dlya_ebalaMVWWW777:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'dlya_ebalaMVWWW777'
        parallel:
            pos (0.5, 1.0)
            linear 0.20 pos (1.0, 1.6)
    with Pause(0.30)
    show dlya_ebalaMVWWW777:
        pos (1.0, 1.6)
    hide morozko
    show morozko:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    play sound sfx_body_bump
    "Скит ударом уложил это {b}<<чудо>>{/b} и пытался побежать вниз."
    window hide
    hide morozko
    show lordsprclon4 at center:
        xcenter -0.4 ycenter 0.5 rotate 0
        easein 0.4 xcenter 0.5 rotate 360
        ease 0.05 zoom 1.3
        ease 0.05 zoom 1.0
        ease 0.1 rotate -360
    $ renpy.pause (0.5)
    window show
    hide lordsprclon4
    show lordsprclon4
    "Но с лестницы сверху вышел... {w}Прошу прощения.{w} На лестничную клетку,{w=0.2} ебанув тройное сальто,{w=0.2} завалился новый клон Вадима Морозова."
    lxrd1 "ТЕБЕ ПИЗДЕЦ!" with vpunch
    "Скит не растерялся и въебал в дыхло новому клону."
    window hide
    show dlya_ebalaMVWWW777:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'dlya_ebalaMVWWW777'
        parallel:
            pos (1.0, 1.5)
            linear 0.20 pos (0.5, 1.0)
    with Pause(0.30)
    show dlya_ebalaMVWWW777:
        pos (0.5, 1.0)
    play sound sfx_punch_washstand
    hide dlya_ebalaMVWWW777
    show dlya_ebalaMVWWW777:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'dlya_ebalaMVWWW777'
        parallel:
            pos (0.5, 1.0)
            linear 0.20 pos (1.0, 1.6)
    with Pause(0.30)
    show dlya_ebalaMVWWW777:
        pos (1.0, 1.6)
    hide lordsprclon4
    show lordsprclon4:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    play sound sfx_body_bump
    play sound2 vozduh
    "Выдался отличный момент съебаться,{w=0.2} чем Дима и воспользовался."
    "Он с разбегу рванул по лестнице вниз."
    play sound door_break
    play ambience rain_out fadein 2
    scene domext at ed_running_fast
    show doshd
    with vpunch
    skt "Где там моя родная десяточка..."
    play sound tazik1
    play ambience rain_in
    scene traphata
    show doshd
    with vpunch
    skt "Осталось завести."
    window hide
    stop ambience fadeout 3
    play sound vaz
    pause 5
    play sound bochka
    with vpunch
    pause 4
    window hide
    play sound vaz
    pause 3
    stop sound
    play ambience dviglo
    window hide
    scene traphata at ed_bus_move
    show doshd
    with vpunch
    play sound attack_1
    pause 2
    "И Скит поехал подальше от этого места."
    scene nmall at ed_bus_move
    show doshd
    with ed_lap
    "Дмитрий гнал под 120 по Новошохтинску на своём некро-{w=0.2}ведре."
    "Из хрипящих динамиков доносился до ушей старый добрый русский транс."
    "Движок десятки пердел,{w=0.2} хрипел,{w=0.2} умирал,{w=0.2} но,{w=0.2} сука,{w=0.2} работал."
    "Самое главное -{w=0.2} что ехал."
    "Иначе Димка бы познал кару Морозки."
    "И тогда бы ему было пиздец как грустно."
    window hide
    pause 1
    "Куда он едет?"
    play sound herznaet
    window hide
    pause 1.6
    "Димка повернул в сторону хаты своей бывшей."
    "Как говориться -{w=0.2} навалил боком под плёнку на Львовский переулок, 9."
    "Вот только не смог он до неё доехать{w=0.2}.{w=0.2}.{w=0.2}."
    pause 2
    "В конце переулка Димка увидел что-то странное,{w=0.2} но не разглядел,{w=0.2} что это."
    "А это было{w=0.2}.{w=0.2}.{w=0.2}."
    play sound fb
    stop ambience
    scene tank
    show deadlylxrd at left
    show doshd
    with flash
    lxrd "Опа{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    lxrd "А вот и наш клиент."
    "Вадимка зарядил крупнокалиберный снаряд в дуло."
    lxrd "Жаль конечно этого добряка."
    lxrd "Но ничего не поделаешь."
    window hide
    pause 2
    stop music fadeout 3
    lxrd "Прощай,{w=0.2} лысая{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    "И Вадимка нажал на кнопку выстрела."
    play sound fb
    scene nmall at ed_bus_move
    show doshd
    with flash
    play ambience dviglo fadein 2
    skt "Что там такое бля?" with vpunch
    skt "Не вижу нихуя..."
    with flash
    stop music
    stop sound
    stop ambience fadeout 6
    scene black
    $ renpy.movie_cutscene('source/videosos/pizdamashine.webm')
    window hide
    play sound probitie1
    pause 2
    scene domintnight
    play sound vozduh
    show unblink
    pause 1.5
    skt "ЕБАТЬ!" with vpunch
    "Скит немного сильно так ахуел от своего сна."
    skt "Присниться же такое..."
    skt "Надо на кухню сходить -{w} водички глотнуть."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Неони:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music outofit0 fadein 2
    scene laba with ed_night_dis
    nvl clear
    nvlbazar "Он стоял напротив колбы в своей лаборатории."
    nvlbazar "Делать было нехуй."
    nvlbazar "Только ждать Вадимку."
    nvlbazar "Он должен {b}ЭТО{/b} видеть."
    nvl clear
    "В лабу заскакивает Вадос."
    window hide
    play sound door_open
    show deadlylxrd:
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos 3.0
            linear 0.80 xpos 0.75
    with Pause(0.90)
    show deadlylxrd:
        xpos 0.75
    window show 
    lxrd "Что на этот раз?" with vpunch
    lxrd "Снова свои детские секс-{w=0.2}игрушки будешь демонстрировать в деле?"
    lxrd "Типа ОЙ СМАРИ ВАДЯ,{w=0.2} КАКОЙ МАЛЕНЬКИЙ СТРАПОН, {w=0.2}АХАХА?" with vpunch
    window hide
    play sound smehb1
    pause 3
    "Вадимка сам проорал со своего пёрла."
    lxrd "Меня это уже заебало,{w=0.2} веришь?" with vpunch
    "Говорил он сквозь смех."
    nn "На этот раз -{w} кое-{w=0.2}что грандиознее."
    nn "Смари."
    window hide
    show lordsprclon4 at center:
        xcenter -0.4 ycenter 0.5 rotate 0
        easein 0.4 xcenter 0.5 rotate 360
        ease 0.05 zoom 1.3
        ease 0.05 zoom 1.0
        ease 0.1 rotate -360
    $ renpy.pause (0.5)
    window show
    "Стенка колбы отодвинулась,{w=0.2} после чего оттуда в знакомой манере вылетело чудо,{w=0.2} отдалённо напоминающее Канеки."
    play sound gul
    lxrd2 "Ащихитео..." with vpunch
    window hide
    scene laba
    show deadlylxrd
    show lordsprclon4 at right
    with flash_fast2
    play sound smehb2
    hide deadlylxrd
    show deadlylxrd:
        subpixel True xpos 0.25 default
        parallel:
            Null(600.0, 720.0)
            'deadlylxrd'
        parallel:
            xzoom 1
            linear 0.20 xzoom 2
            linear 0.20 xzoom 1
            linear 0.60 xzoom 2
            linear 0.20 xzoom 1
        parallel:
            yzoom 1
            linear 0.20 yzoom 1
            linear 0.40 yzoom 2
            linear 0.20 yzoom 1
            linear 0.20 yzoom 2
            linear 0.20 yzoom 1
    with Pause(1.30)
    show deadlylxrd:
        xzoom 1 yzoom 1
    hide deadlylxrd
    show deadlylxrd:
        subpixel True xpos 0.25 default
        parallel:
            Null(600.0, 720.0)
            'deadlylxrd'
        parallel:
            xzoom 1
            linear 0.20 xzoom 2
            linear 0.20 xzoom 1
            linear 0.60 xzoom 2
            linear 0.20 xzoom 1
        parallel:
            yzoom 1
            linear 0.20 yzoom 1
            linear 0.40 yzoom 2
            linear 0.20 yzoom 1
            linear 0.20 yzoom 2
            linear 0.20 yzoom 1
    with Pause(1.30)
    show deadlylxrd:
        xzoom 1 yzoom 1
    window show
    "Вадимка проорал с этого чуда."
    lxrd "Курганский Гуль -{w} это,{w=0.2} конечно,{w=0.2} ахуительно..."
    "Говорил он сквозь смех."
    lxrd "Но я видал и круче." with vpunch
    nn "На этот случай у меня припасено особое оружие."
    "Стенка уже другой колбы отодвинулась в сторону,{w=0.2} дабы не мешать эффектному появлению...{w} Этого {b}<<чуда>>{/b}."
    hide lordsprclon4
    hide deadlylxrd
    $ renpy.movie_cutscene('source/videosos/topgamer.webm')
    window hide
    show deadlylxrd at right
    show ddoser at center:
        xcenter -0.4 ycenter 0.5 rotate 0
        easein 0.4 xcenter 0.5 rotate 360
        ease 0.05 zoom 1.3
        ease 0.05 zoom 1.0
        ease 0.1 rotate -360
    $ renpy.pause (0.5)
    window show
    "В лабу,{w=0.2} порвав футболку за 25к,{w=0.2} влетело создание,{w=0.2} отдалённо напоминающее Вадима Морозова."
    window hide
    play sound ddos
    pause 21
    play sound stul
    show kreslo:
        subpixel True default
        parallel:
            Null(600.0, 720.0)
            'kreslo'
        parallel:
            matrixtransform ScaleMatrix(0.3, 0.3, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
            linear 0.59 matrixtransform ScaleMatrix(2.0, 2.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    with Pause(0.39)
    show kreslo:
        matrixtransform ScaleMatrix(2.0, 2.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    play sound2 sfx_punch_washstand
    scene laba
    show deadlylxrd at right
    show ddoser
    show dark_LW0607
    show blood_LW0607
    with flash_fast_red2
    play ambience huevo
    nn "Ай,{w=0.2} сука{w=0.2}.{w=0.2}.{w=0.2}."
    "Топгеймер кинул стулом в Казаха."
    "Тот аж ахуел."
    window hide
    play sound ddos1
    stop ambience fadeout 2
    hide dark_LW0607
    hide blood_LW0607
    with dissolve2
    pause 11
    play sound ddos2
    pause 16
    hide ddoser
    hide deadlylxrd
    play sound nitroblya
    show deadlylxrd:
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            pos (0.75, 1.0) rotate 0.0
            linear 0.16 pos (0.75, 1.0) rotate 0.0
            linear 0.90 pos (0.5, 3.0) rotate -180.0
    show ddoser:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'ddoser'
        parallel:
            xpos 0.5
            linear 0.16 xpos 0.75
            linear 0.60 xpos 2.0
    with Pause(0.90)
    show deadlylxrd:
        pos (0.5, 3.0) rotate 180.0
    show ddoser:
        xpos 2.0
    play sound2 sfx_body_bump
    pause 1
    hide deadlylxrd
    play sound2 uebalsya
    show deadlylxrd:
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
            'deadlylxrd'
        parallel:
            ypos 2.0
            linear 0.68 ypos 1.5
            linear 0.20 ypos 1.2
        parallel:
            rotate 90.0
            linear 0.88 rotate 0.0
    with Pause(0.98)
    show deadlylxrd:
        ypos 1.2 rotate 0.0
    pause 1.6
    window show
    "Топгеймер со свистом шин улетел из лабы,{w=0.2} попутно сбив Вадима Морозова."
    lxrd "Это чё такое,{w=0.2} придурок?" with vpunch
    lxrd "С хера ли клоны такие буйные пошли?" with vpunch
    lxrd "Он ещё и съебался{w=0.2}.{w=0.2}.{w=0.2}."
    stop music fadeout 5
    nn "Похуй." with vpunch
    nn "У всех бывают неудачные дни."
    nn "Но у меня остался ещё один сюрприз." with vpunch
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Иветты:")
    hide zatemnenie with dissolve2
    play music vampire
    scene black with ed_night_dis
    scene kk with ed_night_dis
    nvl clear
    nvlbazar "Она сидела в абсолютных потёмках."
    nvlbazar "Видны были лишь очертания бункера."
    nvlbazar "Того самого бункера,{w=0.2} что стал её тюрьмой."
    nvl clear
    nvlbazar "А всё обострилось после разлуки с самым близким для неё человеком."
    nvlbazar "Иветта не могла легко этого вынести."
    nvlbazar "В начале своего заточения она пыталась разъебшить стены и сбежать,{w=0.2} но..."
    nvlbazar "Это же не гипсокартон."
    nvl clear
    nvlbazar "Плотные бетонные стены,{w=0.2} что поперёк натырканы арматурой,{w=0.2} ослабляющей любые радиочастоты."
    nvlbazar "В общем,{w=0.2} даже GSM тут не ловил."
    nvlbazar "Да и сам бункер находился достаточно глубоко под землёй."
    nvlbazar "Глубже лабы Казаха."
    nvl clear
    nvlbazar "Но -{w} режущая уши тишина не могла длиться вечно."
    nvlbazar "И следом за открывшейся дверью,{w=0.2} в бункер залетает Казах."
    nvl clear
    play sound door_open
    show kazahspr:
        subpixel True default
        parallel:
            Null(726.0, 754.0)
            'kazahspr'
        parallel:
            xpos -0.3
            linear 0.50 xpos 0.25
    with Pause(0.60)
    show kazahspr:
        xpos 0.25
    nn "Успокоилась?"
    ivt1 "Пошёл на хуй." with vpunch
    nn "А ты не меняешься."
    ivt1 "Где Василиса?" with vpunch
    ivt1 "Куда ты её дел?" with vpunch
    nn "Спокойнее."
    nn "Я обещал вам отдельные тела -{w} я своё обещание выполнил." with vpunch
    nn "С вас спрос тоже был."
    nn "Василиса пока свою часть выполняет."
    nn "Хоть и со скрипом."
    nn "Ну а ты..."
    nn "Нет бы по-{w=0.2}нормальному..."
    nn "Опять наши планы срываешь."
    ivt1 "Пошёл в жопу." with vpunch
    ivt1 "Без Василисы я и палец{w=0.2}-о{w=0.2}-палец не ударю."
    nn "Ха." with vpunch
    nn "Надолго ли тебя так хватит?"
    ivt1 "Посмотришь."
    window hide
    play sound door_open
    show deadlylxrd:
        subpixel True default
        parallel:
            Null(726.0, 754.0)
            'deadlylxrd'
        parallel:
            xpos 1.3
            linear 0.50 xpos 0.75
    with Pause(0.60)
    show deadlylxrd:
        xpos 0.75
    "В комнату залетает Вадим Морозов."
    lxrd "Это и есть твой сюрприз?"
    nn "Нет." with vpunch
    nn "Но это очень важный винтик в этом большом механизме."
    nn "Тебе стоит увидить её в действии."
    lxrd "Я смотрел записи с камер в клубе."
    lxrd "Это,{w=0.2} видимо,{w=0.2} она..."
    lxrd "Хотя я изначально думал,{w=0.2} что это Василиса."
    nn "Это и есть Василиса." with vpunch
    nn "Точнее -{w} её альтер{w=0.2}-эго."
    lxrd "Понял."
    lxrd "И как ты их разъеденил?"
    nn "Василису в клона поместил и всё."
    nn "Наплёл ей про смерть оригинала."
    nn "Она даже ничего не вспомнила."
    ivt1 "МРАЗЬ!" with vpunch
    window hide
    play sound hark
    show harchok:
        subpixel True xpos 0.2 default
        parallel:
            Null(368.0, 411.0)
            'harchok'
        parallel:
            ypos 1.7
            linear 0.21 ypos 0.5 xpos 0.2
    with Pause(0.60)
    show harchok:
        pos (0.2, 0.5)
    window show
    "Смачный харчок полетел в ебло Казаху."
    window hide
    play sound smehb1
    hide deadlylxrd
    show deadlylxrd:
        subpixel True xpos 0.75 default
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            ypos 1.0 xpos 0.75
            linear 0.80 ypos 1.1
        parallel:
            rotate 0.0
            linear 0.13 rotate 180.0
            linear 0.14 rotate 0.0
            linear 0.18 rotate 90.0
            linear 0.21 rotate 270.0
            linear 0.14 rotate 0.0
    with Pause(0.90)
    show deadlylxrd:
        pos (0.75, 1.1) rotate 0.0
    hide deadlylxrd
    show deadlylxrd:
        subpixel True xpos 0.75 default
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            ypos 1.0 xpos 0.75
            linear 0.80 ypos 1.1
        parallel:
            rotate 0.0
            linear 0.13 rotate 180.0
            linear 0.14 rotate 0.0
            linear 0.18 rotate 90.0
            linear 0.21 rotate 270.0
            linear 0.14 rotate 0.0
    with Pause(0.90)
    show deadlylxrd:
        pos (0.75, 1.1) rotate 0.0
    pause 1
    "Вадимка чётко гоготнул с этой всей хуеты."
    window hide
    show harchok:
        subpixel True
        pos (0.2, 0.5)
        linear 0.24 pos (-0.3, 1.0)
    with Pause(0.34)
    show harchok:
        pos (-0.3, 1.0)
    window show
    "Казах вытер харчок с ебла."
    nn "Слушай сюда,{w=0.2} блядь." with vpunch
    nn "У тебя нет выбора -{w} послать нас или помочь." with vpunch
    nn "Жизнь твоей {b}<<подруги>>{/b} -{w} в твоих руках." with vpunch
    lxrd "Тут он прав."
    lxrd "Так что заканчивай харкаться и давай уже делом займись бле{w=0.2}-а{w=0.2}-а{w=0.2}-ать." with vpunch
    "Натужно протянул Вадимка."
    ivt1 "Знаете,{w=0.2} что?"
    ivt1 "Идите нахуй оба." with vpunch
    ivt1 "Малолетки конченные." with vpunch
    "Вадимка и Казах смирили её жгучими взглядами."
    nn "Ты ещё передумаешь."
    ivt1 "Идите нахуй.{w} Оба." with vpunch
    window hide
    play sound door_open
    show kazahspr:
        subpixel True
        ypos 1.0
        linear 0.50 ypos 2.0
    show deadlylxrd:
        subpixel True
        ypos 1.1
        linear 0.50 ypos 2.2
    with Pause(0.60)
    show kazahspr:
        ypos 2.0
    show deadlylxrd:
        ypos 2.2
    window show
    "И они ушли.{w} Нахуй.{w} Оба."
    nvl clear
    nvlvas "Я осталсь думать,{w=0.2} чё же делать дальше?"
    nvlvas "Порыскав по комнате,{w=0.2} нашла люк."
    nvl clear
    play sound stmetal
    scene vent with ed_lap
    nvlvas "Вентиляционная шахта, {w=0.2}значит..."
    nvlvas "Придётся поползать..."
    nvlvas "Как в старые добрые..."
    nvl clear
    window hide
    pause 2
    play sound stmetal
    scene laba with ed_lap
    th2 "Вот я и на месте."
    th2 "Осталось только найти выход."
    window hide
    pause 2
    "Иветта заметила странную деревянную дверь."
    "С подписью {b}ПОСТОРОННИМ ВХОД ВОПСРЕЩЁН БЛЯ{/b}."
    ivt1 "И чё это значит?"
    "Любопытство взяло верх."
    play sound door_open
    play ambience adp fadein 2
    scene portal with ed_lap
    "Иветта заглянула в какое-{w=0.2}то странное помещение."
    "Возле странного сооружения была табличка с надписью:{w=0.2} {b}<<Портал в Новошахтинск>>{/b}."
    "Рядом лежал модифицированный дигл."
    "На нём была надпись -{w} Дамирке от Вадимки."
    "Иветта сразу прикарманила ствол."
    th2 "Попробовать войти?"
    th2 "И где этот Новошахтинск..."
    stop music fadeout 6
    "Но шестое чувство между ног давало понять Иветте,{w=0.2} где искать Василису."
    "Нужно было войти в портал."
    "Работает ли он вообще?" with vpunch
    th2 "Хуй с ним."
    th2 "Была не была."
    "После чего Иветта сиганула в портал вперёд ногами нахуй."
    stop ambience
    $ renpy.movie_cutscene('source/videosos/luntik.webm')
    window hide
    play sound trigger
    scene portal:
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
    pause 3
    scene zagruzka with ed_alpha_diss_fast
    pause 1
    play sound travel
    pause 1
    scene nport:
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
    pause 1.8
    scene nport with ed_alpha_diss_fast
    th2 "Фух мля..."
    "Иветта обернулась."
    scene domext with pushleft
    ivt1 "Я близко."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Димы:")
    hide zatemnenie with dissolve2
    play music zapad fadein 5
    scene black with ed_night_dis
    scene kuhnyanight with ed_night_dis
    "Зайдя на кухню,{w=0.2} Дима узрел ахуенную картину."
    "Вечный спал за столом,{w=0.2} обнимая пустые бутылки."
    "А в углу комнаты..."
    "Кхм..."
    "Вам лучше это увидеть самим."
    $ renpy.movie_cutscene('source/videosos/drochit.webm')
    "В углу комнаты сидела Василиса."
    "Голая." with vpunch
    "Сидела и наяривала." with vpunch
    "Смотря на спящего Вечного." with vpunch
    "И лишь единственная мысль проскочила в голове у Скита:"
    th "Хорошая малолетка..." with vpunch
    th "Она напоминает мне ту самую..."
    th "От которой у меня теперь есть дочь..."
    "Василиса заметила палящигося Скита."
    vas "ВЫЙДИ НАХУЙ ОТСЮДА,{w=0.2} СУКА!" with vpunch
    "От таких криков проснулся Вечный."
    show bergennorm:
        subpixel True default
        parallel:
            Null(726.0, 754.0)
            'bergennorm'
        parallel:
            xpos -0.3
            linear 0.50 xpos 0.25
    with Pause(0.60)
    show bergennorm:
        xpos 0.25
    vchn "Чё бля происходит?" with vpunch
    play sound door_break
    "Скит плеснул с фильтра воды в чашку,{w=0.2} и убежал,{w=0.2} попутно попивая водичку свою ебейшую."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Вечного:")
    hide zatemnenie with dissolve2
    scene kuhnyanight
    show vasilisanight
    with flash
    "Василиса уже успела одеться."
    vchn "Ну и чё это было?" with vpunch
    "Она не знала,{w=0.2} что и ответить."
    vas "Иногда мне бывает трудно себя сдерживать."
    vas "Ты заснул,{w=0.2} и{w=0.2}.{w=0.2}.{w=0.2}.{nw}"
    vchn "Понятно." with vpunch
    "Вечный понурил ебалом."
    "Настроение было парашное."
    "Всё из{w=0.2}-за прерванного сна,{w=0.2} где он снова сидел и коддил какой{w=0.2}-то {b}SKITETSKY REMASTER{/b}."
    "Хер его знает,{w=0.2} что это..."
    "Но во снах Вечного он сидел и делал это говно."
    "Игрушка какая{w=0.2}-то вроде."
    stop music fadeout 5
    vas "Я иду спать." with vpunch
    vchn "Иди."
    window hide
    play sound door_open
    show vasilisanight:
        subpixel True
        ypos 1.0
        linear 0.50 ypos 2.2
    with Pause(0.60)
    show vasilisanight:
        ypos 2.2
    window show
    "Вечный остался на кухне один."
    "Делать было нехуй."
    window hide
    play music lonely fadein 2
    pause 2
    "Вечный вспомнил,{w=0.2} что он так и не дочитал дневник."
    "На трезвую голову не пошло."
    "Но теперь{w=0.2}-то он угашен в нулину блеать!" with vpunch
    "И можно дочитать."
    play sound door_open
    scene domintnight with ed_lap
    window hide
    play sound dostal
    show diary:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'diary'
        parallel:
            ypos 2.0
            linear 0.50 ypos 1.0
    with Pause(0.60)
    show diary:
        ypos 1.0
    nvl clear
    nvlbazar "Проверив,{w=0.2} спят ли Василиса и Скит,{w=0.2} вечный взял дневник."
    nvlbazar "Он лежал на том же месте."
    nvlvhcn "Она ничего не заметила,{w=0.2} видимо."
    nvlvhcn "Оно и к лучшему."
    nvl clear
    hide diary
    play sound ubralstvol
    show diary:
        ypos 0.0
        ease 0.5 ypos 1.5

    pause 0.6
    hide diary
    nvlbazar "Вечный начал читать дальше."
    nvl clear
    nvlvas "В один момент я просто потеряла контроль над ситуацией."
    nvlvas "В том самом лагере были три идиота,{w=0.2} которые канифолили мне мозги."
    nvlvas "Я для них была унтерменьшем."
    nvl clear
    nvlvas "Было достаточно грустно наблюдать их нападки."
    nvlvas "Однако,{w=0.2} виду я не подавала."
    nvlvas "Но есть одно но."
    nvl clear
    nvlvas "Недавно я вспомнила,{w=0.2} что нас было двое."
    nvlvas "Да{w=0.2}-да,{w=0.2} не удивляйтесь."
    nvl clear
    nvlvhcn "К кому она обращается блеать?"
    nvl clear
    nvlvas "Иветта."
    nvlvas "Та самая Иветта."
    nvlvas "Она же -{w} моя тёмная сторона."
    nvlvas "Имея неподконтрольную ненависть в виде Иветты -{w} можно вырезать целый батальйон."
    nvl clear
    nvlvas "Как бы это не звучало,{w=0.2} но{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvas "Нечто подобное и произошло после."
    nvlvas "После очередных подъёбок от этих патау Иветта начала меня буквально упрашивать отдать контроль над телом."
    nvlvas "Ей было просто больно на всё это смотреть."
    nvl clear
    nvlvas "На то,{w=0.2} как они со мной обращаются."
    nvlvas "Вообще с нихуя."
    nvlvas "Они забили стрелку возле сцены вечером."
    nvlvas "Чем это закончится было очевидно."
    nvlvas "И я решилась."
    nvl clear
    stop music fadeout 5
    nvlvas "В самый важный момент я отдала ей контроль."
    nvlvas "После чего начался пиздец."
    nvl clear
    nvlbazar "Вечный буквально визуализировал это всё у себя в голове."
    nvl clear
    scene black with ed_night_dis
    play music mosh1 fadein 2
    scene scena_leto
    show sergo1 at right
    show marat1
    show sanya1 at left
    with ed_lap
    par1 "Мы пришли поговорить."
    par1 "Видишь ли,{w=0.2} нам надоела эта бессмысленная вражда."
    par1 "Предлагаем мирное соглашение на взаимовыгодных условиях."
    vas "Да пошли вы." with vpunch
    par1 "Ну-{w=0.2}у,{w=0.2} раз ты сама против{w=0.2}.{w=0.2}.{w=0.2}.{w} То{w=0.2}.{w=0.2}.{w=0.2}."
    par2 "Решим всё менее гуманными методами." with vpunch
    par3 "Теперь ты никуда не денешься!" with vpunch
    par3 "Хоть в нашем гуманном обществе и не принято бить женщин,{w=0.2} сегодня я нарушу {b}закон гор{/b}."
    "Сказал правый парниша,{w=0.2} попутно надевая на пальцы кастет."
    "Василиса,{w=0.2} почуяв неладное,{w=0.2} дала команду своему {b}альтер-эго{/b}."
    th1 "Твой час настал."
    th1 "Покажи им свю нашу мощь,{w=0.2} {b}подруга{/b}."
    th2 "Я не подведу."
    $ Aw_HeartAttack("scena_leto")
    ivt1 "Вам пиздец." with vpunch
    window hide
    stop music
    play music mosh2
    scene scena_leto
    show sergo1
    $ Aw_HeartAttack("scena_leto")
    with flash_fast2
    play sound dostalstvol
    show pizdavsem:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem'
        parallel:
            ypos 2.0
            linear 0.50 ypos 1.0
    with Pause(0.60)
    show pizdavsem:
        ypos 1.0
    hide pizdavsem
    play sound aw_knife_slash_3
    show pizdavsem:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem'
        parallel:
            xpos 0.5
            linear 0.40 xpos -0.6
    with Pause(0.60)
    show pizdavsem:
        xpos -0.6
    hide pizdavsem
    play sound aw_knife_slash_3
    show pizdavsem2:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 1.6
            linear 0.50 xpos -0.6
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 1.6
            linear 0.50 xpos -0.6
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6
    hide pizdavsem2
    hide sergo1
    play sound sfx_body_bump
    show sergo11:
        subpixel True default
        parallel:
            Null(600.0, 720.0)
            'sergo11'
        parallel:
            pos (0.5, 1.0) rotate 0.0
            linear 0.50 pos (0.8, 2.0) rotate 120.0
    show sergo12:
        subpixel True default
        parallel:
            Null(600.0, 720.0)
            'sergo12'
        parallel:
            pos (0.5, 1.0) rotate 0.0
            linear 0.50 pos (0.35, 2.2) rotate -120.0
    show sergo13:
        subpixel True default
        parallel:
            Null(600.0, 720.0)
            'sergo13'
        parallel:
            pos (0.5, 1.0) rotate 0.0
            linear 0.50 pos (0.2, 2.0) rotate -120.0
    with Pause(0.60)
    show sergo11:
        pos (0.8, 2.0) rotate 120.0
    show sergo12:
        pos (0.35, 2.2) rotate -120.0
    show sergo13:
        pos (0.2, 2.0) rotate -120.0
    window show
    "Она нашинковала первого парнушку аки {b}буряки на винегрет{/b}."
    "Ярость полностью овладела ею."
    "Исчезли абсолютно все чувства."
    "Кроме неконтролируемой ненависти."
    "А в это время со спины готовилось нападение."
    "Иветта ловко извернулась и начала кромсать второго обидчика."
    window hide
    scene scena_leto1
    show sanya1
    $ Aw_HeartAttack("scena_leto1")
    with pushleft
    play sound dostalstvol
    show pizdavsem2:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            ypos 2.0
            linear 0.50 ypos 1.0
    with Pause(0.60)
    show pizdavsem2:
        ypos 1.0
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 0.5
            linear 0.40 xpos -0.6
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 1.6
            linear 0.50 xpos -0.6
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 1.6
            linear 0.50 xpos -0.6
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6
    hide pizdavsem2
    hide sanya1
    play sound sfx_body_bump
    show sanya11:
        subpixel True default
        parallel:
            Null(600.0, 720.0)
            'sanya11'
        parallel:
            pos (0.5, 1.0) rotate 0.0
            linear 0.50 pos (0.8, 2.0) rotate 120.0
    show sanya12:
        subpixel True default
        parallel:
            Null(600.0, 720.0)
            'sanya12'
        parallel:
            pos (0.5, 1.0) rotate 0.0
            linear 0.50 pos (0.35, 2.2) rotate -120.0
    show sanya13:
        subpixel True default
        parallel:
            Null(600.0, 720.0)
            'sanya13'
        parallel:
            pos (0.5, 1.0) rotate 0.0
            linear 0.50 pos (0.2, 2.0) rotate -120.0
    with Pause(0.60)
    show sanya11:
        pos (0.8, 2.0) rotate 120.0
    show sanya12:
        pos (0.35, 2.2) rotate -120.0
    show sanya13:
        pos (0.2, 2.0) rotate -120.0
    window show
    "Иветта покрошила и вторую редиску."
    "Она,{w=0.2} аки {b}Шеф-повар{/b},{w=0.2} кромсающий свежую щуку,{w=0.2} которая отправится в уху."
    ivt1 "ДЕРЖИ{w=0.2}-И{w=0.2}-И{w=0.2}-ИСЬ,{w=0.2} ОГУЗОК!" with vpunch
    "Иветта повернула свой взор на последнего обидчика."
    window hide
    scene scena_leto
    show marat1
    $ Aw_HeartAttack("scena_leto")
    with pushright
    oguzok "Прошу,{w=0.2} остановись!" with vpunch
    ivt1 "А ГДЕ БЫЛ ТЫ,{w=0.2} КОГДА Я ПРОСИЛА ОСТАНОВИТЬСЯ?" with vpunch
    ivt1 "А,{w=0.2} БЛЯТЬ?" with vpunch
    "Буквально проорала ему в ебало эти слова Иветта."
    ivt1 "ГДЕ,{w=0.2} НАХУЙ?" with vpunch
    oguzok "{w=0.5}не{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} надо{w=0.2}.{w=0.2}.{w=0.2}."
    "Огузок совсем обмяк."
    "Иветте надоело с ним нянчится."
    "И она,{w=0.2} орудуя топором аки {b}Кратос{/b},{w=0.2} начала шинковать Огузка в свой {b}кровавый салат{/b}."
    window hide
    play sound dostalstvol
    show pizdavsem2:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            ypos 2.0
            linear 0.50 ypos 1.0
    with Pause(0.60)
    show pizdavsem2:
        ypos 1.0
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 0.5
            linear 0.40 xpos -0.6
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 1.6
            linear 0.50 xpos -0.6
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        subpixel True default
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 1.6
            linear 0.50 xpos -0.6
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6
    hide pizdavsem2
    hide marat1
    play sound sfx_body_bump
    show sanya11:
        subpixel True default
        parallel:
            Null(600.0, 720.0)
            'marat11'
        parallel:
            pos (0.5, 1.0) rotate 0.0
            linear 0.50 pos (0.8, 2.0) rotate 120.0
    show marat12:
        subpixel True default
        parallel:
            Null(600.0, 720.0)
            'marat12'
        parallel:
            pos (0.5, 1.0) rotate 0.0
            linear 0.50 pos (0.35, 2.2) rotate -120.0
    show marat13:
        subpixel True default
        parallel:
            Null(600.0, 720.0)
            'marat13'
        parallel:
            pos (0.5, 1.0) rotate 0.0
            linear 0.50 pos (0.2, 2.0) rotate -120.0
    with Pause(0.60)
    show marat11:
        pos (0.8, 2.0) rotate 120.0
    show marat12:
        pos (0.35, 2.2) rotate -120.0
    show marat13:
        pos (0.2, 2.0) rotate -120.0
    window show
    show blink
    stop music fadeout 4
    "Иветта присела на ближайшую лавочку и прикрыла глаза,{w=0.2} дабы перевести дыхание."
    th2 "Вот и всё."
    th2 "Дышим глубже." with vpunch
    th1 "Я хотела их припугнуть{w=0.2}.{w=0.2}.{w=0.2}."
    play music outofit1
    scene scena_leto
    show unblink
    th1 "А ты их нашинковала{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    hide unblink
    th2 "Омг,{w=0.2} блять,{w=0.2} вечно тебе всё не нравится{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    th1 "Ты в курсе,{w=0.2} что нам с тобой напару пиздец?" with vpunch
    th2 "Не дрейфь,{w=0.2} прорвёмся."
    th2 "Не зря же я тут вон сколько небо копчу."
    th2 "И я,{w=0.2} и ты{w=0.2}.{w=0.2}.{w=0.2}."
    th2 "Проврёмся."
    "Белоснежные трусики уже насквозь промокли."
    "Иветта запустила туда свои шаловливые пальчики,{w=0.2} после чего начала делать прерывистые движения взад-{w=0.2}вперёд."
    th2 "Обожаю насилие." with vpunch
    th2 "И ничего не могу с собой поделать."
    th2 "Слишком сильно возбуждает."
    th1 "Не,{w=0.2} подруга.{w} Сильнее насилия возбуждают другие девочки."
    th2 "Знаешь такое выражение:{w=0.2} {b}<<Каждый дрочит как он хочет>>{/b}?"
    th1 "Не понаслышке знаю,{w=0.2} подруга."
    "Движения всё ускорились."
    th1 "Ак{w=0.2}-к{w=0.2}-уратне{w=0.2}-е{w=0.2}.{w=0.2}.{w=0.2}."
    th1 "Не марк{w=0.2}-о{w=0.2}-вку чист{w=0.2}-ишь{w=0.2}.{w=0.2}.{w=0.2}."
    "Пытаясь совладать с языком думала Василиса."
    th2 "Сделаем красиво?"
    "Они обе чувствовали кайф от дрочки."
    "Пусть со стороны и выглядит,{w=0.2} что он терпят друг друга из-за невозможности разделиться{w=0.2}.{w=0.2}.{w=0.2}."
    "Пусть со стороны это выглядит о{w=0.2}-{w=0.2}о-{w=0.2}очень странно{w=0.2}.{w=0.2}.{w=0.2}."
    "Они обажают друг друга."
    "Была бы возможность получить отдельные тела{w=0.2}.{w=0.2}.{w=0.2}."
    "Они бы стали лучшей лесби-{w=0.2}парой."
    "Как никто другие знают все нужные точки входа друг друга."
    "Как бы это не звучало." with vpunch
    "Тем не менее,{w=0.2} блаженство не может длиться вечно."
    "Кончив и словив экстаз,{w=0.2} Иветта,{w=0.2} рубашка и юбка которой были все в крови,{w=0.2} начала доставать сигарету из секретного кармана."
    "Она знала,{w=0.2} что случится что-то подобное."
    "Вот и положила последнюю сигу {b}Kent Quant{/b} и желтый {b}Cricket{/b} за лямку бюсгалтера."
    "На стороне спины,{w=0.2} разумеется."
    stop music fadeout 5
    "Пока она тянулась за сигой,{w=0.2} локтём уронила окровавленный топор с лавочки."
    th2 "Ну да и хуй с ним." with vpunch
    "И аки {b}Виктор Баринов{/b},{w=0.2} {b}Шеф-повар{/b} ресторана {b}Clod Monet{/b}, прикурив цыбару,{w=0.2} сделала глубокую тягу и лишь тихо выдохнула{w=0.2}.{w=0.2}.{w=0.2}."
    $ renpy.movie_cutscene('source/videosos/pobeda.webm')
    window hide
    scene black with ed_night_dis
    scene domintnight with ed_lap
    "Вечный немного прихуел от этой истории."
    "Но ведь это не конец всей истории,{w=0.2} верно?"
    "Что же там дальше{w=0.2}.{w=0.2}.{w=0.2}."
    nvl clear
    nvlvas "После случившегося пришлось скрываться."
    nvlvas "В один из не самых примечательных дней была намечана стрелка с двумя ментами."
    nvlvas "Владик говорил,{w=0.2} только они смогут помочь."
    nvlvas "Встреча была намечена в баре."
    nvl clear
    "Вечный снова представил себе всё это воочию."
    window hide
    scene black with ed_night_dis
    play music bambino fadein 2
    scene bar100 with ed_lap
    nvlvas "Встречу положено было провести Иветте."
    nvlvas "Всё потому,{w=0.2} что она в нужном моменте сможет надавить."
    nvl clear
    nvlvas "Не тот случай?{w} Ха."
    nvlvas "Не для неё."
    nvlvas "Она не знает такого понятия в принципе."
    nvlvas "Вот и всё."
    nvl clear
    nvlbazar "Наигрывала какая{w=0.2}-то олдовая музычка{w=0.2}.{w=0.2}.{w=0.2}."
    nvlbazar "Вокруг Иветты,{w=0.2} что потягивала свежий мохито кружились какие{w=0.2}-то пьяные додики."
    nvlbazar "Самый рофлан в том,{w=0.2} что они оба решили подкатить к ней."
    nvlbazar "И оба были бы посланы нахуй,{w=0.2} если бы не начали рамсить прямо в баре."
    nvlbazar "После чего их спешно выдворила охрана."
    nvl clear
    nvlbazar "Напиток почти кончался,{w=0.2} а мусаров всё нет и нет."
    nvlbazar "Иветта начинала нервничать."
    nvlbazar "Отвлечься было просто не на что."
    nvlbazar "Только если на громких деградантов в противоположной стороне бара."
    nvl clear
    nvlbazar "Они обсуждали навар от проделанной ходки."
    nvlbazar "Скрутить 20 кило медных проводов с заброшенной ковровой фабрики -{w} это,{w=0.2} конечно,{w=0.2} ахуительно."
    nvlbazar "Но явно не то,{w=0.2} чем можно гордится."
    nvlbazar "Нет бы на работку пойти{w=0.2}.{w=0.2}.{w=0.2}."
    nvl clear
    nvlbazar "Да ну, {w=0.2}зачем?"
    nvlbazar "Можно же напиздить с государственной территории немного металла{w=0.2}.{w=0.2}.{w=0.2}."
    nvlbazar "Обжарить,{w=0.2} да сдать."
    nvlbazar "И пробухать всё лаве в ближайшем баре."
    nvlbazar "Реально дегроды."
    nvl clear
    nvlbazar "За размышлениями о пьяных додиках Иветта не заметила,{w=0.2} как к ней подсели те самые два мента."
    nvl clear
    window hide
    show ment:
        subpixel True default
        parallel:
            Null(750.0, 720.0)
            'ment'
        parallel:
            xpos 2.0
            linear 0.60 xpos 0.75
    show ment1:
        subpixel True default
        parallel:
            Null(600.0, 720.0)
            'ment1'
        parallel:
            xpos 2.0
            linear 0.60 xpos 0.25
    with Pause(0.70)
    show ment:
        xpos 0.75
    show ment1:
        xpos 0.25
    window show
    mt "Я вас категорически приветствую." with vpunch
    "Отсалютовал левый Мент."
    ivt1 "Нихао."
    ivt1 "Вы можете помочь с нарастающей проблемой?"
    "Менты посмотрили друг на друга."
    "Потом на Иветту."
    "И сказали:"
    mt1 "Вполне." with vpunch
    mt1 "Хотя это будет трудно."
    mt1 "Видел я фото того месива,{w=0.2} что ты учудила."
    mt "Балерина прям." with vpunch
    "Хохотнул левый Мент."
    mt "Есть вариант один{w=0.2}.{w=0.2}.{w=0.2}."
    mt "Косить под ненормальную." with vpunch
    ivt1 "Чёт не особо вариант{w=0.2}.{w=0.2}.{w=0.2}."
    mt1 "На пожизненное хочешь загреметь?" with vpunch
    "Сказал уже правый мент."
    "Причём одеты были не по форме."
    "Иветта не смогла разглядеть звание."
    "А то пришли небось два сержантика и пытаются глазёнками хлопать."
    "Приободрять."
    ivt1 "Не особо."
    "Тихо ответила Иветта."
    "Надо же драматизма нагнать."
    mt "Ну так вот."
    "Продолжил левый."
    mt "Мы дадим нужные показания."
    mt "Направим к нужному мозгоправу."
    mt "Он тебе всё чё хочешь подпишет и припишет." with vpunch
    "У Иветты загорелись глаза."
    "Победа снова так близка."
    mt "Но у нас есть одно условие." with vpunch
    "Глазёнки резко поменяли цвет своего огня."
    mt "Ты дашь нам в использование своё тело." with vpunch
    th1 "Чего блять?" with vpunch
    th1 "Это чё за шутки такие у них?" with vpunch
    ivt1 "Прикол я оценила."
    ivt1 "Что делать{w=0.2}-то нужно?"
    mt "А это и не прикол." with vpunch
    mt "Вот ему{w=0.2}.{w=0.2}.{w=0.2}."
    "Показал левый на правого Мента."
    mt "{w=0.2}.{w=0.2}.{w=0.2}.уже 27 скоро."
    mt "А он всё ещё бабу не приголубил."
    "Хохотнул левый Мент."
    mt1 "Серёг!" with vpunch
    "Поспешно решил оправдать своё честное имя правый Мент."
    mt "Да ладно."
    mt "Я всё понимаю."
    mt "Поэтому и предоставлю тебе для этого всё необходимое."
    th1 "Не соглашайся,{w=0.2} слышишь?" with vpunch
    th1 "Это наёб!" with vpunch
    "Лишь безумолку тараторила Василиса в мыслях Иветты."
    th2 "У нас с тобой нет выбора." with vpunch
    th1 "Выбор есть всегда!" with vpunch
    ivt1 "Я согласна." with vpunch
    th1 "Ты чё,{w=0.2} ебанулась?" with vpunch
    th1 "Они же нас трахнут и кинут!"
    th1 "Бля,{w=0.2} да это ребёнку понятно!" with vpunch
    th2 "Я тебе ещё раз повторяю."
    th2 "У нас нет выбора."
    mt "Тогда пройдёмте."
    stop music fadeout 5
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    "И они прыгнули в ментовскую шкоду."
    "И укатили в надвигающийся рассвет."
    "На хату левого Мента."
    "Где и произошёл весь процесс."
    window hide
    scene black with ed_night_dis
    scene nebo with ed_lap
    play music metro fadein 2
    nvl clear
    nvlbazar "{b}<<Серёга>>{/b} был неопытен,{w=0.2} но вот {b}<<Николай>>{/b}{w=0.2}.{w=0.2}.{w=0.2}."
    nvlbazar "Был любителем {b}БДСМ{/b}."
    nvlbazar "Кароче говоря,{w=0.2} они конкретно так испытали на прочность {b}ВСЕ{/b} отверстия Иветты."
    nvlbazar "Было больно.{w} Ещё больше -{w} неприятно."
    nvlbazar "Мерзко было за своё поведение перед Василисой."
    nvl clear
    nvlbazar "Которая,{w=0.2} кстати,{w=0.2} перестала разговаривать с Иветтой."
    nvlbazar "С концами нахуй."
    nvlbazar "Просто исчезла из сознания."
    nvlbazar "Но это на первый взгляд."
    nvlbazar "Она наблюдала за Иветтой."
    nvl clear
    nvlbazar "Последняя,{w=0.2} в свою очередь,{w=0.2} слилась с суда."
    nvlbazar "На котором должны были огласить приговор."
    nvlbazar "Она ушла в подполье с одной единственной целью."
    nvl clear
    nvlbazar "Нужно было совершить план мести."
    nvlbazar "Всё просто -{w} пожарный топорик оружие небольшое,{w=0.2} острое и надежное."
    nvlbazar "Осталось выцепить этих двоих."
    nvlbazar "И зачем соглашалась только?"
    nvl clear
    nvlbazar "Зря доверие Василисы проебала."
    nvlbazar "Ну ничего.{w} Это ещё можно исправить."
    nvlbazar "Посмотрим,{w=0.2} как вы у меня запляшете."
    nvl clear
    nvlbazar "Влад помог с поиском этих двух ментов."
    nvlbazar "Их ареал обитания -{w} {b}<<карамель>>{/b}."
    nvlbazar "Там,{w=0.2} по выходным,{w=0.2} они чаще всего и развлекаются."
    nvlbazar "Осталось только проскочить в випку."
    nvlbazar "Но у Иветты уже была нужная последовательность действий."
    nvlbazar "Осталось её воплотить.{w} Да."
    nvl clear
    scene black with ed_night_dis
    window hide
    stop music fadeout 4
    $ renpy.pause(5, hard=True)
    play music aw_monsterbot fadein 4
    $ renpy.pause(1, hard=True)
    play sound na_popei
    scene black with flash_fast2
    $ renpy.pause(1, hard=True)
    scene aw_club_f at aw_dance_2 with dissolve2
    "Расшатанный и убитый в хлам мозг —{w} явно позитивно откликался на атакующую уши музыку." with dissolve
    "Убитые таблетками чувства —{w} невнятно выражались на лице посредством улыбки и,{w=0.2} то закатывающихся,{w=0.2} то закрывающихся,{w=0.2} глаз."
    play sound na_popei
    $ Aw_Alko("aw_club_f")
    "В весёлом хаосе,{w=0.2} я опрокинула в себя сразу четыре шота текилы,{w=0.2} разбавив их рюмкой джина,{w=0.2} отполировав всё это {b}«дорожкой»{/b} с груди какой-то проститутки в туалете." with flash_fast2
    "После непродолжительного,{w=0.2} всё с той же {b}«дамой по вызову»{/b},{w=0.2} занятия {b}«ласками»{/b} в туалетной кабинке,{w=0.2} я вернулась в зал." with dissolve
    "Тело,{w=0.2} неподвластно,{w=0.2} двигалось в такт музыке,{w=0.2} что разливалась по клубу,{w=0.2} медленно продвигаясь в сторону барной стойки."
    window hide
    $ renpy.pause(2, hard=True)
    lis "Нормально ебашит?!" with hpunch
    "Спросила меня одна из посетительниц,{w=0.2} когда я таки дошла до бара,{w=0.2} намекнув бармену на повторение употребленного ранее."
    ivt1 "Улёт!" with vpunch
    "Она довольно улыбнулась мне,{w=0.2} принявшись потягивать коктейль."
    "Я же —{w} взялась заливать в себя пойло,{w=0.2} что пила до этого."
    play sound na_popei
    lis "Эй,{w=0.2} подруга,{w=0.2} не хочешь немного{w=0.2}.{w=0.2}.{w=0.2}." with flash_fast2
    "Шлепком по заду,{w=0.2} отвлекла меня всё та же девушка,{w=0.2} в конце своей реплики прикрыв одну своих ноздрей пальцем."
    ivt1 "После {b}«этого»{/b} меня распирает...{w} Если ты понимаешь." with dissolve
    lis "Меня тоже."
    "Прошептала она горячо мне на ухо."
    "Я обняла ее за плечи и,{w=0.2} поднявшись со стула —{w} пошла следом за ней в туалетную комнату."
    window hide
    scene black with fade3
    $ renpy.pause(3, hard=True)
    scene aw_club_f at aw_dance_2 with dissolve
    $ Aw_Alko("aw_club_f")
    lis "Нормас{w=0.2}.{w=0.2}.{w=0.2}." with dissolve
    "Только и проговорила {b}«она»{/b},{w=0.2} когда мы вышли вновь в зал."
    ivt1 "Повторим?"
    lis "Позже,{w=0.2} дорогуша."
    "Она принялась пританцовывать."
    lis "Как тебе музло?!" with hpunch
    "Ее стеклянные глаза уже не могли фокусироваться на мне,{w=0.2} из-за чего хаотично бегали вокруг,{w=0.2} пытаясь зацепиться за моё лицо,{w=0.2} которое,{w=0.2} по всей видимости,{w=0.2} у нее расшатывалось в такт музыке."
    ivt1 "Улёт!" with vpunch
    "Ответила я и она,{w=0.2} с глупой улыбкой и смехом —{w} удалилась вглубь зала,{w=0.2} а я,{w=0.2} в свою очередь, {w=0.2}вернулась к барной стойке."
    window hide
    stop music fadeout 6
    $ renpy.pause(2, hard=True)
    scene black with fade3
    $ renpy.pause(3, hard=True)
    play music aw_ost_blade
    scene aw_club_f at aw_dance_2 with dissolve2
    $ Aw_Alko("aw_club_f")
    $ renpy.pause(3, hard=True)
    "Спустя время —{w} я оторвалась от выпивки,{w=0.2} напоследок закинув в себя горсть обезболивающего и заливая его тумблером виски,{w=0.2} выбрасывая остаток денег на барную стойку и уходя от нее в приватный коридор,{w=0.2} в который,{w=0.2} пару минут назад,{w=0.2} прошли {b}«знакомые лица»{/b}." with dissolve
    lis "Вы к кому?" with fade2
    "Спросил меня крупный парень,{w=0.2} стоящий на входе в «приватку»."
    ivt1 "Двое мужчин,{w=0.2} что пару минут назад зашли{w=0.2}.{w=0.2}.{w=0.2}."
    lis "Комната?"
    ivt1 "Не знаю.{w} Но они тут частые гости.{w} Если не трудно —{w} можете сами у них спросить."
    ivt1 "Скажите,{w=0.2} что к ним пришла {b}«балерина»{/b}."
    lis "Колян,{w=0.2} подойди." with vpunch
    "Второй,{w=0.2} не менее крупный парень,{w=0.2} отошел от лесенки,{w=0.2} что вела в служебные помещения."
    lis "Погляди пока за этой."
    "{b}«Колян»{/b} -{w} лишь кивнул,{w=0.2} после чего первый отошел вглубь {b}«приватки»{/b},{w=0.2} скрываясь за занавесками."
    window hide
    $ renpy.pause(3, hard=True)
    "Спустя время —{w} {b}«не Колян»{/b} вернулся,{w=0.2} приподнимая передо мной занавеску."
    lis "Шестая."
    "Я лишь кивнула ему,{w=0.2} проходя внутрь коридора."
    window hide
    scene black with fade3
    play sound door_open
    scene aw_private_r_1
    show ment at right
    show ment1 at left
    with ed_lap
    mt "Какие лица,{w=0.2} ха-ха!{w} Серёг,{w=0.2} узнаешь?" with vpunch
    mt1 "Узнаю.{w} Трудно забыть такой{w=0.2}.{w=0.2}.{w=0.2}.{w} Такие красивые губы."
    mt1 "И с чем на этот раз,{w=0.2} {b}«балерина»{/b}?"
    ivt1 "Нужна помощь." with vpunch
    mt "А чё за помощь то,{w=0.2} девонька?"
    mt "Ты,{w=0.2} вроде как,{w=0.2} в прошлый раз кинула наше {b}«предприятие»{/b}."
    mt1 "За пригласительным не явилась.{w} А людей мы уже оповестили.{w} Где надо —{w} словечко замолвили.{w} Всё для вас устроили,{w=0.2} дамочка,{w=0.2} людей подняли нужных,{w=0.2} а вы же что?{w} Так дела не делаются."
    ivt1 "Возникла пара проблем.{w} Не до этого было."
    mt1 "Не красиво.{w} Очень не красиво{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    ivt1 "Мы можем обсудить и это тоже.{w} Думаю —{w} я придумаю,{w=0.2} как загладить {b}«свою вину»{/b}."
    mt "Прикрой дверь,{w=0.2} девонька.{w} Да на замочек.{w} Там и {b}«подумаем»{/b}."
    "Я лишь улыбнулась,{w=0.2} не отворачиваясь нащупав дверной замок и защелкнув его."
    mt1 "Проходи.{w} Водочки выпьем."
    "Жестом один из мужчин указал на диван,{w=0.2} вместе с этим опрокидывая в себя стопку водки."
    ivt1 "Зачем эти излишества." with vpunch
    "Скинув кроссовки,{w=0.2} я стянула с себя штаны,{w=0.2} откидывая их ногой в сторону,{w=0.2} после чего —{w} избавилась и от толстовки."
    mt "Еп...{w} Эффективно и быстро,{w=0.2} согласись,{w=0.2} Серёг?" with vpunch
    mt1 "Точно что." with vpunch
    mt "А чего эт за обвязки?{w} Новые {b}«штуки»{/b} хочешь попробовать?"
    ivt1 "Это?"
    "Я указала на бинт,{w=0.2} которым была обмотана с торса до груди,{w=0.2} прикрывая шрам на животе и грудь."
    "А за спиной —{w} плотно держал топор,{w=0.2} спрятанный от любопытных глаз."
    vas "Да.{w} Новые штуки." with vpunch
    "Потянув левой рукой за узел,{w=0.2} а правой придерживая топор за рукоять —{w} я распутала обмотки,{w=0.2} позволяя им упасть на пол."
    mt "Как сейчас помню эти классные сиськи."
    stop music fadeout 4
    "Облизнувшись начал один,{w=0.2} вытирая руки и рот шелковым полотенцем,{w=0.2} после подымаясь с места."
    play sound aw_shut_up_and_bleed_snd
    ivt1 "Я тоже всё помню." with vpunch
    "Процедила я,{w=0.2} глядя исподлобья на достаточно приблизившегося ублюдка,{w=0.2} выводя правую руку с топором из-за спины."
    window hide
    stop sound fadeout 1
    play music aw_shut_up_and_bleed
    play sound2 aw_axe_hit_2
    scene aw_private_ms_1 at aw_master_tryas with flash_fast_red2
    $ Aw_Alko("aw_private_ms_1")
    $ renpy.pause(0.8, hard=True)
    play sound2 aw_axe_hit_2
    scene aw_private_ms_1 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ Aw_Alko("aw_private_ms_2")
    play sound3 aw_wom_hight_scr
    scene black
    $ Aw_HeartAttack("black")
    $ renpy.pause(0.6, hard=True)
    play sound2 aw_axe_hit_2
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_2
    scene aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_2
    scene aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_2
    scene aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_1
    scene aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_kill_snd
    scene aw_private_ms_4 at aw_master_tryas with flash_fast_red2
    $ Aw_HeartAttack("aw_private_ms_4")
    $ renpy.pause(1.5, hard=True)
    mt1 "С-{w=0.2}с-{w=0.2}стой{w=0.2}.{w=0.2}.{w=0.2}." with dissolve2
    "Лежа на полу,{w=0.2} выставив перед собой раздробленную руку,{w=0.2} процедил едва-{w=0.2}едва «Серёга»."
    mt1 "П-{w=0.2}п-{w=0.2}просто{w=0.2}.{w=0.2}.{w=0.2}.{w} П-{w=0.2}п-{w=0.2}поговорим{w=0.2}.{w=0.2}.{w=0.2}."
    mt1 "В-{w=0.2}в-{w=0.2}вы{w=0.2}ы{w=0.2}.{w=0.2}.{w=0.2}."
    "Давясь кровавым кашлем,{w=0.2} попытался сказать он."
    mt1 "В-{w=0.2}в-{w=0.2}все{w=0.2}.{w=0.2}.{w=0.2}.{w} Обо вс{w=0.2}-ё{w=0.2}-ём{w=0.2}.{w=0.2}.{w=0.2}.{w} Можно дог{w=0.2}.{w=0.2}. {w}Договорится{w=0.2}.{w=0.2}.{w=0.2}."
    ivt1 "Ложись." with vpunch
    "Я кивнула на диван у стены."
    mt1 "Ч-{w=0.2}что?" with vpunch
    ivt1 "Ложись." with vpunch
    "Тот,{w=0.2} судорожно кивая,{w=0.2} перевернулся и,{w=0.2} неуклюже и со стонами,{w=0.2} принялся заползать на диванчик."
    play sound aw_knife_slash_3
    "Одев на руку пакет,{w=0.2} что лежал в кофе,{w=0.2} я подошла к нему и,{w=0.2} взяв за {b}«хер»{/b} -{w} натянула его вверх,{w=0.2} свободной рукой взмахивая топором." with flash_fast_red2
    ivt1 "Как по маслу.{w} Даже смачивать не пришлось."
    "Процедила я,{w=0.2} склонившись над ним и запихав его достоинство ему же в глотку."
    ivt1 "Глубже.{w} Глотай,{w=0.2} сучка." with vpunch
    "Перехватив топор,{w=0.2} я просунула его рукоять в рот насильника,{w=0.2} тем самым {b}«проталкивая»{/b} отрубленный орган глубже в его глотку."
    "Его глаза — {w}выдавали в нём страх."
    "Они горели мольбой и криком о помощи."
    "И дичайшим ужасом."
    "Настолько ярко и явно это всё читалось,{w=0.2} что я не могла на это смотреть."
    th "Уж чего-{w=0.2}чего —{w} а видеть их лица в кошмарах я уже конкретно заебалась,{w=0.2} а уж такое{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    th "Беззащитное?{w} Испуганное?{w} Отчаявшиеся?{w} Наполненное ужасом?"
    th "…{w=0.2} и подавно." with vpunch
    window hide
    scene black with fade2
    $ Aw_Alko("black")
    "Поэтому —{w} я лишь перевернула его на живот, {w=0.2}закрыв голову подушкой,{w=0.2} чтобы от от вида его разбитой черепушки не сблевать прямо на месте." with dissolve
    stop music fadeout 3
    ivt1 "А теперь —{w} я сладко кончу." with vpunch
    window hide
    play sound aw_kill_snd
    scene aw_private_ms_end
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with flash_fast_red2
    $ Aw_HeartAttack("aw_private_ms_end")
    $ renpy.pause(2, hard=True)
    scene black with fade3
    $ renpy.pause(5, hard=True)
    $ renpy.music.set_volume(0.6)
    play music eb fadein 2
    play ambience rain_out fadein 2
    scene nebo
    show doshd
    with ed_night_dis
    nvl clear
    nvlbazar "Иветта смотрела на ночное небо."
    nvlbazar "Она была уже вся мокрая."
    nvlbazar "Ливень всё хуярил и хуярил."
    nvlbazar "А настроения по{w=0.2}-прежнему не было."
    nvl clear
    nvlvas "Всё ещё обижаешься?"
    nvl clear
    nvlbazar "Вопрос,{w=0.2} казалось бы,{w=0.2} ушёл в пустоту."
    nvl clear
    nvlvas "Было б на что."
    nvlvas "Ты просто конченная."
    nvlvas "Тебе проблем мало было?"
    nvl clear
    nvlvas "Прости."
    nvl clear
    nvlvas "Не прощу."
    nvlvas "Ты мне такая нахуй не нужна."
    nvlvas "Бля,{w=0.2} я бы полжизни отдала за своё,{w=0.2} отдельное тело."
    nvlvas "И чтоб забыть тебя нахуй."
    nvl clear
    nvlvas "Перестань."
    nvl clear
    nvlvas "Не перестану."
    nvlvas "Я всё ещё тебя ненавижу."
    nvlvas "И когда ты только появилась?"
    nvl clear
    nvlvas "Я и есть твой защитный механизм."
    nvlvas "Без меня -{w} ты сдохнешь."
    nvl clear
    nvlvas "Можем проверить."
    nvlvas "И как же?"
    nvl clear
    nvlvas "Херово ты Влада слушала."
    nvlvas "Он ещё советовал в {b}iGandone LLC{/b} обратиться с этим вопросом."
    nvlvas "А ты пошла к мусорам."
    nvlvas "И что в итоге?"
    nvlvas "Никакого нам с тобой помилования{w=0.2}.{w=0.2}.{w=0.2}."
    nvl clear
    nvlvas "Не хотела я его слушать."
    nvlvas "Он безответно влюблён в тебя."
    nvlvas "Не в меня."
    nvlvas "Лично я ему ничем не обязана."
    nvl clear
    nvlvas "Ха."
    nvlvas "Твою жопу он тоже спасал."
    nvlvas "И не раз."
    nvl clear
    nvlvas "Вместе с твоей,{w=0.2} не забывай."
    nvl clear
    nvlvas "Так вот мне бы отдельную от тебя жопу."
    nvlvas "Да чтоб туда всякие мерзопакосные менты свои огрызки не сували."
    nvlvas "Улавливаешь суть?"
    nvl clear
    nvlvas "Значит,{w=0.2} идём к айгандону?"
    nvlvas "Да хоть сейчас."
    nvl clear
    nvlbazar "И они отправились в офис {b}iGandone LLC,{/b}{w=0.2} который находился неподалёку."
    nvl clear
    stop ambience fadeout 5
    scene black with ed_night_dis
    nvlbazar "Они шли пешком,{w=0.2} дабы проветрить голову."
    nvlbazar "И заболеть нахуй."
    nvlbazar "Ведь на улице ливень."
    nvlbazar "Но они всегда любили гулять под дождём."
    nvl clear
    nvlvas "Ты действительно хочешь отделиться?"
    nvl clear
    nvlvas "Да."
    nvlvas "И это не обсуждается."
    nvlvas "Тебе понятно?"
    nvl clear
    nvlvas "Ты ща довыёбываешься."
    nvlvas "Да так довыёбываешься,{w=0.2} что я с разбегу под колёса проезжающей машини сигану."
    nvlvas "И не будет ни меня,{w=0.2} ни тебя."
    nvlvas "Вот и всё блять."
    nvlvas "Распизделась она тут,{w=0.2} видите ли."
    nvl clear
    nvlvas "Успокойся."
    nvl clear
    nvlbazar "Василиса и Иветта поменялись ролями бля."
    nvl clear
    nvlvas "Успокоится?"
    nvlvas "А,{w=0.2} может,{w=0.2} ты просто на хуй пойдёшь?"
    nvlvas "Заебала,{w=0.2} в натуре."
    nvl clear
    nvlvas "Всё ей не нравится."
    nvlvas "Пыталась решить вопрос с гопниками в лагере -{w} опять не так."
    nvlvas "Пыталась решить вопрос с сизо -{w} снова не так бля."
    nvlvas "Наебенила я этих мудаков -{w} да всё не так блять!"
    nvl clear
    nvlvas "Чё?"
    nvlvas "Скажи,{w=0.2} чё тебе не нравится на этот раз?"
    nvl clear
    nvlbazar "Василисе не нашлось,{w=0.2} что и сказать."
    nvlbazar "Остаток пути они молча ненавидели друг друга."
    nvl clear
    scene labaext with ed_lap
    nvlbazar "Под утро они таки дошли до офиса."
    nvlbazar "Недолго поколебавшись,{w=0.2} Иветта зашла внутрь."
    nvl clear
    play sound door_open
    scene ineony with ed_lap
    nn "Здравия."
    nn "Чем обязан?"
    ivt1 "Есть проблема." with vpunch
    ivt1 "Вы единственный,{w=0.2} кто может её решить."
    nn "И что за проблема такая?"
    "Неоня немного удивился."
    "Самую малость."
    "Но ему льстил подобный базар."
    ivt1 "Нам нужно разделиться." with vpunch
    nn "Нам?"
    nn "Это кому конкретно?"
    ivt1 "Мне."
    vas "И Мне."
    nn "Понятно."
    nn "Собираетесь лечить раздвоение личности нестандартными методами?"
    ivt1 "Именно." with vpunch
    ivt1 "Нам бы тела отдельные."
    vas "И Мне бы память подтереть."
    vas "Знать её не хочу нахуй."
    nn "У меня есть идея как вам помочь."
    nn "Но взамен вы на меня поработаете." with vpunch
    vas "И что надо сделать?"
    nn "После процедуры обсудим."
    "Василиса понимала,{w=0.2} что это говнистые такие условия,{w=0.2} ведь он может чё угодно попросить сделать."
    "И хуй потом ты от этого отвертишься."
    "Но всё уже было решено."
    vas "Хорошо."
    "И они пошли в процедурную."
    stop music fadeout 8
    scene laba
    show kazahspr
    with ed_lap
    nn "Может немного подташнивать после процесса."
    nn "Но это стандартный постэффект."
    nn "Ложись в эту колбу -{w} остальное я сделаю сам."
    "Они легли в колбу странного зеленоватого цвета."
    scene black
    $ renpy.movie_cutscene('source/videosos/cloncrate.webm')
    play music ly fadein 5
    $ MND_Chapter("Некоторое время спустя...")
    scene laba with ed_lap
    "Неоня сидел и ждал результат."
    "Это был его первый подобный эксперимент."
    "От его исхода зависит многое."
    "Если успех -{w} он теперь может содавать клонов людей и разделять автономные личности."
    "Энергии на это,{w=0.2} конечно,{w=0.2} масса уходит."
    "Но в запасе было её дохера."
    "А если же фейл..." with hpunch
    "То,{w=0.2} выходит,{w=0.2} он загубил человека."
    "Будем честны -{w} похуй на человека." with hpunch
    "Главное -{w} результат."
    "Стенка колбы начала отъезжать."
    window hide
    show vasilisa at center:
        xcenter -0.4 ycenter 0.5 rotate 0
        easein 0.4 xcenter 0.5 rotate 360
        ease 0.05 zoom 1.3
        ease 0.05 zoom 1.0
        ease 0.1 rotate -360
    $ renpy.pause (0.5)
    hide vasilisa
    show vasilisa
    window show
    "Из колбы в знакомой манере вылетел итог эксперимента."
    vas "Получилось!" with hpunch
    vas "Что теперь надо сделать?"
    nn "Поднимись обратно в мой кабинет и жди меня там."
    nn "Чуть позже дам тебе указания."
    vas "Только вот проблема есть{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Я ничего не помню." with hpunch
    "Чёрт."
    "Не всё прошло гладко."
    "Хотя -{w} так даже лучше."
    "Можно будет любой лапши на уши навешать.{w} Доширак."
    window hide
    play sound door_open
    hide vasilisa
    show vasilisa:
        subpixel True default
        parallel:
            Null(750.0, 720.0)
            'vasilisa'
        parallel:
            xpos 0.5
            linear 0.60 xpos 2.75
    with Pause(0.70)
    show vasilisa:
        xpos 2.75
    window show
    "Василиса покинула процедурную."
    "И через пару минут открылась вторая колба."
    window hide
    show ivettaspr at center:
        xcenter -0.4 ycenter 0.5 rotate 0
        easein 0.4 xcenter 0.5 rotate 360
        ease 0.05 zoom 1.3
        ease 0.05 zoom 1.0
        ease 0.1 rotate -360
    $ renpy.pause (0.5)
    hide ivettaspr
    show ivettaspr
    window show
    ivt1 "Получилось!" with hpunch
    "Не разделяя радости Иветты,{w=0.2} Неоня спросил:"
    nn "Помнишь что-нибудь?" with hpunch
    ivt1 "А я должна была что-{w=0.2}то забыть?"
    ivt1 "Где Василиса кстати?" with hpunch
    "Чёрт."
    "А эта -{w} всё помнит."
    "Где-{w=0.2}то я подобосрался в расчётах{w=0.2}.{w=0.2}.{w=0.2}."
    "Думал Дамирка."
    "Ну ничего."
    "Ещё есть время и ресурсы,{w=0.2} дабы это исправить."
    ivt1 "Дружище,{w=0.2} ты плохо понял?" with hpunch
    ivt1 "Где Василиса?" with hpunch
    "Неоня вышел из раздумий."
    "Эта ведёт себя очень агрессивно."
    "Она точно провалит задание."
    "Хотя попробовать стоит."
    nn "Ты должна{w=0.2}.{w=0.2}.{w=0.2}.{nw}"
    ivt1 "Ты ща пиздов получишь,{w=0.2} если не дашь мне инфу." with hpunch
    ivt1 "Я в последний раз спрашиваю:{w} где Василиса?" with hpunch
    "Неоня понял,{w=0.2} что пора прекращать баловаться."
    "Нужно порешить этот вопрос,{w=0.2} пока он не встал боком."
    window hide
    play sound shpricz
    pause 1
    hide ivettaspr
    show ivettaspr:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    play sound sfx_body_bump
    nn "Вот и всё."
    "Неоня резким движением опустошил шприц с мощным транквилизатором в шею Иветты."
    "После чего та заснула безмятежным сном."
    nn "Осталось её только в бункер оттащить."
    nn "Там она не доставит мне неприятностей."
    "И Неоня потащил Иветту в бункер."
    play sound stmetal
    scene kk with ed_lap
    "Неоня положил Иветту на кровать."
    nn "Сладких снов." with hpunch
    "После чего покинул бункер,{w=0.2} да отправился в свой кабинет,{w=0.2} дабы вешать доширак на уши Василисе."
    stop music fadeout 5
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Вечного:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    scene domint with ed_earth_draw
    "Пока Вечный читал эти ахуительные истории,{w=0.2} уже наступило утро."
    vchn "Ну и что это блять?"
    play music theorem
    vas "Тебе действительно так интересно?" with vpunch
    "И тут Вечный ахуел."
    "Немного сильно так."
    "Надо было хоть местами по сторонам поглядвать."
    vchn "Ладно,{w=0.2} признаю -{w} немного увлёкся."
    vchn "Но это не отменяет того,{w=0.2} что ты бесконечно всё скрываешь." with hpunch
    vas "Я хотела рассказать."
    vas "Просто сейчас не самое подходящее время."
    vchn "Неподходящее время{w=0.2}.{w=0.2}.{w=0.2}.{w} Ха."
    vchn "А когда подходящее{w=0.2}-то?" with hpunch
    vchn "Или ты снова пытаешься выкрутиться?!" with vpunch
    "Вечный наконец решил развернуться."
    scene domint
    show vasilisa
    with pushleft
    vchn "А,{w=0.2} БЛЯТЬ?" with vpunch
    "Ему уже похуй стало -{w} разбудит он Скита или нет."
    "Нужны были ответы."
    "И он их получит."
    "Часть уже получил."
    "Это из разряда той правды,{w=0.2} которую хочется закопать обратно."
    "Она грохнулся трёх типов,{w=0.2} двух мусаров,{w=0.2} после чего сбежала."
    "Это же просто пиздец,{w=0.2} разве нет?"
    vas "Спокойнее." with hpunch
    vas "Дабы её вытащить из рук айгандона,{w=0.2} мне нужно выполнить задание."
    vas "И мы обе станем свободны."
    vchn "И что же за задание?"
    vas "Убить Скитецкого." with vpunch
    window hide
    play sound reaction_joke_1
    pause 3
    vchn "И ты собираешься его грохнуть?"
    window hide
    play sound rld
    skt "Кого убить?" with vpunch
    vchn "Бля,{w=0.2} Димас,{w=0.2} я тут точно не причём!"
    "Начал оправдываться Вечный."
    skt "Не верю я что{w=0.2}-то тебе."
    stop music fadeout 4
    vas "Убери ствол." with hpunch
    vas "Иначе разговора не будет."
    "Было начала Василиса."
    "Накал страстей почти достиг своего апогея."
    "Если бы не финальный штрих."
    window hide
    play music digsig
    play sound door_break
    show ivettaspr:
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'ivettaspr'
        parallel:
            xpos 3.0
            linear 0.80 xpos 0.25
    with Pause(0.90)
    show ivettaspr:
        xpos 0.25
    window show
    ivt1 "ЗДАРОВА,{w=0.2} ЕБАНЬКО!" with vpunch
    ivt1 "СКОЛЬКО ЛЕТ,{w=0.2} СКОЛЬКО ЗИМ!" with vpunch
    "В дом залетела Иветта."
    "С диглом в руке."
    window hide
    play sound nday
    pause 3
    "Взяв за шею Василису,{w=0.2} она уже было начала выцеливать голову Скита."
    vchn "СТОЙ,{w=0.2} БЛЯ{nw}" with vpunch
    window hide
    stop music
    play music zp2main
    play sound introshoot
    pause 7
    play sound popalisempai
    scene black with ed_flash_red
    play sound2 door_break
    pause 1
    scene domint
    show unblink
    skt "Плечо,{w=0.2} сука{w=0.2}.{w=0.2}.{w=0.2}." with hpunch
    "Вечный понял,{w=0.2} что маслина была не для него."
    "Хотя в глазах всё равно потемнело."
    scene domintpov
    show skitpiohit
    with pushright
    "Вечный развернулся и увидел подстреленного Скита."
    "Свой травматический Макаров он выронил при попадании."
    "Вечный оккуратно носком ботинка отодвинул его подальше."
    skt "Чё стоишь,{w=0.2} неси ибупрофен блять!" with hpunch
    vchn "И где он?"
    skt "В ящике на кухне.{w} Слева сверху."
    "И Вечный погнал искать обезбаливающее."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Неони:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    scene laba
    show deadlylxrd
    with ed_lap
    nn "Братиш,{w=0.2} у нас проблемы." with hpunch
    lxrd "Что за проблемы?"
    nn "Иветта сбежала." with vpunch
    lxrd "Та,{w=0.2} которая маньячка?"
    nn "Да." with vpunch
    lxrd "Пиздец."
    lxrd "Чё делать?"
    nn "Я думаю,{w=0.2} можно забить хуй."
    nn "Они для нас опасности не представляют."
    nn "Ты кста мой дигл именной не видел?"
    lxrd "Кхм." with vpunch
    lxrd "Я могу только предположить,{w=0.2} где он теперь."
    nn "Блять."
    nn "А вот это уже опасно."
    lxrd "Ладно,{w=0.2} что{w=0.2}-нибудь придумаем потом."
    lxrd "Я связался с той самой {b}<<Тёмной лошадкой>>{/b}."
    nn "И чё,{w=0.2} как?"
    lxrd "Да никак." with hpunch
    lxrd "Он отложил встречу."
    lxrd "Ща дела у него какие{w=0.2}-то важные."
    nn "Понятно."
    nn "Продинамили тебя,{w=0.2} Вадимка." with hpunch
    nn "Причём уже который раз."
    lxrd "На следующий точно всё получится."
    lxrd "Ну а пока я займусь обустройством жилого комплекса нашего."
    lxrd "Там нужно пару штрихов добавить и можно жить."
    nn "Ты про 4 бункера с койками?"
    lxrd "Их там вроде больше."
    lxrd "Но я не помню,{w=0.2} на самом деле."
    lxrd "А так -{w} да,{w=0.2} я про этот комплекс."
    lxrd "Может быть,{w=0.2} я даже приглашу к нам ещё пару стоящих типов."
    lxrd "Сотрудников много не бывает."
    nn "Ну хорошо."
    nn "Как закончишь -{w} дай знать."
    lxrd "Добро."
    window hide
    play sound door_open
    hide deadlylxrd
    show deadlylxrd:
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos 0.5
            linear 0.80 xpos 1.25
    with Pause(0.90)
    show deadlylxrd:
        xpos 1.25
    window show
    "И Вадимка отправился чистить закрома вилкой."
    "А Неоня остался думать."
    nn "Иветта сбежала{w=0.2}.{w=0.2}.{w=0.2}."
    nn "Чё делать{w=0.2}-то бля теперь?" with hpunch
    stop music fadeout 4
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("Конец четвёртого картера...")
    scene black with ed_night_dis
    jump carter5
