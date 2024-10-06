# ЧЕСТНО - Я УЖЕ НЕ ПОМНЮ, ГДЕ НАМУТИЛ
# ЕСЛИ НАЙДЁТСЯ РАЗРАБ ЭТОГО ШЕЙДЕРА - СТУКАНИТЕ В ЛС @b3rg3n
init python:

    def moving_camera(trans, st, at):
        if persistent.parallax:
            x, y = renpy.display.draw.get_mouse_pos()
            trans.xoffset = (x - config.screen_width / 2) * .05
            trans.yoffset = (y - config.screen_height / 2) * .05
        else:
            trans.xoffset = 0
            trans.yoffset = 0
        return 0

    renpy.register_shader('drunk', variables="""
        uniform sampler2D tex0;
        uniform vec2 u_model_size;
        varying vec2 v_uv;
        varying vec2 v_size;
        uniform float u_blur_radius;
        uniform float u_dark_radius;
    """, vertex_300="""
        v_uv = a_position.xy / u_model_size;
        v_size = u_model_size;
    """, fragment_300="""
        vec4 col = texture2D(tex0, v_uv);

        col += texture2D(tex0, v_uv + vec2(.0, -u_blur_radius) / v_size);
        col += texture2D(tex0, v_uv + vec2(.0, u_blur_radius) / v_size);
        col += texture2D(tex0, v_uv + vec2(-u_blur_radius, .0) / v_size);
        col += texture2D(tex0, v_uv + vec2(u_blur_radius, .0) / v_size);

        col /= 5.0;

        gl_FragColor = vec4(mix(col.rgb, vec3(0,0,0), max(distance(v_uv, vec2(.5,.5)) / sqrt(.5) - u_dark_radius, .0)), col.a);
    """)

transform blur_drunk_blya:
    parallel:
        parallax()
    parallel:
        shader 'drunk'
        u_blur_radius .0 u_dark_radius 1.0
        easein .5 u_blur_radius 4.5 u_dark_radius 3.5
        .1
        easeout .5 u_blur_radius 2.5 u_dark_radius 1.0
        .1
        easein .5 u_blur_radius 5.5 u_dark_radius 3.5
        .1
        easeout .5 u_blur_radius 3.5 u_dark_radius 1.0
        .1
        easein .5 u_blur_radius 7.5 u_dark_radius 3.5
        .1
        easeout .5 u_blur_radius 5.5 u_dark_radius 1.0
        .1
        easein .5 u_blur_radius 3.5 u_dark_radius 3.5
        .1
        easeout .5 u_blur_radius 1.5 u_dark_radius 1.0
        repeat

transform blur_drunk_blya_low:
    parallel:
        parallax()
    parallel:
        shader 'drunk'
        u_blur_radius .0 u_dark_radius 1.0
        easein .5 u_blur_radius 2.5 u_dark_radius 1.5
        .1
        easeout .5 u_blur_radius 1.5 u_dark_radius 1.0
        .1
        easein .5 u_blur_radius 1.5 u_dark_radius 1.5
        .1
        easeout .5 u_blur_radius 1.1 u_dark_radius 1.0
        .1
        easein .5 u_blur_radius 2.5 u_dark_radius 1.5
        .1
        easeout .5 u_blur_radius 1.5 u_dark_radius 1.0
        .1
        easein .5 u_blur_radius 2.0 u_dark_radius 1.5
        .1
        easeout .5 u_blur_radius 1.1 u_dark_radius 1.0
        repeat

transform blur_drunk_blya_lowest:
    parallel:
        parallax()
    parallel:
        shader 'drunk'
        u_blur_radius .0 u_dark_radius 1.0
        easein .5 u_blur_radius 1.5 u_dark_radius 1.5
        .1
        easeout .5 u_blur_radius 0.5 u_dark_radius 1.0
        .1
        easein .5 u_blur_radius 0.5 u_dark_radius 1.5
        .1
        easeout .5 u_blur_radius 0.1 u_dark_radius 1.0
        .1
        easein .5 u_blur_radius 1.5 u_dark_radius 1.5
        .1
        easeout .5 u_blur_radius 0.5 u_dark_radius 1.0
        .1
        easein .5 u_blur_radius 1.0 u_dark_radius 1.5
        .1
        easeout .5 u_blur_radius 0.1 u_dark_radius 1.0
        repeat

transform parallax:
    perspective True
    subpixel True
    function moving_camera