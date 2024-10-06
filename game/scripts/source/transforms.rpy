init:

    transform sr_main_menu_anim(x, y):# 0.1 или 0.9 | 0.5 или же...
        xalign x alpha 0
        ease 0.5 xalign y alpha 1
        on hover:
            easein 0.1 yoffset -2
        on idle:
            easein 0.1 yoffset 2

    transform sr_main_menu_anim1(x, y):# 0.1 или 0.9 | 0.5 или же...
        xalign x alpha 1
        ease 0.5 xalign y alpha 0
        on hover:
            easein 0.1 yoffset -2
        on idle:
            easein 0.1 yoffset 2

    transform sr_load_anim: # АНИМАЦИЯ МЕНЮ ЗАГРУЗКИ
        zoom 0.4 alpha 0
        ease 0.5 zoom 1.0 alpha 1
        on hover:
            easein 0.1 yoffset -2
        on idle:
            easein 0.1 yoffset 2

    transform sr_load_anim1: # АНИМАЦИЯ МЕНЮ ЗАГРУЗКИ
        on hover:
            easein 0.1 yoffset -2
        on idle:
            easein 0.1 yoffset 2

    transform sanek_vhod_v_masterskuyi:
        align(0.5, 0.5) zoom 1.0
        ease 2 align(0.6, 0.5) zoom 3.0

    transform sanek_baza_osmotr3:
        align(0.8, 0.75) zoom 3.0
        ease 3 align(0.5, 0.5) zoom 1.0

    transform sanek_baza_osmotr2:
        align(0.8, 0.4) zoom 3.0
        ease 2 align(0.8, 0.75) zoom 3.0

    transform sanek_baza_osmotr1:
        align(0.35, 0.35) zoom 3.0
        ease 2 align(0.8, 0.4) zoom 3.0

    transform sanek_baza_osmotr:
        align(0.5, 0.5) zoom 1.0
        ease 3 align(0.35, 0.35) zoom 3.0

    transform its_time_to_drop_vaz1:
        align(0.9, 0.7) zoom 3.0
        ease 3 align(0.5, 0.5) zoom 1.0

    transform its_time_to_drop_vaz:
        align (0.5, 0.5) zoom 1.0
        ease 3 align (0.9, 0.7) zoom 3.0

    transform spalil_nyashu_kotoraya_obossalas_ot_orgazma:
        align (0.1, 0.8) zoom 3.0
        ease 2 align (0.5, 0.5) zoom 1.0

    transform spalil_ndevstvennitsu_kotoroi_porval_pisechku:
        align (0.5, 0.5) zoom 1.0
        ease 1 align (0.1, 0.8) zoom 3.0

    transform spalil_nyashu_kotoraya_techet_ot_mishlenta:
        align (0.8, 0.0) zoom 3.0
        ease 2 align (0.5, 0.5) zoom 1.0

    transform spalil_nyashu_kotoraya_ne_breet_pizdu:
        align (0.5, 0.5) zoom 1.0
        ease 1 align (0.8, 0.0) zoom 3.0

    transform gayshit(z, e, x):
        xpos z alpha 0
        ease e xpos x alpha 1

    transform zaprignul_na_stol2:
        align (0.71, 0.65) zoom 3.0
        ease 2 align (0.5, 0.4) zoom 3.0

    transform zaprignul_na_stol1:
        align (0.5, 0.4) zoom 3.0
        ease 1 align (0.5, 0.5) zoom 1.0

    transform zaprignul_na_stol:
        align (0.5, 0.5) zoom 1.0
        ease 1 align (0.71, 0.65) zoom 3.0

    transform camera_zoom:
        align (0.5, 0.5) zoom 1.0
        ease 3 align (0.55, 0.1) zoom 3.0

    transform vadya_uletel_v_portal1:
        align (0.5, 0.9) zoom 3.0
        ease 3 align (0.5, 0.5) zoom 1.0

    transform vadya_uletel_v_portal:
        align (0.5, 0.5) zoom 1.0
        ease 1 align (0.5, 0.9) zoom 3.0

    transform vadya_smotrit_na_zabor:
        align (0.5, 0.5) zoom 1.0
        ease 2 align (0.1, 0.1) zoom 3.0
        ease 6 align (0.9, 0.1) zoom 3.0
        ease 6 align (0.1, 0.1) zoom 3.0
        ease 2 align (0.5, 0.5) zoom 1.0

    transform legendary_zoom_osmotr_bratkov:
        align (0.5, 0.5) zoom 1.0
        ease 2 align (0.1, 0.1) zoom 3.0
        parallel:
            ease 18 align (0.9, 0.1) zoom 3.0
            ease 18 align (0.1, 0.1) zoom 3.0
            repeat

    transform legendary_zoom_chc_out:
        align (0.1, 0.1) zoom 2.3
        ease 2 align (0.5, 0.5) zoom 1.0

    transform legendary_zoom_chc:
        align (0.5, 0.5) zoom 1.0
        ease 1 align (0.1, 0.1) zoom 2.3

    transform ivetta_say_go_sex_anim:
        align (0.5, 0.5) zoom 1.0
        ease 12 align (0.5, 0.4) zoom 3.0

    transform eva_kiss_anm:
        align (0.5, 0.5) zoom 1.0
        ease 1.5 align (0.5, 0.4) zoom 3.0

    transform vas_ocenka_anim:
        shader "MakeVisualNovels.VHS"
        u_color (0.83, 0.83, 0.77, 1.0)
        align (0.1, 0.1) zoom 2.0
        ease 6.0 align (0.9, 0.5) zoom 2.0
        ease 6.0 align (0.1, 0.9) zoom 2.0
        ease 6.0 align (0.5, 0.5) zoom 2.0
        ease 6.0 align (0.9, 0.9) zoom 2.0
        ease 6.0 align (0.5, 0.5) zoom 2.0

    transform sr_hidescreens:
        xpos 0.0 ypos 0.0 alpha 1.0 subpixel True
        ease 1.0 xpos 0.0 ypos 0.2 alpha 0.0

    transform sr_showscreens:
        ypos 0.2 alpha 0.0 subpixel True
        ease 1.0 ypos 0.0 alpha 1.0

    transform sr_null_transform:
        pause 0.01

    transform vas_ending_fb_anim:
        shader "MakeVisualNovels.VHS"
        u_color (0.83, 0.83, 0.77, 1.0)
        align (0.5, 0.5) zoom 1.0
        ease 18.0 align (0.5, 0.5) zoom 6.0

    transform vas_cumback_anim:
        shader "MakeVisualNovels.VHS"
        u_color (0.83, 0.83, 0.77, 1.0)
        align (0.5, 0.5) zoom 2.0
        ease 3.0 align (0.5, 0.5) zoom 1.0

    transform eva_osmotr_ebleta_i_top_tela2:
        align (0.5, 0.95) zoom 2.3
        ease 3 align (0.5, 0.5) zoom 1.0

    transform eva_osmotr_ebleta_i_top_tela1:
        align (0.5, 0.4) zoom 2.3
        ease 1.5 align (0.5, 0.95) zoom 2.3

    transform eva_osmotr_ebleta_i_top_tela:
        align (0.5, 0.5) zoom 1.0
        ease 3 align (0.5, 0.4) zoom 2.3

    transform vasya_kiss_anim:
        align (0.5, 0.5) zoom 1.0
        ease 4 align (0.9, 0.3) zoom 2.3

    transform legendary_zoom_podval15:
        align (0.5, 0.4) zoom 1.3
        ease 6 align (0.5, 0.3) zoom 3.3

    transform legendary_zoom_podval14:
        align (0.5, 0.5) zoom 1.0
        ease 1 align (0.5, 0.4) zoom 1.3

    transform legendary_zoom_podval13:
        align (0.5, 0.8) zoom 3.0
        ease 5 align (0.5, 0.5) zoom 1.0

    transform legendary_zoom_podval12:
        align (0.5, 0.5) zoom 1.0
        ease 1 align (0.5, 0.8) zoom 3.0

    transform legendary_zoom_podval11:
        align (0.65, 0.35) zoom 3.0
        ease 3.5 align (0.5, 0.5) zoom 1.0

    transform legendary_zoom_podval10:
        align (0.5, 0.5) zoom 1.0
        ease 1.7 align (0.65, 0.35) zoom 3.0

    transform legendary_zoom_podval9:
        align (0.5, 0.5) zoom 2.0
        ease 3 align (0.5, 0.5) zoom 1.0

    transform legendary_zoom_podval8:
        align (0.8, 0.8) zoom 3.7
        ease 3 align (0.9, 0.8) zoom 3.7

    transform legendary_zoom_podval7:
        align (0.8, 0.75) zoom 2.7
        ease 6 align (0.8, 0.8) zoom 3.7

    transform legendary_zoom_podval6:
        align (0.55, 0.75) zoom 2.7
        ease 1 align (0.8, 0.75) zoom 2.7

    transform legendary_zoom_podval5:
        align (0.55, 0.55) zoom 2.7
        ease 0.5 align (0.55, 0.75) zoom 2.7

    transform legendary_zoom_podval4:
        align (0.55, 0.4) zoom 2.7
        ease 0.5 align (0.55, 0.55) zoom 2.7

    transform legendary_zoom_podval3:
        align (0.25, 0.55) zoom 2.7
        ease 1 align (0.55, 0.4) zoom 2.7

    transform legendary_zoom_podval2:
        align (0.25, 0.35) zoom 2.7
        ease 0.5 align (0.25, 0.55) zoom 2.7

    transform legendary_zoom_podval1:
        align (0.25, 0.25) zoom 2.7
        ease 0.5 align (0.25, 0.35) zoom 2.7

    transform legendary_zoom_podval:
        align (0.5, 0.5) zoom 1
        ease 2 align (0.25, 0.25) zoom 2.7

    transform legendary_zoom_jenek:
        align (0.5, 0.5) zoom 1
        ease 1.2 align (0.45, 0.1) zoom 2.7

    transform ts_epic_fail_padenie:
        align (0.5, 0.5) zoom 1
        ease 0.5 align (0.5, 0.8) zoom 1.5

    transform ts_preferences_anim: # АНИМАЦИЯ МЕНЮ НАСТРОЕК
        zoom 0.4 alpha 0
        ease 0.5 zoom 1.0 alpha 1
        on hover:
            easein 0.1 yoffset -2
        on idle:
            easein 0.1 yoffset 2

    transform ts_preferences_anim2: # АНИМАЦИЯ МЕНЮ НАСТРОЕК
        zoom 0.4 alpha 0
        ease 0.5 zoom 1.0 alpha 1

    transform ts_preferences_anim1: # АНИМАЦИЯ МЕНЮ НАСТРОЕК
        on show:
            zoom 0.4 alpha 0
            ease 0.5 zoom 1.0 alpha 1
        on hide:
            zoom 1.0 alpha 1
            ease 0.5 zoom 0.4 alpha 0

    transform ts_punch(x=0,y=0): # ts_punch(-0.22) или ts_punch()
        anchor (0.5, 0.5)
        pos (0.5+x, 0.5+y)
        rotate 0
        parallel:
            ease 0.4 pos (0.75+x, 1.43+y)
        parallel:
            ease 0.5 rotate -90

    transform sr_pokachivanie:
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

    transform sr_pokachivanie_light:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.025
        parallel:
            ease 1.0 xalign 0.48
            ease 1.0 xalign 0.51
            repeat
        parallel:
            ease 1.5 rotate 1.1 zoom 1.041
            ease 1.5 rotate -1.2 zoom 1.035
            repeat

    transform heartbeat:
        heartbeat2(1)

    transform heartbeat2(m):
        truecenter
        parallel:
            0.144
            zoom 1.00 + 0.07 * m
            easein 0.250 zoom 1.00 + 0.04 * m
            easeout 0.269 zoom 1.00 + 0.07 * m
            zoom 1.00
            1.479
            repeat
        parallel:
            easeout_bounce 0.3 xalign 0.5 + 0.02 * m
            easeout_bounce 0.3 xalign 0.5 - 0.02 * m
            repeat

    transform ed_bus_move:
        choice:
            ease 0.02 pos (0.001, 0.001)
            ease 0.02 pos (0, 0)
        choice:
            ease 0.02 pos (-0.001, 0.001)
            ease 0.02 pos (0, 0)
        choice:
            ease 0.02 pos (0.001, 0.001)
            ease 0.02 pos (0, 0.001)
        choice:
            ease 0.02 pos (-0.001, 0.001)
            ease 0.02 pos (0, 0.001)
        repeat

    transform aw_dance_2:
        parallel:
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            ease 0.6 zoom 1.04 xpos 0.5 ypos 0.49
        parallel:
            ease 0.6 xpos 0.5 ypos 0.49
            ease 0.6 xpos 0.48 ypos 0.51
            ease 0.6 xpos 0.5 ypos 0.49
            ease 0.6 xpos 0.52 ypos 0.51
            repeat

    transform aw_master_tryas:
        xalign 0.5 yalign 0.5
        parallel:
            ease 0.25 zoom 1.1
            ease 0.5 zoom 1.0
        parallel:
            ease 0.25 rotate -1.5
            ease 0.25 rotate 1.0
            ease 0.25 rotate 0.0

    transform ed_get_achievement:
        pos (0.2, 0.8)
        anchor (0.5, 0.5)
        zoom 0.0
        ease 1.5 zoom 1.05
        ease 0.25 zoom 0.95
        ease 0.25 zoom 1.0
        pause 4.0
        ease 0.5 pos (-0.8, 0.85)
        ease 0.5 pos (-1.0, 0.85) alpha 0.0

    transform ed_running_fast:
        truecenter
        zoom 1.25
        parallel:
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.25 rotate -0.75
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.35 rotate -0.75
            repeat
        parallel:
            ease 0.25 xpos 0.495
            ease 0.20 xpos 0.505
            repeat
        parallel:
            ease 0.25 ypos 0.495
            ease 0.30 ypos 0.505
            repeat

    transform spizdil:
        anchor (0.5, 0.5)
        ypos -0.3
        xpos 0.5
        linear 3.0 ypos 0.5

    transform aw_heartattack(img):


        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 1.10
            repeat
        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 0.90
            repeat
        contains:
            "blood"
            alpha 0.0
            block:
                ease 0.25 alpha 1.0
                ease 0.75 alpha 0.75
                repeat
    python:
        def Aw_HeartAttack(img):
            renpy.show(img, tag="bg2", at_list=[aw_heartattack(img)])

    transform aw_alko(img):


        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 1.10
            repeat
        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 0.90
            repeat

    python:
        def Aw_Alko(img):
            renpy.show(img, tag="bg2", at_list=[aw_alko(img)])

    transform mnd_chapter_anim:
        block:
            parallel:
                parallel:
                    choice:
                        xanchor 0.2
                    choice:
                        xanchor 0.3
                    choice:
                        xanchor 0.4
                    choice:
                        xanchor 0.5
                    choice:
                        xanchor 0.6
                    choice:
                        xanchor 0.7
                    choice:
                        xanchor 0.8
                parallel:
                    choice:
                        yanchor 0.2
                    choice:
                        yanchor 0.3
                    choice:
                        yanchor 0.4
                    choice:
                        yanchor 0.5
                    choice:
                        yanchor 0.6
                    choice:
                        yanchor 0.7
                    choice:
                        yanchor 0.8
            parallel:
                choice:
                    rotate -2
                choice:
                    rotate -1
                choice:
                    rotate 0
                choice:
                    rotate 1
                choice:
                    rotate 2
            parallel:
                choice:
                    alpha 1.0
                choice:
                    alpha 0.9
                choice:
                    alpha 0.8
                choice:
                    alpha 0.7
                choice:
                    alpha 0.6
                choice:
                    alpha 0.5
                choice:
                    alpha 0.4
            pause 0.02
            repeat 20
        block:
            parallel:
                parallel:
                    choice:
                        xanchor 0.498
                    choice:
                        xanchor 0.5
                    choice:
                        xanchor 0.502
                parallel:
                    choice:
                        yanchor 0.498
                    choice:
                        yanchor 0.5
                    choice:
                        yanchor 0.502
            parallel:
                choice:
                    rotate -0.2
                choice:
                    rotate -0.1
                choice:
                    rotate 0
                choice:
                    rotate 0.1
                choice:
                    rotate 0.2
            parallel:
                choice:
                    alpha 1.0
                choice:
                    alpha 0.9
                choice:
                    alpha 0.8
            pause 0.02
            repeat

    python:
        style.mnd_chapter_text.font = "source/fonts/Surfbars.otf"
        style.mnd_chapter_text.xalign = 0.5
        style.mnd_chapter_text.yalign = 0.5
        style.mnd_chapter_text.size = 100    
        style.mnd_chapter_text.color = "#ffffff"

        def MND_Chapter(name, time=3):
            renpy.show_screen("mnd_chapter", name)
            renpy.pause(time-0.4, hard=True)
            renpy.hide("mnd_chapter", layer="screens")
            renpy.show_screen("mnd_chapter", name)
            renpy.pause(0.4, hard=True)
            renpy.hide("mnd_chapter", layer="screens")

screen mnd_chapter(name):
    text name:
        style "mnd_chapter_text"
        at mnd_chapter_anim
