label c0_shooter_askania_hit:
    play sound4 b_atanda
    scene shooter_nv_only_askania_ground
    window hide
    play sound toz34_draw
    show tozik_pricel_anim1
    pause 0.15
    hide tozik_pricel_anim1
    show tozik_pricel_anim2
    pause 0.15
    hide tozik_pricel_anim2
    play sound toz_shoot
    show tozik_shoot_anim1
    pause 0.1
    hide tozik_shoot_anim1
    show tozik_shoot_anim2
    pause 0.3
    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.51
    pause 0.25
    hide hitmarkermlg_LW0607 at center
    play sound2 breaking_glass
    scene shooter_nv
    show tozik2
    with flash_fast2
    play sound toz34_draw
    hide tozik2
    show tozik_pricel_anim3
    pause 0.15
    hide tozik_pricel_anim3
    show tozik_pricel_anim4
    pause 0.15
    play sound4 b_smeh1
    with vpunch
    pause 1.3
    play sound d_normalno
    pause 0.7
    cld "Продолжай, ебанько."
    cld "Умения уже апаются."
    "Колд заставлял Вечного ебашить дальше."
    "После чего выдал разрывную, поставив новую, ахуенную тару."
    window hide
    show shooter_nv_3 with dspr
    play sound b_komik
    with vpunch
    pause 5
    th "Видимо, слава моего легендарного коктейля уже превысила все ожидаемые мною нормы."
    th "Лысая малышка - forever."
    th "Да тут по-другому и не скажешь."
    th "Правда?"
    vchn "Прикол я оценил."
    cld "Какой прикол?" with vpunch
    th "Чтоп, сто?" with vpunch
    cld "Шмаляй давай, хули ты стоишь?" with vpunch
    vchn "А, да. Ща."
    "И Вечный отпрянул ото сна и начал хуячить, струячить и ебачить одновременно."
    th "Ах да..."
    th "Пули же кончились..."
    th "Надо зарядиться..."
    "И Вечный погнал перезаряжаться."
    window hide
    play sound3 team_reload
    play sound2 toz34_draw
    hide tozik_pricel_anim4
    show tozik_reload_anim1
    pause 0.1
    hide tozik_reload_anim1
    play sound toz_reload1
    show tozik_reload_anim2
    pause 0.1
    hide tozik_reload_anim2
    show tozik_reload_anim3
    pause 0.15
    hide tozik_reload_anim3
    play sound2 toz_reload2
    show tozik_reload_anim4
    pause 0.25
    hide tozik_reload_anim4
    play sound2 toz_reload3
    show tozik_reload_anim5
    pause 0.2
    hide tozik_reload_anim5
    play sound2 toz_reload4
    show tozik_reload_anim6
    pause 0.2
    hide tozik_reload_anim6
    show tozik_reload_anim7
    pause 0.2
    call screen c0_shooter_2

label c0_shooter_vodka_hit:
    play sound3 b_zamai
    scene shooter_nv_only_vodka_ground
    window hide
    play sound toz34_draw
    show tozik_pricel_anim1
    pause 0.15
    hide tozik_pricel_anim1
    show tozik_pricel_anim2
    pause 0.15
    hide tozik_pricel_anim2
    play sound toz_shoot
    show tozik_shoot_anim1
    pause 0.1
    hide tozik_shoot_anim1
    show tozik_shoot_anim2
    pause 0.3
    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.77
    pause 0.25
    hide hitmarkermlg_LW0607 at center
    play sound2 breaking_glass
    scene shooter_nv
    show tozik2
    with flash_fast2
    play sound toz34_draw
    hide tozik2
    show tozik_pricel_anim3
    pause 0.15
    hide tozik_pricel_anim3
    show tozik_pricel_anim4
    pause 0.15
    play sound3 b_beret
    with vpunch
    pause 1.3
    play sound d_neploho
    pause 0.7
    cld "Продолжать будешь?"
    "Колд неожиданно спросил это у Вечного."
    "А Вечный задумался."
    "Хорошо так."
    jump c0_shooter_succes_nahui

