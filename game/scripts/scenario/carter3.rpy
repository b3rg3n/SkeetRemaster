label carter3:
    $ pps = 13
    play music lasttrack fadein 5
    scene ineony
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with Fade(1.5, 1, 2)
    show zatemnenie with dissolve2
    $ MND_Chapter("The Carter Three:")
    $ MND_Chapter("iNeoony's Revenge")
    hide zatemnenie with dissolve2
    nvlbazar "Неоня сидел за своим столом."
    nvlbazar "С той самой пьянки в Курске прошёл год."
    nvlbazar "Все начали заниматься своими делами."
    nvl clear
    nvlbazar "Вадимка начал хакерить и законтачился с одним интересным типом."
    nvlbazar "Колд занимался поиском подсосов Скитецкого и последующей карой."
    nvlbazar "Неоня открыл свою личную лабораторию {b}iGandone Labs{/b}."
    nvlbazar "А Вечный пропал с радаров."
    nvl clear
    nvlbazar "Да,{w=0.2} он просто исчез."
    nvlbazar "Либо же не выходил на связь."
    nvlbazar "Пускай об этом и очень быстро забыли."
    nvlbazar "Слишком быстро.{w} Буд то и не было его вовсе."
    nvl clear
    nvlbazar "Тем не менее -{w} Неоня вызвал всех лучших сотрудников на совещание."
    nvlbazar "Всё это по поводу презентации своего нового,{w=0.2} совершенного,{w=0.2} да и просто пиздатого вида вооружения."
    nvlbazar "А что же за оружие?{w} А это мы сейчас и узнаем."
    nvl clear
    scene laba with ed_night_dis
    "Неоня стоял в подземке с колбами."
    "Там и храниться всё,{w=0.2} что {b}запрещено Женевской конвенцией{/b}."
    window hide
    pause 1
    "В помещение зашёл Вадимка."
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
    lxrd "Здарова.{w} Чё там у тебя?"
    nn "Где Колд?" with vpunch
    lxrd "Скоро будет."
    nn "Ну,{w=0.2} как будет -{w} так и посмотрим.{w} Чё там у меня."
    nn "Добро?"
    lxrd "Темнишь ты что-то{w=0.2}.{w=0.2}.{w=0.2}."
    nn "Да неужели?" with vpunch
    nn "Я просто хочу увидеть вашу реакцию."
    nn "Сразу обоих."
    nn "И всё." with vpunch
    lxrd "Ну и что?"
    lxrd "Неужели там настолько экстраординарное что-то?" with vpunch
    nn "Скоро увидишь."
    "В помещение зашёл колд."
    play sound door_open
    show coldspr:
        subpixel True default
        parallel:
            Null(508.0, 733.0)
            'coldspr'
        parallel:
            xpos -3.0
            linear 0.80 xpos 0.25
    with Pause(0.90)
    show coldspr:
        xpos 0.25
    cld "Всем шалом.{w} Так чё там у тебя?"
    "Неоня колебался."
    "Он не хотел до последнего раскрывать все карты."
    "Но ему рано или поздно пришлось бы это сделать."
    nn "Новое оружие против Скитецкого."
    nn "Клоны." with vpunch
    "Стенка колбы начала съезжать."
    "Там лежало тело{w=0.2}.{w=0.2}.{w=0.2}.{w} Вадима Морозова?"
    lxrd "Это{w=0.2}.{w=0.2}.{w=0.2}.{w} Блять{w=0.2}.{w=0.2}.{w=0.2}.{w} Как?!" with vpunch
    "Тело начало приходить в себя,{w=0.2} выпадая из стадии анабиоза."
    window hide
    show lordsprclon1 at center:
        xcenter -0.4 ycenter 0.5 rotate 0
        easein 0.4 xcenter 0.5 rotate 360
        ease 0.05 zoom 1.3
        ease 0.05 zoom 1.0
        ease 0.1 rotate -360
    $ renpy.pause (0.5)
    window show
    "Из колбы вышел... {w}Прошу прощения.{w} В лабу,{w=0.2} ебанув тройное сальто,{w=0.2} завалился клон Вадима Морозова."
    window hide
    hide lordsprclon1
    hide coldspr
    show coldspr:
        subpixel True
        xpos 0.25
        linear 0.56 xpos 0.3
    show lordsprclon1:
        subpixel True default
        parallel:
            Null(499.0, 842.0)
            'lordsprclon1'
        parallel:
            xpos 0.5
            linear 0.56 xpos 0.25
    with Pause(0.66)
    show coldspr:
        xpos 0.3
    show lordsprclon1:
        xpos 0.25
    window show
    lxrd1 "Я курю,{w=0.2} буд то нечего терять мне!" with vpunch
    window hide
    play sound ssmeh2
    hide coldspr
    show coldherovo
    pause 4
    window show
    hide coldherovo
    show coldspr
    "Колд с этой лысой двухметровой хиппарской хуеты поймал некислую смешинку."
    "А вот Вадимка негодовал."
    lxrd "Слышь{w=0.2}.{w=0.2}.{w=0.2}."
    lxrd "Казах,{w=0.2} сука." with vpunch
    lxrd "Это чё такое,{w=0.2} придурок?" with vpunch
    stop music fadeout 5
    "Неоня усмехнулся."
    "Неоднозначная реакция его сотрудников была ему очевидна с самого начала."
    "Он упивался моментом,{w=0.2} ведь удивить Вадима Морозова нельзя уже давно."
    "А у Неони получилось."
    "Пусть он и потратил на это целый год."
    play music dumaet
    window hide
    scene black with ed_night_dis
    window show
    "Дамирка снова ушёл в свои воспоминания."
    window hide
    scene skitserun with ed_night_dis
    window show
    "В свои золотые мгновения жизни он сидел на крыше одного из домов."
    "Приглядевшись,{w=0.2} он увидел нечто странное."
    window hide
    play sound dostal
    show skitserun1:
        subpixel True default
        parallel:
            Null(473.0, 712.0)
            'skitserun1' with dissolve
        parallel:
            ypos 2.0
            linear 0.80 ypos 1.0
    with Pause(0.90)
    show skitserun1:
        ypos 1.0
    window show
    "Взяв свой {b}Nikon{/b},{w=0.2} он начал приближать изображение на экране камеры."
    "Немного сильно так ахуев от увиденного,{w=0.2} Неоня моргнул шоколадным глазом."
    window hide
    show blink
    pause 1
    hide blink
    scene vladik-serun2
    show unblink
    pause 1
    window show
    stop music fadeout 5
    "Там,{w=0.2} на конце крана,{w=0.2} всего лишь срал какой-то рандомный чел."
    "С кем не бывает,{w=0.2} казалось бы."
    play sound fb
    scene laba
    show lordsprclon1 at left
    show coldspr
    show deadlylxrd at right
    with flash
    play music goloederevo fadein 2
    "Но щелбан Вадима Морозова вернул его в реальность."
    lxrd "Уснул что ли?" with vpunch
    nn "Нет."
    nn "Просто вспомнил былое."
    nn "Старых друзей,{w=0.2} так сказать{w=0.2}.{w=0.2}.{w=0.2}."
    lxrd1 "Предай нахуй всех друзей,{w=0.2} ведь уже всё равно{w=0.2}.{w=0.2}.{w=0.2}."
    play sound zubek
    hide lordsprclon1
    show lordsprclon3 at left
    with flash
    "Клон Вадимки одарил всех своей ослепительной улыбкой."
    "Его ремень за 25к то и дело злорадно поблёскивал,{w=0.2} наровясь зажать яйца клона."
    "А Неоня снова усмехнулся."
    "Клону передались повадки Вадимки."
    "Та же способность подпёздывать цитатками Уаджета и покупать мегадорогие шмотки."
    "В этот момент Колд выходит из куража своих мыслей."
    "Он замечает лучезарную улыбку клона."
    "А Клон в этот момент решил подыграть."
    window hide
    play sound lacalut
    pause 3
    play sound ssmeh1
    hide coldspr
    show coldspr:
        subpixel True xpos 0.25 default
        parallel:
            Null(600.0, 720.0)
            'coldspr'
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
    show coldspr:
        xzoom 1 yzoom 1
    hide coldspr
    show coldspr:
        subpixel True xpos 0.25 default
        parallel:
            Null(600.0, 720.0)
            'coldspr'
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
    show coldspr:
        xzoom 1 yzoom 1
    pause 1.1
    hide coldspr
    show coldspr:
        subpixel True xpos 0.25 default
        parallel:
            Null(600.0, 720.0)
            'coldspr'
            0.01
            'coldspr'
        parallel:
            ypos 1.0 rotate 0.0
            linear 0.07 ypos 0.8 rotate 60.0
            linear 0.07 ypos 0.7 rotate 120.0
            linear 0.07 ypos 0.6 rotate 180.0
            linear 0.07 ypos 0.5 rotate 240.0
            linear 0.07 ypos 0.4 rotate 320.0
            linear 0.07 ypos 0.3 rotate 380.0
            linear 0.07 ypos 0.2 rotate 440.0
    with Pause(1.11)
    show coldspr:
        pos (0.25, 0.2) rotate 440.0
    pause 1.65
    hide coldspr
    "После чего Колд,{w=0.2} ебанув несколько сальтух разом,{w=0.2} улетает нахуй на луну."
    "Настолько сильным был его ор."
    lxrd "Он так долго ещё улетать с этого дела будет?"
    nn "Ты погоди."
    nn "Это ещё Вечный не видел."
    lxrd "А ты уверен,{w=0.2} что он увидит?"
    "Неоня задумался."
    "Если Вечный раскусил его схему по добыче ДНК для создания его клона..."
    "То хуй он больше сюда вернётся."
    "А что за схема?{w} Это мы сейчас и узнаем."
    stop music fadeout 5
    scene black with ed_night_dis
    scene ineony
    show vasilisa at right
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with ed_night_dis
    play music lovewooman fadein 2
    nn "Ты мой первый удачный клон."
    nn "Я скрупулёзно подбирал внешность."
    nn "Даже черты характера."
    nn "Ты должна{w=0.2}.{w=0.2}.{w=0.2}.{w} Нет,{w=0.2} блядь,{w=0.2} просто {b}ОБЯЗАНА{/b} ему понравится!"
    lis "И для чего же?"
    nn "Мне нужен его ДНК." with vpunch
    nn "Зная Вечного -{w} я уверен на все двести процентов,{w=0.2} что он не даст мне свой биоматериал."
    nn "Поэтому ты должна втереться в доверие и гопнуть это самое ДНК." with vpunch
    nn "Каким образом ты будешь это делать -{w} меня мало интересует."
    nn "Я дам тебе катетер с тоненькой иголкой."
    nn "Этого хватит более чем."
    nn "Остаётся надеяться,{w=0.2} что ты унаследовала от оригинала когнетивные способности и чуткость."
    nn "Иначе плакала моя затея."
    nn "Намёк понят?"
    lis "Понят."
    lis "Только один вопрос остался."
    lis "Какое имя мне взять?" with vpunch
    nn "Хм{w=0.2}.{w=0.2}.{w=0.2}."
    "Недолго думая,{w=0.2} Неоня выдал жидкий пёрл."
    nn "Будешь Василисой." with vpunch
    vas "Василиса так Василиса.{w} Чё бухтеть-то."
    nn "С твоим вопросом разобрались."
    nn "Есть ещё?"
    vas "Нет."
    vas "Приступаю к выполнению поставленной задачи."
    window hide
    play sound door_open
    hide vasilisa
    show vasilisa:
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'vasilisa'
        parallel:
            xpos 0.75
            linear 0.80 xpos 2.0
    with Pause(0.90)
    show vasilisa:
        xpos 2.0
    window show
    hide vasilisa
    "Клон покинул кабинет Неони."
    nn "Остаётся надеяться{w=0.2}.{w=0.2}.{w=0.2}.{w} Да."
    stop music fadeout 5
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Вечного:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music wmm fadein 2
    scene bergdomint1
    show vlados2
    with ed_night_dis
    nvl clear
    nvlbazar "Это должен был быть один самый обычный день.{w} Да как бы не так."
    nvlbazar "Всё началось дня за 2 до этого."
    nvlbazar "Именно тогда Вишневский предложил Вечному отправиться в нереальный рейв."
    nvl clear
    vsn "Почему бы тебе не прийти?"
    vsn "Тем более,{w=0.2} на моё др должен заскочить Максончик и компания."
    vchn "Тот самый негритос?"
    vsn "Да." with vpunch
    vsn "Он ахуенен."
    vchn "Да кто ж спорит."
    vchn "Просто желания куда-то идти нет абсолютно."
    vsn "Да неужели?" with vpunch
    vsn "Может быть такого шанса у тебя больше не будет."
    vsn "Сам подумай:{w} там будем не мы вдвоём."
    vsn "Будут тёлки!"
    vsn "Так из своей депрессии выйдешь когда-нибудь."
    vchn "Смешно{w=0.2}.{w=0.2}.{w=0.2}."
    vchn "Тут наоборот скорее."
    vchn "Хотя ёпта,{w=0.2} когда меня тёлки волновали?" with vpunch
    vchn "Сам вспомни пятый класс тот же,{w=0.2} когда меня прилюдно отшили!" with vpunch
    vchn "Да похуй мне было совершенно." with vpunch
    vsn "Мне нравится твой настрой."
    vsn "Тем более -{w=0.2} чем тебе не нравится идея отправиться на др кента?"
    vchn "Ну,{w=0.2} тоже верно."
    vsn "Кароче,{w=0.2} я буду ждать тебе через два дня в 4 вечера в клубаке на запольной."
    vsn "Не опаздывай."
    vsn "Будет расставлять алко и прибамбасы."
    vsn "Познакомлю тебя с Кирюхой."
    window hide
    hide vlados2
    play sound door_open
    show vlados2:
        subpixel True default
        parallel:
            Null(473.0, 712.0)
            'vlados2'
        parallel:
            yanchor 1.0
            linear 0.80 yanchor -2.0
    with Pause(0.90)
    show vlados2:
        yanchor -2.0
    hide vlados2
    stop music fadeout 5
    nvlbazar "На этой не особо весёлой ноте они распрощались."
    nvl clear
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("День X")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    scene tusa with ed_night_dis
    play music korabl fadein 2
    nvlbazar "Ради чего всё это? {w}- Думал Вечный, сидя недалеко от диджейского пульта."
    nvlbazar "Не сказать,{w=0.2} что его опасения подтвердились."
    nvlbazar "Просто пока что он не знает об этом."
    nvlbazar "Для него сейчас всё под контролем и всё ахуенно."
    nvlbazar "Ничего не предвещает беды,{w=0.2} так сказать."
    nvl clear
    nvlbazar "До одного момента."
    nvl clear
    nvlbazar "К нему на тусе подсаживается одна рыжеволосая тян{w=0.2}.{w=0.2}.{w=0.2}."
    nvl clear
    window hide
    show vasilisa:
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'vasilisa'
        parallel:
            xpos 3.0
            linear 0.80 xpos 0.75
    with Pause(0.90)
    show vasilisa:
        xpos 0.75
    window show
    "Вечный увидел до боли знакомое ебало."
    "Его настроение находилось слишком в очке, чтоб ещё вспоминать всё то, что было между ними до."
    "Поэтому он включил дурачка, да начал делать вид, типа её не знает."
    "Типа <<обижается>>."
    "Пусть почувствует себя важной."
    "Хоть и 2020 не вернуть."
    vas "Привет."
    vas "Ты тот самый Вечный?" with vpunch
    vchn "Допустим."
    "Вечный был не в самом хорошем настроении."
    vchn "Тебе надо что-то?"
    vas "Да." with vpunch
    vchn "И что же?"
    vas "Ты сидишь и унываешь."
    vas "Я собираюсь это исправить." with vpunch
    vas "Рассказывай."
    vas "Чё случилось?"
    vchn "Да ничего особенного." with vpunch
    vchn "Просто неприятно находиться в месте,{w=0.2} где я никого не знаю."
    vchn "Давит на мозги конкретно." with vpunch
    vchn "И чё с этим делать -{w} я не знаю."
    vchn "Вот так вот."
    vas "Понятно."
    vas "Ты просто мало приголубил." with vpunch
    vas "Пойдём,{w=0.2} там где-то был Джеймесон."
    window hide
    scene bar1
    show vasilisa at right
    with ed_lap
    nvlbazar "И они отправились к барной стойке."
    nvlbazar "Василиса в пьяном угаре пыталась открыть сок ножом."
    nvlbazar "По итогу она отхуячила пол пакета и сок начал разливаться на пол."
    nvlbazar "Вечный,{w=0.2} прям как истинный джентельмен,{w=0.2} кропотливо начал пытаться выхватить у неё сок,{w=0.2} пока она его не доразлила."
    nvl clear
    nvlbazar "По итогу она сделала ему свой фирменный коктейль -{w} казах в астане."
    nvlbazar "Что это?"
    nvl clear
    nvlbazar "Много Джеймесона и немного яблочного сока {b}<<Добрый>>{/b}."
    nvlbazar "Уносит с него не так сильно,{w=0.2} как с лысой малышки."
    nvlbazar "Иначе Вечный бы просто всё забыл."
    nvl clear
    nvlbazar "Тем не менее,{w=0.2} бахнув этого чудесного {b}<<морса>>{/b},{w=0.2} он осмелел."
    nvlbazar "Нихуёво так."
    nvlbazar "После чего они вернулись ближе к танцполу."
    nvl clear
    window hide
    scene tusa
    with ed_lap
    nvlbazar "Один из темнокожих кентов {b}Maxxyma{/b} заметил угашенного Вечного и затащил его на танцпол."
    nvlbazar "И когда врубили на диджейском пульте {b}народные песни республики Конго{/b},{w=0.2} Вечный ушёл в отрыв."
    nvl clear
    nvlbazar "Все проблемы и загоны отошли на второй план."
    nvlbazar "Он просто чувствовал себя прекрасно."
    nvlbazar "Позабыв о потере {b}Номера Третьего{/b},{w=0.2} о зачётах в шараге,{w=0.2} о уборке хаты и прочем говне,{w=0.2} Вечный узнал,{w=0.2} что есть настоящее счастье."
    nvl clear
    nvlbazar "Счастье для него -{w} не париться ни о чём."
    nvlbazar "Иметь людей вокруг себя."
    nvlbazar "Не чувствовать туманности завтрашнего дня."
    nvl clear
    nvlvhcn "Вот так надо отдыхать."
    nvlbazar "Думал про себя Вечный."
    nvl clear
    show vasilisa:
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'vasilisa'
        parallel:
            xpos 3.0
            linear 0.80 xpos 0.75
    with Pause(0.90)
    show vasilisa:
        xpos 0.75
    nvlbazar "Присев на пуфики перевести дыхание,{w=0.2} Вечный заметил Василису,{w=0.2} которая летела на всех парах к нему с бухлом."
    nvlbazar "Продолжая его спаивать,{w=0.2} она спрашивала наводящие вопросы."
    nvl clear
    vas "А у тебя девушка есть?" with vpunch
    "Вечный прихуел от своей удачи."
    vchn "Теперь нет." with vpunch
    "Немного резво ответил наш паря."
    "Всё таки градус не самый низкий залит внутри у него."
    vas "Не верится мне что-то." with vpunch
    vas "Ты ж не урод."
    vas "Не конченный."
    vas "Да даже не отбитый."
    vas "Брешешь небось?" with vpunch
    vchn "Нет."
    vchn "Просто я вечно кого-то чем-то не устраиваю."
    "Не соврал он."
    vas "Не заметила в тебе ничего такого."
    vchn "Значит,{w=0.2} все мои бывшие -{w} шмаромойки?"
    vas "Вот ты и ответил на вопрос,{w=0.2} который,{w=0.2} я уверена,{w=0.2} не давал тебе покоя."
    vchn "Хм."
    vchn "А ведь действительно." with vpunch
    stop music fadeout 4
    nvlbazar "За их разговором последовало включение трека {b}Enjoykinа <<Ламповая Няша>>{/b}."
    nvlbazar "Они просто наслаждались моментом и парили одноразку."
    nvl clear
    play music thatlife fadein 2
    nvlbazar "Не сказать,{w=0.2} что Василиса не начала что-то чувствовать."
    nvlbazar "Было что-то отдалённое,{w=0.2} из далёкого прошлого."
    nvlbazar "Ощущение давно забытое."
    nvlbazar "Как из прошлой жизни.{w} Которой не было."
    nvl clear
    nvlbazar "Пока Вечный завтыкал на исполняющего танец {b}Рикардо{/b} Максимку,{w=0.2} Василиса поняла,{w=0.2} что другого шанса не будет."
    nvlbazar "Она аккуратно извлекла катетер из подсумка,{w=0.2} прикреплённого к бедру и спрятанного под юбкой."
    nvlbazar "Почти добравшись до поясницы Вечного,{w=0.2} тот решил обернуться,{w=0.2} дабы поделиться впечатлениями от увиденного."
    nvlbazar "Василиса еле успела убрать катетер обратно."
    vchn "Чёта ты загрустила."
    vas "А?{w} Да не,{w=0.2} тебе показалось."
    "Она неумело натянула улыбку."
    vchn "Я же вижу,{w=0.2} что что-то не так."
    vas "Просто ты мне нравишься." with vpunch
    "Сумела выкрутиться,{w=0.2} ничего не сказать."
    "Только вот методы такие на Вечном просто не сработают."
    vchn "Да неужели?"
    "Он решил играть в дурака."
    vchn "Ты мне тоже." with vpunch
    vas "Правда?"
    vchn "Конечно."
    nvl clear
    nvlbazar "Парализованный разговор спас кент Максимки,{w=0.2} который вытянул обоих на танцпол."
    nvl clear
    nvlbazar "На медляке каждый из них думал о своём."
    nvl clear
    nvlvhcn "Кому она пиздит?"
    nvlvhcn "Не верю я в подобное."
    nvlvhcn "Она вообще меня впервые видит."
    nvl clear
    nvlvas "Надеюсь,{w=0.2} он не засёк ничего."
    nvlvas "Не успела подсумок застегнуть."
    nvlvas "Хоть бы не выпал{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvas "Хоть бы{w=0.2}.{w=0.2}.{w=0.2}."
    nvl clear
    nvlvas "Точно!"
    nvlvas "Есть вариант,{w=0.2} как гопнуть ДНК."
    nvlvas "Он мне его сам и отдаст."
    nvlvas "Буквально."
    vas "Слушай{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Пойдём отсюда,{w=0.2} а?" with vpunch
    vchn "А чё так?"
    "Хотя Вечный тоже был не против ливнуть."
    "Ему был интересен её мотив."
    vas "Мне тоже{w=0.2}.{w=0.2}.{w=0.2}.{w} Тяжко находится в подобных местах{w=0.2}.{w=0.2}.{w=0.2}."
    "Вечный из-за затуманенного разума не смог определить элементарное противоречие."
    "Её сюда никто не тащил.{w} В отличие от него."
    "Вечному просто было похуй.{w} И это стало его большо{w=0.2}о{w=0.2}ой ошибкой."
    vchn "Ну,{w=0.2} пошли."
    "Они отправились ко входу в помещение для уеденения."
    play sound door_break
    scene komnata_seksa at aw_master_tryas
    "Василиса проталкивает его в двери,{w=0.2} после чего,{w=0.2} имитируя порыв страсти,{w=0.2} ловко достаёт катетер и гопает ДНК Вечного из поясницы."
    vchn "Ай,{w=0.2} сука!" with vpunch
    "Вечный почувствовал лёгкий укол в поясницу."
    vchn "Неудачно приземлился,{w=0.2} однако."
    nvl clear
    nvlbazar "Он всё ещё туго соображал."
    nvlbazar "План Василисы был выполнен."
    nvlbazar "Почти.{w} Осталось отделаться от него и ливнуть."
    nvl clear
    nvlbazar "И шанс подвернулся."
    nvlbazar "Вечный пошёл в толкан."
    nvl clear
    scene vannaya with ed_lap
    nvlvhcn "Сука,{w=0.2} не идёт совершенно..."
    nvl clear
    nvlbazar "Из-за дымящего шишака напор вообще отсутствовал."
    nvlbazar "Он стоял там минут десять с {b}fat cockом{/b} в руке."
    nvlbazar "К нему даже пару раз типа залетали."
    nvlbazar "И сразу же улетали обратно."
    nvl clear
    nvlbazar "Вечный стоял с лицом,{w=0.2} полным недоумения.{w} В толчке.{w} С хуем в руке."
    nvlbazar "Со стороны странное зрелище."
    nvlbazar "Но ему было похуй."
    nvlbazar "Были проблемы и понасущнее."
    nvl clear
    scene tusa with ed_lap
    nvlbazar "С горем пополам поссав,{w=0.2} он возвращается обратно."
    nvl clear
    nvlbazar "В зале нигде не было Василисы."
    nvlbazar "Вечный взглядом замечает Вишневского."
    window hide
    show vlados2:
        subpixel True default
        parallel:
            Null(473.0, 712.0)
            'vlados2'
        parallel:
            ypos 2.0
            linear 0.80 ypos 1.0
    with Pause(0.90)
    show vlados2:
        ypos 1.0
    window show
    vchn "Юра!" with vpunch
    vsn "О,{w=0.2} Вечный!"
    vchn "Слушай,{w=0.2} ты не видел тут одну тяночку..."
    vsn "ООО!" with vpunch
    vsn "Поздравляю,{w=0.2} братиш!"
    stop music fadeout 5
    vchn "Да погоди ты."
    vchn "Рыжеволосую такую не видел?"
    "Вечный осознал,{w=0.2} что он даже её имени не спросил."
    th "Пиздец.{w} Полный."
    vsn "Была какая-то."
    vsn "Она спешно покинула это заведение." with vpunch
    window hide
    show rageone with ed_alpha_diss_fast
    play music redhead
    pause 1
    nvl clear
    nvlvhcn "Ебать я лошара."
    nvlvhcn "Это просто пиздец."
    nvlvhcn "Меня кинули?{w} Ха."
    nvlvhcn "Как буд-то ты ожидал чего-то другого?"
    nvlvhcn "Всё было очевидно с самого начала."
    nvl clear
    nvlvhcn "Не зря я не верил во все эти сказки."
    nvlvhcn "Не верил{w=0.2}.{w=0.2}.{w=0.2}.{w} Ха!"
    nvlvhcn "Оно и видно блять."
    nvlvhcn "Пиздец."
    vsn "Что с тобой?" with vpunch
    vsn "На тебе лица нет."
    vsn "Ты буд то призрака увидел."
    stop music fadeout 5
    vchn "Ничего особенного,{w=0.2} не бери в голову."
    hide rageone with ed_alpha_diss_fast
    nvl clear
    window hide
    hide vlados2
    show vlados2:
        subpixel True default
        parallel:
            Null(473.0, 712.0)
            'vlados2'
        parallel:
            yanchor 1.0
            linear 0.80 yanchor -2.0
    with Pause(0.90)
    show vlados2:
        yanchor -2.0
    hide vlados2
    pause 3
    play music idiot fadein 2
    nvlvhcn "Какой же я идиот{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvhcn "Мне тут делать больше нечего."
    nvl clear
    nvlbazar "Думал про себя Вечный,{w=0.2} попутно проверяя баланс."
    nvlbazar "Там были лишь полторы сотки."
    nvlbazar "Потом он чекнул яндекс такси,{w=0.2} где цена была 250."
    nvl clear
    nvlvhcn "Заебись."
    nvl clear
    nvlbazar "Но у него появилась идея."
    nvl clear
    nvlvhcn "Надеюсь,{w=0.2} ещё не забыли меня{w=0.2}.{w=0.2}.{w=0.2}."
    nvl clear
    nvlbazar "Он начал писать в свой заброшенный чат в телеграмме,{w=0.2} пингуя всех."
    nvl clear
    nvlvhcn "Бля посоны.{w} Киньте сотку,{w=0.2} по-братски.{w} На такси не хватает."
    nvl clear
    nvlbazar "Первым откликнулся Вадим Морозов."
    nvl clear
    nvllxrd "Здарова.{w} Где ты пропадаешь?{w} Сотку ща кину.{w} Номер карты дай."
    nvl clear
    nvlbazar "После того,{w=0.2} как Вадимка скинул Вечному сотку на сбербанк,{w=0.2} Вечный записал видеосос,{w=0.2} где танцевали негритосы."
    nvl clear
    nvllxrd "АХАХА!{w} Ебать ты там отжигаешь."
    nvl clear
    nvlvhcn "Я ливаю отсюда.{w} Заебало всё нахуй."
    nvl clear
    nvlbazar "И Вечный закрыл тг,{w=0.2} после чего заказал эконом."
    nvlbazar "Юра и негритосы проводили его в долгий путь домой."
    nvlbazar "Вечный прыгнул в Kia Rio и поехал домой."
    window hide
    scene black with ed_night_dis
    $ MND_Chapter("От лица Василисы:")
    scene tusaposle
    show doshd
    with ed_night_dis
    nvl clear
    nvlbazar "Василиса двигалась к автовокзалу,{w=0.2} который был недалеко от изначального места дислокации."
    nvlbazar "Попутно она размышляла о правильности совершенного поступка."
    nvl clear
    nvlvas "И зачем всё это?"
    nvlvas "Он явно не тот,{w=0.2} кого стоит так жестко наёбывать."
    nvlvas "Ебучий казах,{w=0.2} сука!"
    nvl clear
    nvlbazar "На её глазах начали появляться слёзы."
    nvl clear
    nvlvas "Оригинал бы точно не хотела себе такого клона{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvas "Жаль только,{w=0.2} что её больше нет в живых."
    nvlvas "И за что она полегла только?"
    nvlvas "Казах и за это ответит{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvas "А ты -{w} дура."
    nvlvas "Согласилась работать на идиота."
    nvlvas "Зачем только{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvas "Можно же было просто съебаться!"
    nvl clear
    nvlvas "Ладно."
    nvlvas "Всё равно собралась возвращаться."
    nvlvas "Надо потребовать у него свободу."
    nvlvas "Ему ничего не останется мне предоставить."
    nvl clear
    nvlvas "Так и сделаю."
    nvlvas "А сейчас{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvas "Меня ждёт рейс в Курган."
    stop music fadeout 5
    nvl clear
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("Через пару дней")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music raw
    scene ineony
    with ed_night_dis
    vas "Ты моральный урод." with vpunch
    vas "Для чего тебе это ебаное ДНК?" with vpunch
    nn "Ха."
    nn "Кто из нас урод ещё{w=0.2}.{w=0.2}.{w=0.2}.{w} Тем более моральный{w=0.2}.{w=0.2}.{w=0.2}."
    nn "Я-то в отличие от тебя никого не наёбывал." with vpunch
    vas "Всё из-за тебя{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Я отказываюсь работать на тебя." with vpunch
    vas "Всё кончено."
    vas "Можешь идти нахуй." with vpunch
    nn "Так уверена в себе?{w} Ахаха{w=0.2}.{w=0.2}.{w=0.2}."
    nn "Не забывай,{w=0.2} кто твой создатель."
    nn "Я заложил в тебя механизм отката."
    nn "Стоит мне сказать секретную комбинацию,{w=0.2} как ты полностью потеряешь самоконтроль." with vpunch
    vas "Ах ты{w=0.2}.{w=0.2}.{w=0.2}."
    nn "А теперь утирай сопли и пиздуй блять на новое задание."
    nn "Выбора у тебя всё равно нет."
    vas "И что на этот раз?"
    vas "Грабёж,{w=0.2} убийство,{w=0.2} изнасилование?" with vpunch
    nn "Каво?"
    vas "Никаво.{w} Чё тебе в этот раз надо?{w} Ускоглазая ты морда." with vpunch
    nn "Попроще будь.{w} Иначе пойдёшь по пути утилизации,{w=0.2} прям как отбраковка."
    nn "Чувства у неё появились,{w=0.2} видите ли.{w} Ха."
    nn "В общем.{w} Тебе нужно убрать одну нехорошую фигуру из нашей партии."
    nn "Его имя -"
    nn "Его имя -{fast} Дмитрий Скитецкий." with vpunch
    nn "Лысый такой."
    nn "В капюшоне постоянно ходит."
    nn "Как ты его нейтрализуешь -{w} уже твои проблемы."
    nn "Задача ясна?"
    "В ответ молчание."
    nn "ЯСНА,{w=0.2} БЛЯТЬ?!" with vpunch
    vas "да{w=0.2}.{w=0.2}.{w=0.2}."
    "Тихо проронила Василиса и покинула комплекс."
    scene labaext with ed_lap
    th3 "И чё мне с этим делать?"
    th3 "Ладно."
    th3 "Подумаю об этом позже."
    stop music fadeout 5
    th3 "А сейчас меня ждёт рейс в Новошахтинск."
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Димы:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music nightmare fadein 5
    scene nmall
    show doshd
    play ambience dviglo
    with ed_night_dis
    "Дмитрий ехал по Новошохтинску на своём некро-ведре."
    "Из хрипящих динамиков доносился до ушей старый добрый русский транс."
    "Движок десятки пердел,{w=0.2} хрипел,{w=0.2} умирал,{w=0.2} но,{w=0.2} сука,{w=0.2} работал."
    "Самое главное -{w=0.2} что ехал."
    "Иначе Димка бы ехал на маршрутке."
    "С бабками.{w} Которые не моются."
    "И тогда бы ему было пиздец как грустно."
    window hide
    pause 1
    "Куда он едет?"
    play sound herznaet
    window hide
    pause 1.6
    "Димка повернул в сторону своей trap хаты."
    "Как говориться -{w=0.2} навалил боком под плёнку на Лвовский переулок, 4."
    scene traphata
    show doshd
    with dissolve2
    window hide
    pause 1
    "Выглядит как бомжатник?" with vpunch
    "У{w=0.2}у{w=0.2}у{w=0.2},{w=0.2} это вы ещё внутри не были!"
    "Там вообще пиздец свалка нахуй."
    "Как говорит Димасек:"
    skt "Главное -{w=0.2} кто пахан.{w=0.2} Остальное не ебёт.{w=0.2} Если,{w=0.2} конечно,{w=0.2} ты не под шконкой))){w=0.2} гы"
    window hide
    pause 1
    scene domext
    play sound tazik1
    show doshd
    stop ambience fadeout 2
    "Дима припарковал свой тазик,{w=0.2} обклеенный аниме наклейками с зеро ту."
    play sound tazik2
    "Оставив тазик гнить под открытым небом,{w=0.2} Скит отправился домой."
    scene domint with dissolve2
    window hide
    pause 1
    "Зайдя, как полагается,{w=0.2} на хату,{w=0.2} Дерьмон начал думать{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Чем бы заняться сука?" with vpunch
    window hide
    pause 1
    "Димка решил поклацать свой пк."
    scene pc with ed_lap
    "Его комп на AMD Athlon 64 4000+ с 256 мб ддр1 еле тянул браузер."
    "А IDE хард на 40 гигов был забит файлами для прошивки на LegionOS."
    skt "ДА ЗАГРУЖАЙСЯ БЫСТРЕЕ,{w=0.2} СУКА!" with vpunch
    play sound udarklava
    "Скитолс распсиховался и въебал двоечку по клавиатуре ps/2."
    window hide
    pause 2
    skt "Может ссд исправит ситуацию?"
    window hide
    pause 1
    "Не долго думая,{w=0.2} Димка решил отправится в DNS в своём любимом тц Новошахтинск MALL."
    scene traphata
    show doshd
    with dissolve2
    window hide
    pause 1
    skt "Ща по фасту все сделаем."
    skt "Хули время терять."
    "И Димка поехал в тц."
    scene nmall
    show doshd
    with dissolve2
    "Димас припарковал свой тазик и вышел на улицу."
    scene novomall
    show doshd
    window hide
    pause 1
    skt "Бля там охранник сука." with vpunch
    scene propusk with dissolve2
    "Предъявив охране свой паспорт,{w=0.2} Дима отправился гулять по тц."
    scene nmallint with dissolve2
    window hide
    pause 3
    stop music fadeout 6
    "Походив по павильонам,{w=0.2} Димка таки купил ссд."
    "Это был Goldenfir на 120 гб."
    "Доместос отдал за него three hundred bucks."
    "Зато теперь его windows 98 будет загружаться очень быстро."
    window hide
    pause 1
    "У Димона проскочила шальная мысль пойти обоссать золотой ободок параши{w=0.2}.{w=0.2}.{w=0.2}."
    "И он решил совершить сие действие."
    "Золотые толчки {b}Новошахтинск MALL{/b}а начали трепетать."
    "Ведь туда идёт Дима."
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Василисы:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music wmm1 fadein 2
    scene train with ed_night_dis
    nvl clear
    nvlbazar "Поезд проехал Ростов и двигается прямо к Новошахтинску."
    nvlbazar "Василиса задумчиво смотрела в окно."
    nvl clear
    nvlvas "Пойти парашу обоссать?"
    nvl clear
    nvlbazar "После этой мысли у неё пошли странные ассоциации.{w} Как из прошлой жизни.{w} Которой не было."
    nvlbazar "Как к ней приходит какой-то старпёр с пельменем на голове и представляется сантехником {b}<<Личинус Турбо>>{/b}."
    nvlbazar "Он обирается почистить толчок вилкой,{w=0.2} но всё же у него этого не вышло,{w=0.2} после чего ему пришлось харкнуть и блять ебануть ногой."
    nvlbazar "После чего развалился толчок и он сбежал с криком {b}<<ИДИ НАХУЙ>>{/b}."
    nvl clear
    nvlvas "С чего такие мысли пошли,{w=0.2} интересно?"
    nvl clear
    nvlbazar "Впрочем,{w=0.2} это её мало заботило."
    nvl clear
    play sound door_open
    scene train2 with ed_lap
    "Василиса вышла в корридор."
    "Её не покидало плохое предчувствие."
    th3 "Может не стоит туда заходить?"
    th3 "Не так уж и сильно охота{w=0.2}.{w=0.2}.{w=0.2}."
    th3 "Хотя,{w=0.2} делать всё равно нехрен{w=0.2}.{w=0.2}.{w=0.2}."
    th3 "С Богом."
    "И она зашла в толкан поезда РЖД."
    window hide
    play sound door_break
    scene train3 with vpunch
    pause 0.5
    play sound chenado
    window hide
    pause 1.5
    "Открыв дверь ногой,{w=0.2} она,{w=0.2} мягко говоря,{w=0.2} ахуела."
    vas "Блять." with vpunch
    "В параше царил полный хаос."
    "По стенкам стекала малафья."
    "Запах стоял соответствующий."
    "А на параше,{w=0.2} как на троне,{w=0.2} сидел какой-то обезумевший дед."
    "Зрелище не из приятных."
    play sound door_break
    scene train2 with vpunch
    "Василиса поспешно ретировалась оттуда,{w=0.2} не проронив ни слова."
    "Ссать перехотелось капитально."
    scene train with ed_lap
    "Остаток поездки она провела в подвешанном состоянии."
    "Сдерживаться под конец было тяжко."
    "Но,{w=0.2} слава мэру Новошахтинска,{w=0.2} вокзал находился не за пределами города."
    scene novomallblya with ed_lap
    "В итоге Василиса вышла к тц {b}Новошахтинск MALL{/b}."
    "Выбора не было,{w=0.2} пришлось искать толкан там."
    play sound door_break
    scene nmallint with vpunch
    "Сбив с ног охранника,{w=0.2} она помчалась в рандомном направлении."
    "Не прогадала."
    "Толкан как раз находился в той стороне."
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Димы:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    scene tolkanmall with ed_night_dis
    window show
    "Димас стоял и играл своими {b}<<мускулами>>{/b} перед зеркалом."
    "Его ничто не могло отвлечь."
    window hide
    play sound nitroblya
    show vasilisa:
        subpixel True default
        parallel:
            Null(640.0, 640.0)
            'vasilisa'
        parallel:
            xpos -0.3
            linear 0.80 xpos 1.3
    with Pause(0.90)
    show vasilisa:
        xpos 1.3
    play sound2 door_break
    window show
    "Даже рыжая тян,{w=0.2} которая с разбегу выносит дверь и залетает в толкан."
    play sound possala
    "Скит всё так же любовался своими руками."
    "А ведь если просто начать заниматься спортом{w=0.2}.{w=0.2}.{w=0.2}."
    "То и Димас может стать кочкой."
    "Масса -{w} есть."
    "Небольшая,{w=0.2} но есть."
    "Остались тренировки и спортивное питание."
    "Но с этим всё посложнее."
    "Дима,{w=0.2} конечно,{w=0.2} никогда не славился пробитием очка с любой хавки."
    "Но крафтовый спортпит с ходу пить он очкует."
    "Хотя,{w=0.2} когда работаешь сантехником{w=0.2}.{w=0.2}.{w=0.2}."
    "Не похуй ли?"
    "Толчок всегда под рукой."
    window hide
    pause 1
    "Димас прислушался{w=0.2}.{w=0.2}.{w=0.2}."
    "И помимо стандартных звуков мочеиспускания он услышал приглушённые маты{w=0.2}.{w=0.2}.{w=0.2}."
    "Единственная мысль,{w=0.2} которая его посетила{w=0.2}.{w=0.2}.{w=0.2}."
    stop sound fadeout 3
    th4 "Бля{w=0.2}.{w=0.2}.{w=0.2}.{w} А какой из толчков я обоссал?" with vpunch
    play sound smiltolkan
    th4 "Будет нехорошо если она на обоссаный мною полетела."
    "Рыжая тян выходит с параши."
    window hide
    play sound door_open
    pause 1
    show vasilisa:
        subpixel True default
        parallel:
            Null(640.0, 640.0)
            'vasilisa'
        parallel:
            xpos -0.3
            linear 0.56 xpos 0.25
    with Pause(0.66)
    show vasilisa:
        xpos 0.25
    window show
    stop music fadeout 7
    vas "Дружище,{w=0.2} не знаешь,{w=0.2} кто весь ободок обоссал?" with vpunch
    "Скит начал паниковать."
    play sound nezn2
    window hide
    pause 1.7
    vas "Уверен?" with vpunch
    play sound nezn3
    window hide
    pause 1.9
    vas "Ну ладно."
    "И тут Василиса заметила подозрительное сходство этого типа с описанием Неони."
    play music theorem
    vas "Как тебя звать?" with vpunch
    skt "К чему такие вопросы?"
    vas "Это важно."
    "Димка почуял неладное."
    "Рука машинально потянулась к старенькому макарычу,{w=0.2} что Скит всегда с собой таскал за пазухой."
    play sound dostal
    "Однако,{w=0.2} было уже поздно."
    "Прямо в лоб Диме был направлен {b}семнадцатый Glock{/b}."
    skt "Что тебе нужно?"
    vas "Узнать,{w=0.2} кто обоссал стульчак." with vpunch
    "Скит понял,{w=0.2} что с этой девочкой шутить не стоит."
    skt "Это был я." with vpunch
    skt "Прости пожалуйста."
    skt "Я не хотел."
    skt "Честно."
    "Соврал он."
    skt "Просто голова закружилась,{w=0.2} и я наклонился,{w=0.2} пока ссал{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Голова закружилась?!" with vpunch
    vas "Да там твоя ссанина с потолка аж капает!" with vpunch
    vas "Это ж какой напор должен был быть?!" with vpunch
    skt "Да у тебя тоже неслабый был{w=0.2}.{w=0.2}.{w=0.2}."
    play sound pistolkurok
    "Она взвела курок пистолета."
    vas "Ты мне тут не тыкай!" with vpunch
    vas "Вытерпи с моё."
    vas "И не такой напор будет."
    skt "Давай забудем то,{w=0.2} что тут было,{w=0.2} а?"
    vas "Ты погоди."
    vas "Так как тебя звать-то?"
    skt "Меня зовут Дмитрий."
    skt "Дмитрий Скитецкий."
    "Василиса ахуела."
    "Это тот самый Скит."
    th3 "И что мне теперь с ним делать?"
    skt "Малолетка конченная тебя послала ко мне,{w=0.2} да?"
    "Скит горько усмехнулся."
    skt "Убьёшь меня?" with vpunch
    "У неё начали дрожать руки."
    "Начался самый настоящий мандраж."
    play sound ubralstvol
    "Василиса опустила пистолет."
    vas "Не собираюсь я тебя убивать."
    "Димасик выдохнул."
    stop music fadeout 5
    vas "У меня есть информация для тебя."
    vas "А за стульчак ты ответишь."
    vas "Извращенец." with vpunch
    skt "А почему извращенец?"
    vas "А зачем тогда подслушивал?"
    "Скиту не нашлось,{w=0.2} что ответить."
    play music hgod fadein 3
    "И следом назрел вопрос."
    skt "А ты где ствол ныкаешь-то?" with vpunch
    skt "На юбках карманов вроде нету,{w=0.2} насколько я знаю."
    vas "Ты уверен,{w=0.2} что хочешь это знать?"
    "Скит задумался."
    skt "Конечно."
    vas "На трусах карманчик есть." with vpunch
    skt "Да ну."
    skt "Он слишком маленький для глока."
    vas "Ладно,{w=0.2} развести тебя не получилось."
    vas "Я храню ствол между трусами и пиздой." with vpunch
    vas "Я возбуждаюсь,{w=0.2} когда мой клитер касается холодного металла."
    vas "И начинаю течь."
    vas "Весь ствол пахнет смазкой."
    vas "Не хочешь занюхнуть?" with vpunch
    "Все эти фразы она выпалила с явной долей язвы в голосе,{w=0.2} но скит этого не заметил."
    "Мб тупой слишком."
    skt "Давай." with vpunch
    "Василиса достала ствол из под юбки."
    "Сделала всё так,{w=0.2} чтобы Скит не заметил подсумок,{w=0.2} который прикреплён к бедру."
    play sound vdohnul
    "Скит понюхал ствол."
    skt "Но он же ничем не пахнет!"
    vas "Потому что ты идиот." with vpunch
    "Резко констатировала факт Василиса."
    "Скит лишь пожал плечами."
    skt "Ты говорила,{w=0.2} что у тебя есть информация для меня?"
    vas "Да."
    vas "Но не здесь."
    vas "Много лишних ушей."
    vas "Тип с дверного проёма уже минут 15 на нас глазеет." with vpunch
    play sound door_break
    "После этих слов дверь в толкан захлопнулась."
    skt "Тогда поехали ко мне."
    vas "Не хотелось бы,{w=0.2} конечно{w=0.2}.{w=0.2}.{w=0.2}."
    stop music fadeout 4
    vas "Но вариантов лучше у меня нет."
    skt "Тогда прыгаем в мою ладу 2110 и стартуем."
    skt "Ехать недалеко там."
    scene nmall
    show doshd
    play music rassvet fadein 2
    play ambience dviglo fadein 4
    with dissolve2
    "Они прыгнули в тачку Скита."
    "Он изначально хотел подрубить треков {b}EMINEM{/b}а, но передумал."
    "Они ему уже просто надоели."
    "А {b}plenka{/b} она бы не оценила."
    "По крайней мере,{w=0.2} так думал Дима."
    "Поэтому он подрубил молодёжного исполнителя."
    "Василиса это никак не прокоментировала."
    "И они продолжали двигаться к Львовскому переулку 4."
    scene traphata
    show doshd
    with dissolve2
    stop ambience fadeout 3
    stop music fadeout 3
    skt "Приехали."
    window hide
    scene domext
    show doshd
    play ambience rain_out
    play sound tazik1
    with vpunch
    show vasilisa:
        subpixel True default
        parallel:
            Null(640.0, 640.0)
            'vasilisa'
        parallel:
            xpos -0.3
            linear 0.56 xpos 0.25
    with Pause(0.66)
    show vasilisa:
        xpos 0.25
    window show
    vas "Веди,{w=0.2} сорвиголова."
    window hide
    stop ambience fadeout 3
    play music morandi fadein 3
    scene domint
    show vasilisa at left
    with ed_lap
    skt "Вот они,{w=0.2} мои хоромы."
    vas "Бомжатник." with vpunch
    skt "Да почему?"
    vas "Воняет носками."
    vas "Ремонт не делался лет двадцать."
    vas "Ну и твои трусы с черкашами под тумбочкой лежат."
    show krisa at right
    dobby "Привет." with vpunch
    window hide
    pause 1
    vas "ЕБАТЬ!" with vpunch
    "Василиса аж подпрыгнула от неожиданности."
    vas "Ты что ещё за хуйня?!"
    dobby "Я не хуйня,{w=0.2} я -{w} {b}доберман{/b}."
    vas "С хуя ли у тебя тут такой зоопарк?" with vpunch
    skt "Ответь мне на один вопрос."
    "Обратился он к доберману."
    skt "Кто такой Ракун?"
    dobby "Да я ебу?" with vpunch
    skt "Понятно."
    "Скит достал из под заваленного шкафа ргдшку."
    dobby "Что тебе понятно?"
    show grena at right
    play sound prosto
    skt "Всё просто!"
    dobby "Что ты делаешь?!" with vpunch
    hide grena
    play sound grena0
    dobby "БЛЯ!" with vpunch
    play sound grena1
    show normalno_ebanulo with dspr:
        ypos 0.15
        xpos 0.50
        zoom 1.6

    with vpunch
    window hide
    hide krisa
    hide normalno_ebanulo
    play sound2 perdun
    show krisa:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 2 rotate 1080 zoom 0.0 xpos 0.45 ypos 0.1
    window hide
    pause 2
    "После того,{w=0.2} как доберманчик улетел всратосферу,{w=0.2} Димка решил объяснить своё поведение Василисе."
    skt "Это не мой доберман."
    skt "Как оказалось,{w=0.2} подставным был и тот,{w=0.2} который пытался отогнать школьников."
    skt "В итоге они его застралели с СВД."
    th4 "Вечный,{w=0.2} сука,{w=0.2} ты за это ответишь."
    vas "Дурдом." with vpunch
    vas "Сплошной." with vpunch
    "Дима хотел что-то возразить,{w=0.2} как вдруг{w=0.2}.{w=0.2}.{w=0.2}."
    play sound mobila_zvonok
    skt "Да сука!" with vpunch
    "Димочке позвонили на {b}POCO M3 PRO 5G{/b}."
    "Пиздатый рингтон,{w=0.2} да?"
    play sound mobila_dostal
    skt "Оло."
    "На проводе был его брат -{w=0.2} Даня Скитецкий."
    "Он как раз сдавал егэ."
    play sound ege1
    with vpunch
    window hide
    pause 6
    skt "И?"
    play sound ege2
    with vpunch
    window hide
    pause 17
    skt "Какой Сталин-Гулаг?"
    play sound ege3
    with vpunch
    window hide
    pause 20
    skt "Успокойся."
    play sound ege4
    with vpunch
    window hide
    pause 19
    skt "Они всем так говорят."
    play sound ege5
    with vpunch
    window hide
    pause 7
    skt "Ну а как ты хотел?{w} Всё по чесноку."
    play sound ege6
    with vpunch
    window hide
    pause 19
    play sound mobila_polojil
    skt "Заебал своим нытьём сука."
    "Скит сбросил звонок."
    vas "Типа на линии явно таращит."
    skt "Ой,{w=0.2} блять." with vpunch
    skt "Как буд то сама ЕГЭ не сдавала{w=0.2}.{w=0.2}.{w=0.2}."
    stop music fadeout 4
    "Василиса впала в ступор."
    "Однако быстро оклемалась."
    skt "Так что за информация?"
    play music crysis21
    vas "Тебя заказал Казах." with vpunch
    window hide
    pause 1
    play sound chivo_blyat
    pause 1
    vas "Не удивляйся."
    vas "Это действительно так."
    skt "Значит,{w=0.2} всё суперхуёво{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Я тебе больше скажу."
    vas "Он разработал методику теневого клонирования людей." with vpunch
    vas "Он смог клонировать меня и Вадима Морозова."
    vas "Мой оригинал он убил." with vpunch
    vas "Сучара{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Небось долго над ней издевался{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    vas "А клоны Вадимки просто уродливые получаюся."
    vas "Один лысый,{w=0.2} другой сизый{w=0.2}.{w=0.2}.{w=0.2}."
    vas "В общем,{w=0.2} он настоящий садист." with vpunch
    skt "Пиздец{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Он приказал мне убить тебя." with vpunch
    skt "Ты же не собираешься{nw}"
    vas "Нет."
    vas "Расслабься."
    skt "И что предлагаешь делать?"
    vas "Пока что нас двое."
    vas "И я не самый надежный вариант для тебя."
    skt "Почему?"
    vas "Казах говорил,{w=0.2} что у него есть секретная комбинация отката клона."
    vas "Стоит ему сказать эту фразу как меня переклинит." with vpunch
    vas "Всё это с его слов."
    vas "Может быть,{w=0.2} он блефовал."
    vas "Но я проверять не особо хочу."
    stop music fadeout 4
    skt "Армии клонов и этой технологии впринципе у меня нет."
    skt "Но у меня есть один туз в рукаве." with vpunch
    skt "Причем козырный."
    skt "Позывной Вечный тебе о чём нибудь говорит?" with vpunch
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Василисы:")
    hide zatemnenie with dissolve2
    play music crysis3pausetheme
    hide vasilisa
    show skitpio
    with flash
    window show
    show rageone with ed_alpha_diss_fast
    th3 "Ещё как говорит{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Так я же{w=0.2}.{w=0.2}.{w=0.2}."
    "У неё началось головокружение и адская пульсация в висках."
    hide rageone
    show ragetwo with ed_alpha_diss_fast
    vas "Что-то мне нехорошо{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Ты только не помирай мне тут!"
    hide ragetwo
    show ragethree with ed_alpha_diss_fast
    "Боль стала невыносимой."
    "Кричать не было сил."
    show blink
    "Василиса просто закрыла глаза."
    window hide
    scene black
    pause 1
    scene tusa
    show bergennorm
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    show unblink
    vchn "И для чего тебе всё это надо было?" with vpunch
    "Василиса потеряла дар речи."
    "Увиденное шокировало похлеще вкладки {b}trans на сайте x-videos{/b}."
    vchn "Ты так и будешь молчать?" with vpunch
    "Похуистическим тоном спросил Вечный."
    vas "прости{w=0.2}.{w=0.2}.{w=0.2}."
    "Тихо вымолвила Василиса."
    vchn "Что мне твоё прости?" with vpunch
    vchn "Ты уже показала себя в деле."
    "У Василисы машинально потекли слёзы."
    vchn "Слезами горю не поможешь."
    vchn "Успокойся для начала."
    vchn "Потом помоги Димону наказать школьников."
    vchn "Этим ты и заработаешь себе искупление." with vpunch
    "Василиса лишь угрюмо кивнула."
    stop music fadeout 3
    vchn "А теперь очнись." with vpunch
    vas "Что?"
    lis "ОЧНИСЬ!" with vpunch
    "Картина перед глазами начала рушиться."
    window hide
    scene black with ed_night_dis
    play sound fb
    scene domint
    show skitpio
    with flash
    play music crysis3 fadein 2
    skt "ОЧНИСЬ!" with vpunch
    "Василиса начала жадно хватать ртом воздух."
    skt "Оклемалась?"
    "Василиса отдышалась."
    vas "Вроде да."
    skt "Всё забываю спросить{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Как тебя звать-то хоть?"
    vas "Ва{w=0.2}.{w=0.2}.{w=0.2}."
    "Её терзали мысли о том сне."
    vas "ва{w=0.2}.{w=0.2}.{w=0.2}."
    "Она же сейчас разревётся!"
    vas "ВАСИЛИСА!" with vpunch
    "Она обняла Скита и начала реветь навзрыд."
    "Но Скит не такой чёрствый,{w=0.2} как вы думаете."
    skt "Ну тише,{w=0.2} тише{w=0.2}.{w=0.2}.{w=0.2}."
    "Скиту стало грустно."
    skt "Перестань,{w=0.2} а не то я тоже заплачу{w=0.2}.{w=0.2}.{w=0.2}."
    "Дима пытался держаться изо всех сил{w=0.2}.{w=0.2}.{w=0.2}."
    "Но по итогу тоже пустил скупую мужскую."
    window hide
    pause 1
    "Они сидели на полу обняв друг друга."
    "Каждый думал о своём."
    "Скит продумывал план с кодовым названием {b}<<CRASH MALOLETOK>>{/b}."
    "Василиса пыталась успокоится."
    "Как бы она себя не пыталась переубедить{w=0.2}.{w=0.2}.{w=0.2}."
    "Она окончательно поняла,{w=0.2} что любит Вечного."
    "И по итогу поступила с ним так{w=0.2}.{w=0.2}.{w=0.2}."
    "Но положение спас Скит."
    skt "Я отправлю ему гс."
    skt "Он нам нужен как воздух."
    skt "Без него мы не справимся."
    "Василиса понимала это."
    "Но она не могла представить себе{w=0.2}.{w=0.2}.{w=0.2}."
    ".{w=0.2}.{w=0.2}.{w=0.2}как теперь смотреть ему в глаза{w=0.2}.{w=0.2}.{w=0.2}."
    "Тем временем скит уже достал свой {b}POCO M3 PRO 5G{/b} и открыл телеграм."
    "Потом начал записывать гс,{w=0.2} убрав дрожь в голосе."
    skt "Здарово,{w=0.2} агалый."
    skt "Мне сейчас как никогда нужна твоя помощь."
    skt "Если ты приедешь сюда быстро,{w=0.2} так уж и быть,{w=0.2} прощу тебе те подсрачники и подстреленного добермана."
    skt "Буду ждать ответа."
    "Скит убрал телефон."
    vas "волнуюсь{w=0.2}.{w=0.2}.{w=0.2}.{w} очень{w=0.2}.{w=0.2}.{w=0.2}."
    stop music fadeout 7
    "Из-за эмоционального перенапряжения Василиса начала говорить очень тихо."
    "Видно, эта фича досталась ей от покойного оригинала."
    play sound zubek
    with vpunch
    "Пиликнул поко Димы,{w=0.2} где был установлен звук айфона на уведомлениях."
    "Дима увидел гску и сразу же её включил."
    window hide
    play sound gskabergena
    pause 19
    window show
    skt "Будем ждать."
    play music theorem
    play ambience domofon
    with vpunch
    window hide
    pause 1
    skt "Какого{w=0.2}.{w=0.2}.{w=0.2}."
    vas "кто там?"
    skt "Я никого сегодня не жду{w=0.2}.{w=0.2}.{w=0.2}."
    stop ambience fadeout 3
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Колда:")
    hide zatemnenie with dissolve2
    scene domext with ed_lap
    cld "Опачки..."
    rcn "мфмфмфм!1!" with vpunch
    cld "Потерпи сладкий."
    cld "Оказывается,{w=0.2} у нас завелась крыса{w=0.2}.{w=0.2}.{w=0.2}."
    cld "Никогда бы не подумал{w=0.2}.{w=0.2}.{w=0.2}."
    play ambience domofon1
    "Колд начал звонить в домофон."
    window hide
    pause 2
    stop ambience
    play sound mobila_dostal
    skt "Ало."
    cld "Привет,{w=0.2} Лысая." with vpunch
    cld "Узнаешь меня?"
    window hide
    pause 1
    skt "Это ты,{w=0.2} малолетка конченная?"
    cld "И я тут не один."
    "Колд сдавил правое яичко Ракуна,{w=0.2} что оно чуть не лопнуло."
    rcn "МФМФМФМ!" with vpunch
    cld "Узнаешь голосок?"
    skt "За Ракуна ты ответишь,{w=0.2} школьница."
    cld "Если не хочешь,{w=0.2} чтобы я отстрелил ему башку,{w=0.2} то выходи."
    cld "А не то{nw}"
    rcn "МФМФМФМФМ!!!!" with vpunch
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Скита:")
    hide zatemnenie with dissolve2
    scene domint
    show vasilisa
    with ed_lap
    skt "Нужно идти."
    vas "не оставляй меня{w=0.2}.{w=0.2}.{w=0.2}."
    "Тихо вымолвила окончательно поникшая Василиса."
    skt "Иначе ему крышка."
    skt "Скоро вернусь."
    cld "Ты там скоро?" with vpunch
    skt "Заебал,{w=0.2} дай носки найти!"
    cld "Реще,{w=0.2} заебал." with vpunch
    cld "Если жизнь твоего подсоса для тебя хоть сколько-нибудь важна{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Да подожди ты,{w=0.2} заебал!" with vpunch
    stop music fadeout 4
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Колда:")
    hide zatemnenie with dissolve2
    play music zp22 fadein 3
    scene domext with ed_lap
    pause 2
    play sound door_open
    show skitpio:
        subpixel True default
        parallel:
            Null(473.0, 712.0)
            'skitpio'
        parallel:
            ypos 2.0
            linear 0.80 ypos 1.0
    with Pause(0.90)
    show skitpio:
        ypos 1.0
    pause 1 
    window show
    play sound bm16_shoot
    "В момент выхода Димы из падика Колд отстреливает башку Ракуну со своей трофейной {b}ТОЗ-34{/b}."
    skt "Пидрила,{w=0.2} ты ответишь за это!" with vpunch
    "И начался нереальный махач в стиле {b}JoJo Blizzare Adventure{/b}."
    hide skitpio
    show skitpio1 at center:
        ypos 1.1
        xpos 0.5
        zoom 1.2
        ease 0.1 xpos 0.51 ypos 1.09
        ease 0.1 xpos 0.5 ypos 1.1
        ease 0.1 xpos 0.49 ypos 1.11
        ease 0.1 xpos 0.5 ypos 1.1
        repeat

    with dspr
    play sound_loop Ora_ora_ora_LW0607

    show kulak_LW0607:
        zoom 0.1
        xpos 0.3
        ypos 0.45
        ease 0.15 zoom 0.8 xpos 0.1 ypos 0.45
        pause (0.05)
        repeat

    show kulak2_LW0607:
        zoom 0.1
        xpos 0.6
        ypos 0.45
        pause (0.05)
        ease 0.15 zoom 0.8 xpos 0.5 ypos 0.45
        repeat

    play sound_loop2 sfx_punch_washstand
    pause (0.2)
    play sound_loop3 sfx_punch_washstand

    $ renpy.pause (0.3)

    $ _window_show(dissolve)
    skt "ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA!"

    show Fight_Ddv_Dun_png with dspr
    play sound_loop Ora_Muda_LW0607

    show skitpio1 at center:
        ypos 1.1
        xpos 0.5
        zoom 1.2
        ease 0.2 zoom 1.5 xpos 0.5 ypos 1.0

    show skitpio1 at center:
        ypos 1.1
        xpos 0.5
        zoom 1.5
        ease 0.1 xpos 0.53 ypos 1.13
        ease 0.1 xpos 0.5 ypos 1.1
        ease 0.1 xpos 0.47 ypos 1.07
        ease 0.1 xpos 0.5 ypos 1.1
        repeat

    show dlya_ebala_LW0607 behind Fight_Ddv_Dun_png:
        xpos 2.0
        ypos 2.0
        ease 0.1 xpos 0.1 ypos -0.0
        pause (0.10)
        ease 0.1 xpos 2.0 ypos 2.0
        pause (0.1)
        repeat

    show dlya_ebalaleft_LW0607 behind Fight_Ddv_Dun_png:
        xpos -2.0
        ypos 1.5
        pause (0.1)
        ease 0.1 xpos -0.1 ypos -0.0
        pause (0.10)
        ease 0.1 xpos -2.0 ypos 1.5
        repeat

    show kulak_LW0607:
        zoom 0.1
        xpos 0.3
        ypos 0.65
        ease 0.15 zoom 0.8 xpos 0.1 ypos 0.65
        pause (0.05)
        repeat

    show kulak2_LW0607:
        zoom 0.1
        xpos 0.6
        ypos 0.65
        pause (0.05)
        ease 0.15 zoom 0.8 xpos 0.5 ypos 0.65
        repeat

    $ renpy.pause (0.3)

    skt "MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA!"

    $ _window_hide(dissolve)

    stop sound_loop fadeout 2
    stop sound_loop2 fadeout 2
    stop sound_loop3 fadeout 2
    hide Fight_Ddv_Dun_png
    hide kulak_LW0607
    hide kulak2_LW0607
    hide dlya_ebala_LW0607
    hide dlya_ebalaleft_LW0607
    with dissolve

    show skitpio1 at center:
        ypos 1.1
        xpos 0.5
        zoom 1.5
        ease 0.8 zoom 0.6 xpos 0.5 ypos 1.0

    $ _window_show(dissolve)
    skt "Получай, Колд-Дио!"
    $ _window_hide(dissolve)

    play sound JoJo_vsk_LW0607

    show skitpio1 at center:
        ypos 1.5
        xpos 0.5
        zoom 0.6
        ease 0.4 zoom 1.6 xpos 0.5 ypos 1.1

    show kulak_LW0607:
        zoom 0.2
        xpos 0.4
        ypos 0.5
        ease 0.4 zoom 1.5 xpos 0.15 ypos 0.0
    play sound3 sfx_punch_washstand

    $ renpy.pause (0.3)
    hide kulak_LW0607 with dspr

    play sound2 sfx_body_bump
    with vpunch
    with ed_flash_red
    show blink

    $ _window_show(dissolve)
    "Скит разъебал малолетку просто в щепки!" with vpunch
    $ _window_hide(dissolve)
    scene black
    cld "Лысый{w=0.2}.{w=0.2}.{w=0.2}."
    "Колд помирал от причинённого урона."
    cld "Скажи мне одно{w=0.2}.{w=0.2}.{w=0.2}."
    cld "Почему ты нас начал оскать с казахом?" with vpunch
    scene domext
    show skitpio
    show unblink
    "Колд кинул последний взгляд на Диму."
    skt "Всё просто."
    skt "Вы конченные малолетки." with vpunch
    cld "Да пошёл ты{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    cld "Многолетка{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    stop music
    play sound sfx_punch_washstand
    show dark_LW0607
    show blood_LW0607
    with vpunch
    pause 1
    play sound coldazvuk
    pause 4.3
    scene black
    pause 2
    $ MND_Chapter("От лица Скита:")
    play music Death_Note_theme_LW0607 fadein 2
    scene domext with ed_night_dis
    skt "Минус одна малолетка."
    vchn "Жесткий ты тип,{w=0.2} однако." with vpunch
    "Скит обернулся."
    window hide
    show bergennorm:
        subpixel True default
        parallel:
            Null(473.0, 712.0)
            'bergennorm'
        parallel:
            ypos 2.0
            linear 0.80 ypos 1.0
    with Pause(0.90)
    show bergennorm:
        ypos 1.0
    window show
    skt "Какой есть." with vpunch
    skt "Вовремя ты."
    vchn "Как успел." with vpunch
    "Передразнил Скита Вечный."
    skt "У меня для тебя подарок."
    vchn "Я в предвкушении."
    skt "Пошли на хату."
    skt "Она ждёт тебя там."
    vchn "Я походу понял,{w=0.2} про кого ты говоришь."
    skt "Ну тогда не будем медлить!"
    skt "Ток ты по моей команде заходи."
    skt "Я хочу её удивить."
    vchn "А она нас с окон не увидела ещё?"
    skt "У меня они на другую сторону выходят."
    vchn "Ну,{w=0.2} тогда погнали,{w=0.2} хуле."
    play sound door_open
    scene domint
    show vasilisa at right
    with ed_lap
    vas "И как всё прошло?" with vpunch
    "С ходу начала газовать Василиса."
    "Видно,{w=0.2} уже пришла в себя."
    skt "С переменным успехом."
    skt "Спасти Ракуна не удалось."
    skt "Однако малолетку я эту забил."
    skt "До смерти."
    vas "Ебать." with vpunch
    skt "А ещё у меня для тебя сюрприз."
    vas "Какой?"
    skt "Заходи давай,{w=0.2} ало."
    "И после этих слов в хату залетает Вечный."
    window hide
    play sound door_open
    show bergennorm:
        subpixel True default
        parallel:
            Null(473.0, 712.0)
            'bergennorm'
        parallel:
            ypos 2.0
            linear 0.80 ypos 1.0
    with Pause(0.90)
    show bergennorm:
        ypos 1.0
    window show
    vas "ВЕЧНЫЙ!" with vpunch
    vchn "ХЗ КАК ТЕБЯ ЗВАТЬ!" with vpunch
    "Василиса крепко сжала Вечного в обьятиях."
    "Тот,{w=0.2} отойдя от шока,{w=0.2} сделал то же самое."
    "А Димас смотрел на это как смотрит отец на своего сына."
    "С пониманием."
    vas "Мне столько всего тебе рассказать надо!" with vpunch
    vchn "Успеешь ещё."
    vchn "Димас,{w=0.2} есть чё пожрать?"
    skt "Есть бигмак."
    skt "Он,{w=0.2} правда,{w=0.2} с полудня лежит в холодосе."
    vchn "Сойдёт."
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Неони:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    scene ineony
    show deadlylxrd at right
    with ed_night_dis
    lxrd "Мы потеряли Колда." with vpunch
    lxrd "Я посмотрел по ip камерам с Новошахтинска."
    lxrd "Говорилось ему блять,{w=0.2} что не стоит в соло на такого бегемота лезть!" with vpunch
    nn "Это прискорбно."
    nn "У меня нет его образца ДНК,{w=0.2} дабы сделать клон."
    nn "ДНК Вечного тоже голимый оказался."
    lxrd "Может,{w=0.2} у образцов срок действия заканчивается?"
    nn "Может быть."
    nn "А из него клоны-то пиздатые бы вышли!" with vpunch
    lxrd "Но это не самое главное сейчас."
    lxrd "Посмотри на экран."
    "Вадимка отмотал на нужный таймкод."
    "Рядом со Скитом чиллил Вечный."
    nn "Ты тоже это видишь?"
    lxrd "Ага."
    lxrd "Кароче говоря,{w=0.2} у нас завёлся {b}IMPOSTER{/b}." with vpunch
    nn "Это суперприскорбно{w=0.2}.{w=0.2}.{w=0.2}."
    lxrd "Но у меня есть идея как их обоих нейтрализовать."
    nn "И как же?"
    lxrd "Нужно связаться с одним человеком."
    lxrd "Он ща в подполье."
    lxrd "Я пойду один." with vpunch
    nn "Я походу понял,{w=0.2} про кого ты."
    lxrd "Думаешь о том же,{w=0.2} о чём и я?"
    nn "Именно."
    nn "Пизда им." with vpunch
    nn "Но ты не торопись." with vpunch
    nn "Ещё нужно кое-что доделать,{w=0.2} дабы быть уверенным в его соглашении."
    nn "Только впечатлив его,{w=0.2} мы сможем добиться его согласия."
    nn "Просто так -{w} он не влезет в это дело."
    nn "Никак." with vpunch
    lxrd "Я понимаю."
    lxrd "И что ты предлагаешь?"
    nn "Я досовершенствую систему клонирования."
    nn "Результат увидишь сам."
    lxrd "Всё таки стоит ломануть сейф."
    lxrd "Похуй уже,{w=0.2} что там может быть заминировано." with vpunch
    nn "С этим позже."
    lxrd "Этот человек умеет ломать такие замки."
    lxrd "Так что..."
    nn "Да." with vpunch
    nn "Сначала клоны."
    lxrd "Я тебя услышал."
    stop music fadeout 5
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Колда:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music oni fadein 2
    scene domext with ed_night_dis
    "Колд встал и отряхнулся."
    cld "Сука..." with vpunch
    "Боль пронзила всё тело в попытке встать."
    cld "Многолетка..." with vpunch
    "Скит ебашил по болевым точкам."
    "На районе его научили драться."
    "Пускай,{w=0.2} он и не дрался за район..."
    "Но неумехой он не был."
    "В итоге он нанёс чисто болевой дамаг Колду."
    cld "Что б я ещё хоть раз..."
    cld "Учавствовал в подобном..."
    "Очко малолетки подпекало."
    "Но ничего не оставалось,{w=0.2} кроме как..."
    cld "Осталось дождаться ночи." with vpunch
    cld "А там и спросим с Вечного."
    cld "Его план,{w=0.2} конечно,{w=0.2} ахуенный..."
    cld "Но мне такое не по душе."
    play sound fb
    scene coldbuhaet
    show layer master at VHS(0.83, 0.83, 0.77, 1.0)
    with flash
    vchn "Пока Вадимка в толчке -{w} нам нужно разработать план."
    cld "Что ты предлагаешь?"
    vchn "Я на хорошем счету у Скита."
    vchn "Нужно его немного расшатать,{w=0.2} дабы я смог поднять уровень доверия выше,{w=0.2} помогая ему."
    cld "И как?"
    vchn "Легко." with vpunch
    vchn "У Неони в планах создать лабараторию по клонированию типов."
    vchn "Днк Ракуна у тебя где-{w=0.2}то был."
    vchn "Вот и сделаешь его клон,{w=0.2} дабы шантажить Скита."
    vchn "Он про клона знать не будет."
    vchn "Будет думать,{w=0.2} что это ориг."
    vchn "И всё!" with vpunch
    vchn "Дело в шляпе."
    vchn "Патрон один возьми на всякий."
    vchn "Не то вторым Скита ваншотнешь."
    vchn "Убить он тебя не сможет в любом случае."
    vchn "Подберёшься близко -{w} начинай давить на него."
    vchn "Дальше будешь импровизировать."
    cld "Почему я?" with vpunch
    "Единственный вопрос,{w=0.2} который не давал Колду покоя."
    vchn "Больше некому." with vpunch
    "Лишь кратко бросил Вечный,{w=0.2} после чего пафосно ушёл в другую комнату за подиком или чем-{w=0.2}то ещё."
    cld "Легко сказать..."
    "Колду ничего не оставалось,{w=0.2} кроме как попробовать провернуть эту афёру."
    play sound fb
    scene domext with flash
    cld "Такая судьба у нас..."
    cld "Нелёгкая..."
    cld "Ха." with vpunch
    "После этих слов,{w=0.2} Колд принялся ждать ночи."
    "Больше ничего не оставалось делать."
    show zatemnenie with dissolve2
    $ MND_Chapter("Конец третьего картера...")
    scene black with ed_night_dis
    jump carter4