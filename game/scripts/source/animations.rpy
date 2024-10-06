init:

    define ed_flash_red = Fade(1, 0, 1, color="#e11")
    define ed_alpha_diss_fast = Dissolve(0.5, alpha=True)
    define flash = Fade(.25, 0, .75, color="#fff")
    define dissolve2 = Dissolve(2.0)
    define flash_fast2 = Fade(0.05, 0, 0.35, color="#fff")
    define flash_fast_red2 = Fade(0.05, 0, 0.75, color="#ff0000")
    define fade3 = Fade(1.5, 0, 1.5)
    define fade2 = Fade(1, 0, 1)
    define dissolve3 = Dissolve(3)
    define dissolve4 = Dissolve(4)
    define dspr = Dissolve(.2)

    define ed_earth_draw = ImageDissolve("source/ed_earth_draw.png", 3.0)
    define ed_lap = ImageDissolve("source/ed_lap.png", 2.0)
    define ed_night_dis = ImageDissolve("source/ed_night_dis.png", 2.5)
    define poplil_pacan = ImageDissolve("source/wow_blya.png", 6.66)

    image sl_zombie_sprite_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.png", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite2_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.png", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite3_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.png", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite4_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.png", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite5_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.png", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite6_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.png", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite7_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.png", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite8_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.png", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite9_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.png", im.matrix.tint(0.94, 0.82, 1.0))
    image slzombar = im.MatrixColor("source/sl_zombie_sprite_LW0607.png", im.matrix.tint(0.94, 0.82, 1.0))
    image slzombar1 = im.MatrixColor("source/sl_zombie_sprite.png", im.matrix.tint(0.94, 0.82, 1.0))

    image vignette:
        truecenter
        "source/vignette.png"

    image bergenbook_obs = im.MatrixColor( im.Composite((1920,1080), (0,0), "source/bergenbook.jpg"), im.matrix.saturation(.7, desat = (0.2126, 0.7152, 0.0722)) )
    image bergenbook_obs_eshe = im.MatrixColor( im.Composite((1920,1080), (0,0), "source/bergenbook.jpg"), im.matrix.saturation(.4, desat = (0.2126, 0.7152, 0.0722)) )
    image bergenbook_obs_eshe1 = im.MatrixColor( im.Composite((1920,1080), (0,0), "source/bergenbook.jpg"), im.matrix.saturation(.0, desat = (0.2126, 0.7152, 0.0722)) )
    image bergkoridor_obs = im.MatrixColor( im.Composite((1920,1080), (0,0), "source/bergkoridor.jpg"), im.matrix.saturation(.0, desat = (0.2126, 0.7152, 0.0722)) )
    image bergkuhint1_obs = im.MatrixColor( im.Composite((1920,1080), (0,0), "source/bergkuhint1.jpg"), im.matrix.saturation(.0, desat = (0.2126, 0.7152, 0.0722)) )

#DREAM - СОН, НУ ИЛИ ФЛЕШБЕК БЛЯТЬ. ТУТ СЕПИЯ ВМЕСТО КАРТИНОК, ОК?
###DREAM BG & CG
    image ostrovok_sp = im.Sepia("source/ostrovok.jpg") # ОСТОРОВОК В NMALL
    image nightdvor_sp = im.Sepia("source/nightdvor.jpg") # ОСТОРОВОК В NMALL
    image domintnight_sp = im.Sepia("source/domintnight.jpg") # ОСТОРОВОК В NMALL

###DREAM SPRITES
    image jenek_vor_sp = im.Sepia("source/rmcj_vor.png") # БАРЫГА ВОР
    image jenek_vor_night_sp = im.Sepia("source/jenek_vor_night.png") # БАРЫГА ВОР НОЧНОЙ
    image vor_sp = im.Sepia("source/vor.png") # ВОРИШКА ЖАНИМАНОВ
    image vor_night_sp = im.Sepia("source/vor_night.png") # ВОРИШКА ЖАНИМАНОВ НОЧНОЙ
    image skitpiopivo_sp = im.Sepia("source/skitpiopivo.png") # СКИТ ПИОНЕР С ОХОТОЙ КРЕПКОЙ ДЛЯ ОБЫЧНОЙ СЦЕНЫ

