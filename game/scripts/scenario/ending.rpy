label carter_ending:
    stop music fadeout 3
    stop sound fadeout 3
    window hide
    scene black with ed_night_dis
    pause 1
    play music adelaida fadein 1
    scene novoshahtinsk at sr_pokachivanie_light
    show lepestki_krutyatsa
    with ed_night_dis
    nvl clear
    nvlbazar "Наступили первые дни осени 2022 года."
    nvlbazar "Начались долгожданные перемени в жизни каждого участника этой истории."
    nvlbazar "После килла Скитового жизнь в Новошахтинске наконец-то стала спокойной."
    nvlbazar "Больше никого не заставляют шить банана ром и легион."
    nvlbazar "Армия из клонов доберманки так же была повержена."
    nvlbazar "Больше жителей львовского переулка не будет беспокоить ночью вой на луну."
    nvl clear
    window hide
    scene ext_clubs_day at sr_pokachivanie_light
    show lepestki_krutyatsa
    show deadlylxrd
    with ed_night_dis
    nvlbazar "Компания Skeet Dynasty перенесла свой главный офис из подвала в Новошахтинске в параллельный мир пионерлагеря."
    nvlbazar "Он был уже обжитой локацией, на которой было всё необходимое."
    nvlbazar "Перенос обородования по клонированию малолеток организовал Deadlylxrd а.к.а. Вадимус."
    nvlbazar "Со временем он ушёл от скама и осков и стал примерным заводчанином."
    nvlbazar "В 2024 году он стал примерным семьянином и на этот раз окончательно покинул Skeet Dynasty."
    nvl clear
    window hide
    scene buhaem
    with ed_night_dis
    nvlbazar "Колд после финальной пьянки решил таки податься в спорт."
    nvlbazar "Он занимался спортивной стрельбой."
    nvlbazar "После череды успехов он закончил карьеру и стал кайфовать на заработанные бабосы."
    nvlbazar "Взял себе пентхаус в подмосковье и отдыхал от мирской суеты."
    nvlbazar "Устроился ахуенно."
    nvl clear
    window hide
    scene ineony
    with ed_night_dis
    nvlbazar "Неоня смог найти инвесторов для своей компании."
    nvlbazar "Дела у него складывались просто ахуенно."
    nvlbazar "Вместо клонов он начал делать человекоподобных андроидов, что устроят революцию в Новошахтинске в 2038 году."
    nvlbazar "Но это потом."
    nvlbazar "Сейчас его компания только набирает обороты."
    window hide
    nvl clear
    scene vchn_vas
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with ed_night_dis
    nvlbazar "Василиса после всей этой истории уже окончательно законнектилась с Вечным."
    nvlbazar "Её альтер-эго в виде Иветты оставило их в покое."
    nvlbazar "Она начала потихоньку перевоплощаться из джокерши в няшную вафлежуйку."
    nvlbazar "Перебралась в хату к Вечному."
    nvlbazar "Жизнь начала налаживаться."
    nvl clear
    scene sz2 at sr_pokachivanie_light
    show lepestki_krutyatsa
    show mikola at right
    with ed_night_dis
    nvlbazar "А что же Вечный?"
    nvlbazar "Он отправился в свой родной мухосранск и начал профессионально заниматься кодингом."
    nvlbazar "Не сказать, что всё давалось легко..."
    nvlbazar "Просто нужно было начать. Дальше дело уже само пошло."
    nvlbazar "Он часто вспоминал лето 2022 года... Его конкретные события."
    nvlbazar "Вся эта история со Скитом капитально на него повлияла."
    nvlbazar "Он начал меняться в лучшую сторону."
    nvlbazar "И достигать небывалых высот."
    scene sz5 with linearblurbolee
    nvl clear
    nvlbazar "Он стал мастером ренхуйни, да взял с собой кента, с которым они сделали мод, который уронил реддит."
    nvlbazar "Просмотры прохождения мода на ютубе начали набирать нормальные (как для такого контента) просмотры."
    nvlbazar "Эти двое стали известными."
    nvl clear
    nvlbazar "В один осенний вечер Вечный просто стоял на балконе и дул Aegis Nano."
    nvlbazar "В его голову закралась одна ахутельная навязчивая идея."
    nvlbazar "В этот момент к нему подошла Василиса."
    show vasilisa at right
    with linearblur
    nvl clear
    vchn "Я хочу увековечить эту историю."
    vchn "Хоть это всё и слишком уж сюрреалистично..."
    vas "Да и похуй." with vpunch
    vas "Ты и без меня знаешь, что делать."
    vas "Остальное не важно."
    vas "Правда?"
    vchn "Правда." with vpunch
    nvl clear
    nvlbazar "Нам предоставляют выбор, к счастью и сожалению"
    nvlbazar "Липовое либо-либо удовлетворило временно"
    nvlbazar "Они примут всхлипывая то что им отмерено"
    nvlbazar "И Аделаида их не манит берегом"
    nvlbazar "А мы выбираем вкалывать поднимаясь с малого"
    nvlbazar "Пока под ногами не земная гладь, а палуба"
    nvlbazar "Принимая много, но не забывая главного"
    nvl clear
    scene mogila with linearblur
    nvlbazar "Засыпая снова и все начиная заново"
    nvlbazar "Плавно проплываем новостройки на востоке"
    nvlbazar "Наши легкие настолько переполнены восторгом"
    nvlbazar "Что вся эта игра нам просто кажется настольной"
    nvlbazar "Но мы знаем: она скроет за собой еще историй"
    nvlbazar "И нам будет, что вспомнить..."
    nvl clear
    window hide
    stop music fadeout 11
    if not persistent.achivka3:
        $ persistent.achivka3 = True
    play sound ach_sound
    show achiv3 at ed_get_achievement
    pause 7
    scene black with Dissolve(4)
    play music wapdomik_song
    $ MND_Chapter("Skitetsky REMASTER", time=3.25)
    $ MND_Chapter("Skitetsky REMASTER", time=3.25)

    $ MND_Chapter("Твоё путешевствие окончено", time=3.25)
    $ MND_Chapter("Твоё путешевствие окончено", time=3.25)

    $ MND_Chapter("Тебе хоть понравилось?", time=3.45)

    scene novoshahtinsk at sr_pokachivanie_light
    show lepestki_krutyatsa
    show zatemnenie
    with linearblurbolee

    show sr_logo:
        xalign 0.5
        ypos 1.05
        linear 100.0 ypos -6.28
    show credits sr_credits:
        xalign 0.5
        ypos 1.05
        linear 100.0 ypos -6.28
    $ renpy.pause (45, hard=True)

    stop music fadeout 3
    scene black with dissolve2
    pause 1
    return