label c0_shooter_ohota_hit:
    play sound4 b_chiki
    scene shooter_nv_only_ohota_ground
    window hide
    show tozik_pricel_anim1
    pause 0.15
    hide tozik_pricel_anim1
    show tozik_pricel_anim2
    pause 0.15
    hide tozik_pricel_anim2
    play sound toz_shoot
    show tozik_shoot_anim1
    pause 0.1
    hide tozik_shoot_anim1
    show tozik_shoot_anim2
    pause 0.3
    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.05
    pause 0.25
    hide hitmarkermlg_LW0607 at center
    play sound2 breaking_glass
    scene shooter_nv
    show tozik2
    with flash_fast2
    play sound toz34_draw
    hide tozik2
    show tozik_pricel_anim3
    pause 0.15
    hide tozik_pricel_anim3
    show tozik_pricel_anim4
    pause 0.15
    play sound4 b_smeh
    with vpunch
    pause 1.3
    play sound ebanushka
    pause 0.7
    cld "Ты чё сделал?" with vpunch
    vchn "Да чё не так-то?" with vpunch
    cld "Ты мне чуть башку не снёс пулей, ебанько."
    window hide
    play sound team_naberut
    pause 4
    "Вечный в душе тихонько гоготнул, но виду не подал."
    "Реально ведь мог тыковку снести по своей тупости."
    cld "Ладно, оно того стоило."
    cld "Может, хоть где-то чему-то дельному научишься."
    "Колд подбадривал Вечного, ведь знал - за этим парнишей большое будущее, ахаха."
    "Вечный проверил боезапас, да погнал шмалять со шпалера дальше."
    "А Колд в это время ставил новую бутыль."
    window hide
    show shooter_nv_2 with dspr
    play sound b_plesen
    pause 1
    th "Аскания - дело святое."
    th "Хотя... Мятная - говнище то ещё."
    th "Лимонной, видно, не было..."
    "Вечный начал шпалерить дальше."
    window hide
    call screen c0_shooter_1

label c0_shooter_essa_hit:
    scene shooter_nv_only_essa_ground
    window hide
    play sound toz34_draw
    show tozik_pricel_anim1
    pause 0.15
    hide tozik_pricel_anim1
    show tozik_pricel_anim2
    pause 0.15
    hide tozik_pricel_anim2
    play sound toz_shoot
    show tozik_shoot_anim1
    pause 0.1
    hide tozik_shoot_anim1
    show tozik_shoot_anim2
    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.05
    pause 0.25
    hide hitmarkermlg_LW0607 at center
    play sound2 breaking_glass
    scene shooter_nv
    show tozik2
    with flash_fast2
    play sound toz34_draw
    hide tozik2
    show tozik_pricel_anim3
    pause 0.15
    hide tozik_pricel_anim3
    show tozik_pricel_anim4
    pause 0.15
    play sound v_nat_klass
    pause 1.7
    "Первая тара из под ESSE была успешно отстреляна, ёпта."
    "После чего была выставлена ахуеть какая тара разрывная."
    window hide
    scene shooter_nv_only_garage_ground
    show tozik1
    with dspr
    "Тара из под лимонного гаража должна притягивать удачу."
    "По крайней мере, так думал Вечный."
    "Время пострелять, между нами шотgun..."
    th "Ах да..."
    th "Пули же кончились..."
    th "Надо зарядиться..."
    "И Вечный погнал перезаряжаться."
    lxrd "Привет." with vpunch
    window hide
    play sound3 team_reload
    play sound2 toz34_draw
    hide tozik1
    show tozik_reload_anim1
    pause 0.1
    hide tozik_reload_anim1
    play sound toz_reload1
    show tozik_reload_anim2
    pause 0.1
    hide tozik_reload_anim2
    show tozik_reload_anim3
    pause 0.15
    hide tozik_reload_anim3
    play sound2 toz_reload2
    show tozik_reload_anim4
    pause 0.25
    hide tozik_reload_anim4
    play sound2 toz_reload3
    show tozik_reload_anim5
    pause 0.2
    hide tozik_reload_anim5
    play sound2 toz_reload4
    show tozik_reload_anim6
    pause 0.2
    hide tozik_reload_anim6
    show tozik_reload_anim7
    pause 0.2
    vchn "Надо что-то?"
    "Мрачно спросил Вечный подошедшего сзади Лорда."
    lxrd "Да нет."
    lxrd "Спросить вот хотел."
    lxrd "Как успехи в этом нелёгком деле?"
    call screen c0_shooter_4

label c0_shooter_garage_hit:
    scene shooter_nv_only_garage_ground
    window hide
    play sound toz34_draw
    show tozik_pricel_anim1
    pause 0.15
    hide tozik_pricel_anim1
    show tozik_pricel_anim2
    pause 0.15
    hide tozik_pricel_anim2
    play sound toz_shoot
    show tozik_shoot_anim1
    pause 0.1
    hide tozik_shoot_anim1
    show tozik_shoot_anim2
    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.51
    pause 0.25
    hide hitmarkermlg_LW0607 at center
    play sound2 breaking_glass
    scene shooter_nv
    show tozik2
    with flash_fast2
    play sound toz34_draw
    hide tozik2
    show tozik_pricel_anim3
    pause 0.15
    hide tozik_pricel_anim3
    show tozik_pricel_anim4
    pause 0.15
    play sound v_chetko
    pause 0.7
    vchn "Как видишь -{w} неплохо."
    "У Вечного не было никакого желания отвлекаться и гутарить с Лордом."
    lxrd "Сильно отвлекаю небось?"
    vchn "Нет."
    window hide
    scene shooter_nv_only_huga_ground
    show tozik1
    with dspr
    "Вечный поставил последнюю бутылку на мишень."
    window hide
    call screen c0_shooter_5