###ЭФФЕКТ RTX ЛУЧЕЙ (БЛЯ БУДУ)
    image god_light:
        contains:
            "source/light_eff.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 0
            linear 120 rotate 360
            repeat
        contains:
            "source/light_eff.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 180
            linear 150 rotate -180
            repeat
        contains:
            "source/light_eff.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 90
            linear 180 rotate 450
            repeat
        contains:
            "source/light_eff.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate -90
            linear 210 rotate -450
            repeat
        contains:
            "source/light_eff.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate 45
            linear 240 rotate 405
            repeat
        contains:
            "source/light_eff.png"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5 rotate -45
            linear 270 rotate -405
            repeat

#SPR
    image vadimka_smile_sprava: #НАРИК ЛЫБИТСЯ ВЫСРАВШИСЬ СПРАВА НАПРАВО
        default subpixel True 
        parallel:
            Null(499.0, 842.0)
            'lordsprsmile'
        parallel:
            xpos 1.5 
            linear 0.30 xpos 0.8 

    image vadimka_smile_sleva: #НАРИК ЛЫБИТСЯ ВЫСРАВШИСЬ СЛЕВА НАЛЕВО
        default subpixel True 
        parallel:
            Null(499.0, 842.0)
            'lordsprsmile'
        parallel:
            xpos -0.5 
            linear 0.30 xpos 0.25

    image vadimka_leave_sprava: #НАРИК СБЕЖАЛ НАПРАВО ГАНДОН
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos 0.75
            linear 0.80 xpos 3.0

    image vadimka_leave_centr_sprava: #НАРИК СБЕЖАЛ ИЗ ЦЕНТРА НАПРАВО ГАНДОН
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos 0.5 
            linear 0.51 xpos 1.2 

###KAZAH
    image nn_spr_sprava: #КАЗАХ СПРАВА НАПРАВО
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'kazahspr'
        parallel:
            xpos 3.75
            linear 0.80 xpos 0.75

    image nn_spr_sleva: #КАЗАХ СЛЕВА НАЛЕВО
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'kazahspr'
        parallel:
            xpos -3.75
            linear 0.80 xpos 0.25

    image nn_leave_sprava: #КАЗАХ ЛИВАЕТ НАПРАВО
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'kazahspr'
        parallel:
            xpos 0.75
            linear 0.80 xpos 3.0

###JENECHKA
    image rmcj_spr_sprava: #ЖЕНЁК СПРАВА НАПРАВО
        default subpixel True 
        parallel:
            Null(540.0, 720.0)
            'jenek'
        parallel:
            xpos 1.5 
            linear 0.40 xpos 0.75

    image rmcj_spr_sleva: #ЖЕНЁК СЛЕВА НАЛЕВО
        default subpixel True 
        parallel:
            Null(540.0, 720.0)
            'jenek'
        parallel:
            xpos -1.5 
            linear 0.40 xpos 0.25

###COLDICK
    image cld_spr_sprava: #КОЛДИК СПРАВА НАПРАВО
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'coldspr1'
        parallel:
            xpos 3.0
            linear 0.80 xpos 0.75

    image cld_centr_sleva_leave: #КОЛДИК ЛИВАЕТ ИЗ ЦЕНТРА НАЛЕВО
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'coldspr'
        parallel:
            xpos 0.5
            linear 0.80 xpos -3.0
    
    image cld_spr_sleva: #КОЛДИК СЛЕВА НАЛЕВО
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'coldspr'
        parallel:
            xpos -3.0
            linear 0.80 xpos 0.25
    
    image cld_sleva_leave: #КОЛДИК ЛИВАЕТ СЛЕВА НАЛЕВО
        subpixel True default
        parallel:
            Null(500.0, 842.0)
            'coldspr'
        parallel:
            xpos 0.25
            linear 0.80 xpos -3.25

    image vilka_dostal_anim: # with Pause(0.50)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'vilka1'
        parallel:
            ypos 1.5 
            linear 0.33 ypos 1.0 
            linear 0.03 ypos 1.02

    image vilka_ubral_anim: # with Pause(0.50)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'vilka1'
        parallel:
            ypos 1.02
            linear 0.36 ypos 2.0

