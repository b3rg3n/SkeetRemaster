# Nai @ Make Visual Novels - АВТОР ШЕЙДЕРОВ
init python:
# Variables Section


    colorOperations ="""
    uniform vec4 u_color;
    """
    intensityOperations ="""
    uniform float u_intensity;
    """
    toggleMode = """
    uniform float u_mode;
    """
   
    commonVars ="""
    //Commonly used variables in nearly all shaders.
    uniform sampler2D tex0;
    uniform float u_time;
    varying vec2 v_tex_coord;
    """
   
    aberrationVars="""
    uniform float u_aberrationAmount;
    """


    simulatedLightingVars ="""
        uniform vec3 u_back_light_color; // Color of the back light
        uniform vec3 u_fill_light_color; // Color of the fill light
        uniform vec3 u_key_light_color; // Color of the key light
        uniform vec2 u_back_light_direction; // Direction of the back light
        uniform vec2 u_back_light_position;
        uniform vec2 u_fill_light_direction; // Direction of the fill light
        uniform vec2 u_key_light_position; // Position of the key light
        uniform float u_back_light_intensity; // Intensity of the back light
        uniform float u_fill_light_intensity; // Intensity of the fill light
        uniform float u_key_light_intensity; // Intensity of the key light
        uniform float u_key_light_radius; // Radius of the key light
    """


    perlinShaderVars = """
    //Perlin Variables here
    uniform float u_warpIntensity;
    uniform float u_flipIntensity;
    uniform float u_speed;
    uniform float u_scale;
    uniform float u_flipScale;
    uniform float u_flipSpeed;
    uniform float u_fps;
    uniform float u_minSmooth;
    uniform float u_maxSmooth;
    """


# Functions Section


    hsvFunctions = """
    vec3 rgb2hsv(vec3 c) {
    vec4 K = vec4(0.0, -1.0 / 3.0, 2.0 / 3.0, -1.0);
    vec4 p = mix(vec4(c.bg, K.wz), vec4(c.gb, K.xy), step(c.b, c.g));
    vec4 q = mix(vec4(p.xyw, c.r), vec4(c.r, p.yzx), step(p.x, c.r));


    float d = q.x - min(q.w, q.y);
    float e = 1.0e-10;
    return vec3(abs(q.z + (q.w - q.y) / (6.0 * d + e)), d / (q.x + e), q.x);
    }


    vec3 hsv2rgb(vec3 c) {
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
    }
    """




    perlinFunctions = """
    //Perlin Noise functions here
     float rand(vec2 c)
    {
        return fract(sin(dot(c.xy, vec2(12.9898, 78.233))) *
                        43758.5453123);
    }


    float Perlin(vec2 x)
    {  
        vec2 index = floor(x);
        vec2 fractal = fract(x);
        //Points
        float a = rand(index);
        float b = rand(index + vec2(1.0, 0.0));
        float c = rand(index + vec2(0.0, 1.0));
        float d = rand(index + vec2(1.0, 1.0));
        //This is really just Smooth Stepping, but people say this way is more performative.
        vec2 blur = fractal * fractal * (3.0 - 2.0 * fractal);
        return mix(a, b, blur.x) +
            (c - a) * blur.y * (1.0 - blur.x) +
            (d - b) * blur.x * blur.y;
    }


    vec2 Noise2D(vec2 uv, float frame)
    {
        //Create Fractal Brownian Motion using Perlin noise generation
        //https://thebookofshaders.com/13/ is a great article on the method.
        //Frame isn't really accurate as a term, but it's consistent with our naming below.
        //It's really a function of the current frame multiplied against the designated speed.


        vec2 q = vec2(0);
        q.x = Perlin(uv);
        q.y = Perlin(uv + 1);


        vec2 r = vec2(0);
        r.x = Perlin( uv + 1.0*q + vec2(1.7,9.2)+ 0.15 * frame );
        r.y = Perlin( uv + 1.0*q + vec2(8.3,2.8)+ 0.126 * frame);
        return clamp(r, 0, 1);
    }


    """

   
    vhsShader="""
            vec2 uv = v_tex_coord;
            uv.x += sin(u_time * 0.5) * 0.12;
            uv.y += cos(u_time * 0.5) * 0.11;
            vec4 color = texture2D(tex0, v_tex_coord) * u_color;
            float scanline = fract(uv.y * 50.0) < 0.5 ? 0.95 : 1.0;
            color.rgb *= scanline;
            float alpha = texture2D(tex0, v_tex_coord).a;
            float noise = alpha > 0.0 ? fract(sin(dot(v_tex_coord + u_time, vec2(12.9898, 78.233))) * 43758.5453) : 0.0;
            color.rgb += noise * 0.1;
            gl_FragColor = vec4(color.r,color.g, color.b, color.a);
    """

    renpy.register_shader("MakeVisualNovels.VHS",
        variables=commonVars+colorOperations,
        fragment_300=vhsShader)


transform VHS(a, b, c, d): # ИЗ НАЗВАНИЯ ПОНЯТНО
    shader "MakeVisualNovels.VHS"
    u_color (a, b, c, d)