label c0_shooter_huga_hit:
    scene shooter_nv_only_huga_ground
    window hide
    play sound toz34_draw
    show tozik_pricel_anim1
    pause 0.15
    hide tozik_pricel_anim1
    show tozik_pricel_anim2
    pause 0.15
    hide tozik_pricel_anim2
    play sound toz_shoot
    show tozik_shoot_anim1
    pause 0.1
    hide tozik_shoot_anim1
    show tozik_shoot_anim2
    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.77
    pause 0.25
    hide hitmarkermlg_LW0607 at center
    play sound2 metall01gr
    scene shooter_nv
    show tozik2
    with flash_fast2
    play sound toz34_draw
    hide tozik2
    show tozik_pricel_anim3
    pause 0.15
    hide tozik_pricel_anim3
    show tozik_pricel_anim4
    pause 0.15
    play sound v_zaebis
    pause 0.7
    "Последняя тара из под хуги была отстреляна."
    th "Тары закончились, сука-а-а..."
    th "Мне влом другие искать..."
    th "Но ствол надо бы зарядить..."
    "И Вечный погнал перезаряжаться."
    lxrd "Рассказывай - чем заняться планируешь?" with vpunch
    window hide
    play sound3 team_reload
    play sound2 toz34_draw
    hide tozik_pricel_anim4
    show tozik_reload_anim1
    pause 0.1
    hide tozik_reload_anim1
    play sound toz_reload1
    show tozik_reload_anim2
    pause 0.1
    hide tozik_reload_anim2
    show tozik_reload_anim3
    pause 0.15
    hide tozik_reload_anim3
    play sound2 toz_reload2
    show tozik_reload_anim4
    pause 0.25
    hide tozik_reload_anim4
    play sound2 toz_reload3
    show tozik_reload_anim5
    pause 0.2
    hide tozik_reload_anim5
    play sound2 toz_reload4
    show tozik_reload_anim6
    pause 0.2
    hide tozik_reload_anim6
    show tozik_reload_anim7
    pause 0.5
    play sound ubral
    hide tozik_reload_anim7
    play sound ubralstvol
    show tozik_ubral_anim
    pause 0.49
    hide tozik_ubral_anim
    scene shooter_nv_zerkal
    show deadlylxrd
    with pushleft
    play sound pr_ploho_ponyal
    pause 3
    jump c0_shooter_vadimka_success

###ЭКРАНЫ
screen c0_shooter:
    tag menu 
    modal True
    imagemap: 
        ground "source/shooter_nv_only_ohota_ground.jpg" 
        hover  "source/shooter_nv_only_ohota_hover.jpg"
        add "source/tozik1.png"
        alpha True

        hotspot (128, 1, 114, 222) clicked[Jump("c0_shooter_ohota_hit")]

screen c0_shooter_1:
    tag menu 
    modal True
    imagemap: 
        ground "source/shooter_nv_only_askania_ground.jpg" 
        hover  "source/shooter_nv_only_askania_hover.jpg"
        add "source/tozik1.png"
        alpha True

        hotspot (1030, 3, 75, 211) clicked[Jump("c0_shooter_askania_hit")]

screen c0_shooter_2:
    tag menu 
    modal True
    imagemap: 
        ground "source/shooter_nv_only_vodka_ground.jpg" 
        hover  "source/shooter_nv_only_vodka_hover.jpg"
        add "source/tozik1.png"
        alpha True

        hotspot (1537, 0, 88, 243) clicked[Jump("c0_shooter_vodka_hit")]

screen c0_shooter_3:
    tag menu 
    modal True
    imagemap: 
        ground "source/shooter_nv_only_essa_ground.jpg" 
        hover  "source/shooter_nv_only_essa_hover.jpg"
        add "source/tozik1.png"
        alpha True

        hotspot (127, 1, 114, 222) clicked[Jump("c0_shooter_essa_hit")]

screen c0_shooter_4:
    tag menu 
    modal True
    imagemap: 
        ground "source/shooter_nv_only_garage_ground.jpg" 
        hover  "source/shooter_nv_only_garage_hover.jpg"
        add "source/tozik1.png"
        alpha True

        hotspot (1030, 3, 75, 211) clicked[Jump("c0_shooter_garage_hit")]

screen c0_shooter_5:
    tag menu 
    modal True
    imagemap: 
        ground "source/shooter_nv_only_huga_ground.jpg" 
        hover  "source/shooter_nv_only_huga_hover.jpg"
        add "source/tozik1.png"
        alpha True

        hotspot (1537, 0, 88, 243) clicked[Jump("c0_shooter_huga_hit")]

screen c7_chisti_govno:
    tag menu 
    modal True
    imagemap: 
        ground "source/parasha_v_shkole_1.png" 
        hover  "source/parasha_v_shkole_2.png" 
        add "source/vilka1.png"
        alpha True

        hotspot (643, 28, 486, 640) clicked[Jump("c7_after_chistka_sooqa")]