#DAY
    image aku_dostal_anim: # with Pause(0.50)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku1'
        parallel:
            ypos 1.5 
            linear 0.33 ypos 1.0 
            linear 0.03 ypos 1.02

    image aku_ubral_anim: # with Pause(0.50)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku1'
        parallel:
            ypos 1.02
            linear 0.36 ypos 1.5

    image aku_pricel_anim1: # with Pause(0.20)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku1'
        parallel:
            pos (0.5, 1.02) 
            linear 0.20 pos (0.4, 1.2) 

    image aku_pricel_anim2: # with Pause(0.20)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku2'
        parallel:
            pos (0.5, 1.2) 
            linear 0.20 pos (0.5, 1.0) 

    image aku_pricel_anim3: # with Pause(0.20)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku2'
        parallel:
            ypos 1.0 
            linear 0.20 ypos 1.2 

    image aku_pricel_anim4: # with Pause(0.20)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku1'
        parallel:
            pos (0.4, 1.2) 
            linear 0.20 pos (0.5, 1.02) 

    image aku_reload_anim1: # with Pause(0.10)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku1'
        parallel:
            ypos 1.02 
            linear 0.10 ypos 1.1 

    image aku_reload_anim2: # with Pause(0.10)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku3'
        parallel:
            ypos 1.1 
            linear 0.10 ypos 1.0 

    image aku_reload_anim3: # with Pause(0.10)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku3'
        parallel:
            ypos 1.0 
            linear 0.10 ypos 1.1 

    image aku_reload_anim4: # with Pause(0.10)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku4'
        parallel:
            ypos 1.1 
            linear 0.10 ypos 1.2 

    image aku_reload_anim5: # with Pause(0.10)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku3'
        parallel:
            ypos 1.2 
            linear 0.10 ypos 1.0 

    image aku_reload_anim6: # with Pause(0.30)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku6'
        parallel:
            xpos 0.5 
            linear 0.20 xpos 0.6 
            linear 0.20 xpos 0.5 
        parallel:
            ypos 1.0 
            linear 0.10 ypos 1.05 
            linear 0.10 ypos 1.0 
            linear 0.10 ypos 1.1 


    image aku_reload_anim7: # with Pause(0.10)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku1'
        parallel:
            ypos 1.1 
            linear 0.10 ypos 1.02 


    image aku_shoot_anim1: # with Pause(0.10)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku_sht'
        parallel:
            ypos 1.0 
            linear 0.10 ypos 1.1 

    image aku_shoot_anim2: # with Pause(0.10)
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'aku2'
        parallel:
            ypos 1.1 
            linear 0.10 ypos 1.0 


#DAY
    image pm_dostal_anim: # pause 0.49
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm1'
        parallel:
            ypos 1.5 
            linear 0.49 ypos 1.0 

    image pm_ubral_anim: # pause 0.49
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm1'
        parallel:
            ypos 1.0
            linear 0.49 ypos 1.5

    image pm_pricel_anim1: # pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm1'
        parallel:
            pos (0.5, 1.0) 
            linear 0.20 pos (0.4, 1.1) 

    image pm_pricel_anim2: # pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm2'
        parallel:
            ypos 1.1 
            linear 0.20 ypos 1.0 

    image pm_pricel_anim3: # pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm2'
        parallel:
            ypos 1.0 
            linear 0.20 ypos 1.1 

    image pm_pricel_anim4: # pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm1'
        parallel:
            pos (0.4, 1.1) 
            linear 0.20 pos (0.5, 1.0) 

    image pm_shoot_anim1: # pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm_sht'
        parallel:
            ypos 1.0 
            linear 0.10 ypos 1.15 

    image pm_shoot_anim2: # pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm2'
        parallel:
            ypos 1.15 
            linear 0.10 ypos 1.0 

    image pm_reolad_anim1: # pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm3'
        parallel:
            ypos 1.0 
            linear 0.25 ypos 1.15 

    image pm_reolad_anim2: # pause 0.2
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm3'
        parallel:
            ypos 1.15 
            linear 0.25 ypos 1.0
            linear 0.10 ypos 1.05

    image pm_reolad_anim3: # pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm4'
        parallel:
            ypos 1.05 
            linear 0.10 ypos 1.1
            linear 0.15 ypos 1.0

    image pm_reolad_anim4: # pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm5'
        parallel:
            ypos 1.0 
            linear 0.15 ypos 1.1 

    image pm_reolad_anim5: # pause 0.2
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm4'
        parallel:
            ypos 1.1 
            linear 0.15 ypos 1.0

    image pm_reolad_anim6: # pause 0.2
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'pm1'
        parallel:
            ypos 1.1 
            linear 0.20 ypos 1.0


    image overlaymenushki1: #pause 0.49
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'source/overlaymenushki1.png'
        parallel:
            ypos 1.6 alpha 0
            linear 0.3 ypos 1.0 alpha 1 

    image overlaymenushki11: #pause 0.49
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'source/overlaymenushki1.png'
        parallel:
            ypos 1.0 alpha 1
            linear 0.3 ypos 1.6 alpha 0