label carter_ending_bad:
    stop music fadeout 3
    stop sound fadeout 3
    window hide
    scene black with ed_night_dis
    pause 1
    play music mf_e fadein 1
    scene sz3
    show piluka_fb
    with ed_night_dis
    nvl clear
    nvlbazar "Вечер. Компьютерный стол. Открытый клиент телеграмма. Клубы пара играючи заграждают мне обзор."
    nvlbazar "Который по счёту день я уже так провёл? Интересно…"
    nvlbazar "Последние полгода затяжной депрессии дают о себе знать."
    nvlbazar "Самое интересное, что я сам же всё и проебал. В одночасье."
    nvl clear
    scene novoshahtinsk
    show skitpiopivo
    show piluka_fb
    with ed_night_dis
    nvlbazar "Скит всё так же остался на своём месте в Новошахтинске. Неоня напару с Морозычем так и не смогли ничего ему противопоставить."
    nvlbazar "Колонна клонов Морозки была разбита клонами рыжей тян, что сделал Скитовский в своей лабаратории."
    nvlbazar "Остальные побратимы просто разбежались и покинули Новошахтинск."
    nvlbazar "Неоня и Колд были убиты доберманкой возле так и не упавшего забора Скитецкого."
    nvlbazar "Skeet Dynasty прекратила своё существование. Но Вадимка смог сбежать."
    nvlbazar "Дальнейшая его судьба неизвестна. Возможно, он таки смог вернуть жизнь в прошлое русло. Хотя… Скорее всего – просто смог совершить реинкарнацию. Мне это знать не дано."
    nvl clear
    scene nmallint
    show pchr
    with dreamyzoom
    nvlbazar "Команда Legendary прекратила своё существование под эгидой осков Сезамчика. Больше они не соберутся в тг для теста новой сборки пискель экспириенс."
    nvlbazar "Они ушли от прошивкостроения и занялись каждый своим делом."
    nvlbazar "Император всё так же работал на государство и получил повышение."
    nvlbazar "Чиконя стал главным инженером в крупной айти компании."
    nvlbazar "Шелбик всё так же дует бланты и занимается установкой пиратского ПО по квартирам в Самаре."
    nvlbazar "Судьба Ламени неизвестна."
    nvl clear
    scene vasdead
    with dreamyzoom
    nvlbazar "Рыжая тян совершила РКН после проёба со Скитом."
    nvlbazar "Вечный не перезвонил. Дальнейшее существование без него она просто не видела."
    nvlbazar "Лезвие бритвы совершило крупный надрез вдоль вены… Потом была изрезана артерия…"
    nvlbazar "Смерть была быстрой. Возможно даже безболезненной."
    nvl clear
    scene bergenokno
    show snezhok
    show bergenokno1
    with dreamyzoom
    nvlbazar "А что же Вечный? Он впал в серьёзную депрессию."
    nvlbazar "От него отвернулись все бывшие товарщи."
    nvlbazar "Женёк, который резво стал наносеком, после того как отошёл от дел."
    nvlbazar "Сексинос, который переехал в Питер и стал гуру по ремонту калозвонов разной степени ушатанности. Он нашёл своё призвание. Сделал хобби своей работой. Сейчас живёт в прибрежном районе СПБ."
    nvlbazar "Вечный думал покинуть город после массированных атак со стороны рейха."
    nvlbazar "Но что-то ему мешало."
    nvl clear
    scene vishel1
    with dreamyzoom
    nvlbazar "17 этажей - это достаточно высоко. Бетон внизу не добавлял вероятности выжить."
    nvlbazar "Легендарный белый куртец обдувал холодный влажный ветер."
    nvlbazar "Настроения не было. Ничего не было."
    nvlbazar "Было лишь осознание тотального проёба."
    nvl clear
    nvlvchn "Где-то я оступился… Сделал неправильный выбор."
    nvlvchn "И в один момент всё потерял."
    nvlbazar "Больше не будет осков Скита в тг."
    nvlbazar "Больше не будет прогулок за асканией и булками с ленты."
    nvlbazar "Больше не подогреются в микроволновке острые чебупенисы."
    nvlbazar "Больше не прошьётся 9т на новый репак миуи."
    nvlbazar "Больше не будет пройдён ни один мод на сталкер."
    nvlbazar "Больше не будет ренхуйни."
    nvl clear
    nvlvchn "Это конец. Всё началось с любопытства."
    nvl clear
    nvlbazar "Во время падения он ничего не чувствовал. Даже ничего не подумал."
    nvlbazar "Лежащий внизу кирпич стал камнем преткновения."
    nvlbazar "Боли не было. Ничего не было."
    nvlbazar "На этом эта история действительно заканчивается."
    nvlbazar "Больше ничего не будет."
    show blink
    nvlbazar "Занавес."
    nvl clear
    window hide

    if not persistent.achivka5:
        $ persistent.achivka5 = True
    play sound ach_sound
    show achiv5 at ed_get_achievement
    pause 7

    show sr_logo:
        xalign 0.5
        ypos 1.05
        linear 100.0 ypos -6.28
    show credits sr_credits:
        xalign 0.5
        ypos 1.05
        linear 100.0 ypos -6.28
    $ renpy.pause (45, hard=True)

    stop music fadeout 3
    scene black with dissolve2
    pause 1
    return