###ТОЗ-34

    image tozik_dostal_anim: #pause 0.49
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik1'
        parallel:
            ypos 1.6 
            linear 0.49 ypos 1.0 

    image tozik_ubral_anim: #pause 0.49
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik1'
        parallel:
            ypos 1.0 
            linear 0.49 ypos 1.6

    image tozik_pricel_anim1: #pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik1'
        parallel:
            pos (0.5, 1.0) 
            linear 0.10 pos (0.4, 1.1) 

    image tozik_pricel_anim2: #pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik2'
        parallel:
            ypos 1.1 
            linear 0.10 ypos 1.0 

    image tozik_pricel_anim3: #pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik2'
        parallel:
            ypos 1.0
            linear 0.10 ypos 1.1

    image tozik_pricel_anim4: #pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik1'
        parallel:
            pos (0.4, 1.1) 
            linear 0.10 pos (0.5, 1.0)

    image tozik_shoot_anim1: #pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik8'
        parallel:
            ypos 1.0 
            linear 0.10 ypos 1.1 

    image tozik_shoot_anim2: #pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik2'
        parallel:
            ypos 1.1 
            linear 0.10 ypos 1.0 

    image tozik_reload_anim1: #pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik1'
        parallel:
            ypos 1.0 
            linear 0.10 ypos 1.1 

    image tozik_reload_anim2: #pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik3'
        parallel:
            ypos 1.1 
            linear 0.10 ypos 1.0

    image tozik_reload_anim3: #pause 0.1
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik4'
        parallel:
            ypos 1.0
            linear 0.10 ypos 1.1
    
    image tozik_reload_anim4: #pause 0.2
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik5'
        parallel:
            ypos 1.1 xpos 0.5
            linear 0.10 ypos 1.0
            linear 0.10 xpos 0.55 

    image tozik_reload_anim5: #pause 0.2
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik6'
        parallel:
            ypos 1.0 xpos 0.55
            linear 0.10 ypos 1.1 
            linear 0.10 xpos 0.5

    image tozik_reload_anim6: #pause 0.2
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik7'
        parallel:
            ypos 1.1 xpos 0.5
            linear 0.10 ypos 1.0 xpos 0.55
            linear 0.10 xpos 0.5

    image tozik_reload_anim7: #pause 0.2
        default subpixel True 
        parallel:
            Null(1920.0, 1080.0)
            'tozik1'
        parallel:
            ypos 1.0
            linear 0.10 ypos 1.05
            linear 0.10 ypos 1.0

    image Fight_Ddv_Dun_png:
        'source/fight_png_01_LW0607.png' with dissolve
        pause (0.1)
        'source/fight_png_02_LW0607.png' with dissolve
        pause (0.1)
        repeat


    image coldherovo:
        'source/coldspr.png'
        zoom 1.0
        ease 1.0 xzoom 6.5
        ease 1.0 xzoom 13.1
        ease 1.0 xzoom 15.2
        ease 1.0 xzoom 3.2
        ease 1.0 xzoom 7.7
        ease 1.0 xzoom 14.2
        ease 1.0 xzoom 1.2
        ease 1.0 xzoom 17.45
        ease 1.0 xzoom 7.27
        ease 1.0 xzoom 8.2
        ease 1.0 xzoom 9.2
        ease 1.0 xzoom 1.0
        repeat

    image anim pizda_ot_skita:
        'int_bus_night' with poplil_pacan
        pause 8
        "int_bus_black" with poplil_pacan
        pause 8
        repeat

    image rageone:
        "et_rage1" with dissolve
        pause .6
        "et_rage2" with dissolve
        pause .6
        repeat

    image ragetwo:
        "et_rage1" with dissolve
        pause .6
        "et_rage2" with dissolve
        pause .6
        "et_rage3" with dissolve
        pause .6
        repeat

    image ragethree:
        "et_rage1" with dissolve
        pause .3
        "et_rage2" with dissolve
        pause .3
        "et_rage3" with dissolve
        pause .3
        "et_rage4" with dissolve
        pause .3
        repeat


    image unblink:
        contains:
            "source/blink_up.png"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "source/blink_down.png"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)

    image blink:
        contains:
            "source/blink_up.png"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "source/blink_down.png"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0

    image normalno_ebanulo:
        'source/babah1.png' with dissolve
        pause (0.1)
        'source/babah2.png' with dissolve
        pause (0.1)
        'source/babah3.png' with dissolve
        pause (0.1)
        'source/babah4.png' with dissolve
        pause (0.1)
        'source/babah5.png' with dissolve
        pause (0.1)
        'source/babah6.png' with dissolve
        pause (0.1)

    image aw_club_f:
        contains:
            choice:
                "aw_club_f1"
            choice:
                "aw_club_f2"
            choice:
                "aw_club_f3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_club_f1"
            choice:
                "aw_club_f2"
            choice:
                "aw_club_f3"
            alpha 0.25
            pause 0.15
            repeat
        contains:
            choice:
                "aw_club_f1"
            choice:
                "aw_club_f2"
            choice:
                "aw_club_f3"
            alpha 0.25
            pause 0.15
            repeat

    image anim br_smoke:
        contains:
            'source/br_smoke_1.png'
            xpos 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.5)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0
        contains:
            'source/br_smoke_2.png'
            xpos 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.6)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0
        contains:
            'source/br_smoke_3.png'
            xpos 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.7)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0
        contains:
            'source/br_smoke_4.png'
            xpos 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.8)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0
        contains:
            'source/br_smoke_5.png'
            xpos 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.9)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0

    image doshd:
        contains:
            "source/rain.png"
            xpos 0.5 ypos -1.0
        contains:
            "source/rain.png"
            xpos -0.5 ypos -1.0
        contains:
            "source/rain.png"
            xpos 0.5 ypos 0.0
        contains:
            "source/rain.png"
            xpos -0.5 ypos 0.0
        contains:
            "source/rain.png"
            xpos 0.5 ypos 1.0
        contains:
            "source/rain.png"
            xpos -0.5 ypos 1.0
        contains:
            "source/rain.png"
            xpos 0.5 ypos 2.0
        contains:
            "source/rain.png"
            xpos -0.5 ypos 2.0
        block:
            yanchor 1.0
            linear 0.3 yanchor 0.0
            repeat

    image tripsMVWWW777:
        'source/trip1MVWWW777.png' with dissolve
        pause (0.5)
        'source/trip2MVWWW777.png' with dissolve
        pause (0.5)
        'source/trip3MVWWW777.png' with dissolve
        pause (0.5)
        repeat

    image aom_wood:
        contains:
            choice:
                "wood_1"
            choice:
                "wood_2"
            choice:
                "wood_3"
            pause 0.05
            repeat
        contains:
            choice:
                "wood_1"
            choice:
                "wood_2"
            choice:
                "wood_3"
            alpha 0.25
            pause 0.05
            repeat
        contains:
            choice:
                "wood_1"
            choice:
                "wood_2"
            choice:
                "wood_3"
            alpha 0.25
            pause 0.05
            repeat