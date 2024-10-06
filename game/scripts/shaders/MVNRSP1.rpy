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


# Shader Meat


    aAberrationShader = """
        vec2 uv = v_tex_coord;        
        float offset =  cos(u_time * 1.3 * 3.14159) * (u_aberrationAmount * 0.001) ;
        vec2 redUV = uv + vec2(offset, 0);
        vec2 greenUV = uv;
        vec2 blueUV = uv - vec2(offset, 0);
        vec2 alphaUV = uv;


        vec4 red = texture2D(tex0, redUV);
        vec4 green = texture2D(tex0, greenUV);
        vec4 blue = texture2D(tex0, blueUV);
        vec4 alpha = texture2D(tex0, alphaUV);


        gl_FragColor = vec4(red.r, green.g, blue.b, alpha.a);
        """


    sAberationShader = """
        vec2 uv = v_tex_coord;        
        float offset =  u_aberrationAmount * 0.001;
        vec2 redUV = uv + vec2(offset, 0);
        vec2 greenUV = uv;
        vec2 blueUV = uv - vec2(offset, 0);
        vec2 alphaUV = uv;


        vec4 red = texture2D(tex0, redUV);
        vec4 green = texture2D(tex0, greenUV);
        vec4 blue = texture2D(tex0, blueUV);
        vec4 alpha = texture2D(tex0, alphaUV);


        gl_FragColor = vec4(red.r, green.g, blue.b, alpha.a);


    """
   
    colorDepth16Shader="""
        vec2 uv = v_tex_coord;
        vec4 color = texture2D(tex0, uv);
        color.rgb = floor(color.rgb * 4) / 4;
        if (color.a == 0 ) discard;
        color += vec4(0.125,0.125,0.125, 0);
        color.rgb = floor(color.rgb * 8) / 8;
        gl_FragColor = color;
   """


    colorDepth256Shader="""
        vec2 uv = v_tex_coord;
        vec4 color = texture2D(tex0, uv);
        color.rgb = floor(color.rgb * 8) / 8;
        gl_FragColor = color;
    """
   
    mangaStyleShader="""
        vec4 col = texture2D(tex0, v_tex_coord);
        if (col.a == 0) discard;
        vec3 hsv = rgb2hsv(col.rgb);
        if (hsv.z < u_intensity || hsv.y < 0.0025) {  // Adjust the thresholds as needed
        col *= vec4(0.01,0.01,0.01,1.0);
        } else {
        col= u_color;
        }
        gl_FragColor = col;
    """
   
    staticNoiseShader="""
        vec2 uv = v_tex_coord;
        vec4 colorShift = vec4(0.9, 0.7, 1.0, 1.0);
            uv.x += sin(u_time * 0.5) * 0.12;
            uv.y += cos(u_time * 0.5) * 0.11;
            vec4 color = texture2D(tex0, v_tex_coord) * u_color;
            //float scanline = fract(uv.y * 50.0) < 0.5 ? 0.95 : 1.0;
            //color.rgb *= scanline;
            float alpha = texture2D(tex0, v_tex_coord).a;
            float brightFactor = 1.0 - u_mode;
            float darkFactor = u_mode;
            float staticValue = alpha > 0.0 ? fract(sin(dot(v_tex_coord + u_time, vec2(12.9898, 78.233))) * 43758.5453) : 0.0;
            float noise = smoothstep(0.0, u_intensity, staticValue);
            // Adjust operation based on u_operation: 0 for bright static, 1 for dark static


            //if mode is 0 bright factor is 1
            color.rgb = ((color.rgb + noise * brightFactor) + (color.rgb * noise * darkFactor)) - color.rgb * (1 - brightFactor);
            gl_FragColor = vec4(color.r,color.g, color.b, color.a);
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


    simulatedLightingShader = """
        vec2 uv = v_tex_coord;
        vec4 color = texture2D(tex0, uv);
        if(color.a < 0.01) discard; //Gross but I'm lazy.
        // Back lighting
        float edge_factor = 1.0 - smoothstep(0.0, 0.05, min(uv.x, 1.0 - uv.x) * min(uv.y, 1.0 - uv.y));
        vec2 to_light = normalize(uv - u_back_light_position);
        float back_light = max(dot(to_light, u_back_light_direction), 0.0);
        vec3 back_light_contribution = u_back_light_color * back_light * u_back_light_intensity * edge_factor;
        // Fill lighting.  Really it's a fill shadow, because screen lighting and meat space lighting work differently
        vec3 fill_light_contribution = u_fill_light_color * u_fill_light_intensity;
        // Key lighting
        float key_light_distance = distance(uv, u_key_light_position);
        float key_light_intensity = smoothstep(u_key_light_radius, 0.0, key_light_distance);
        vec3 key_light_contribution = u_key_light_color * key_light_intensity * u_key_light_intensity;
        // Combine lighting contributions, but also respect the original color's alpha because that's how we roll.
        vec3 final_color = (color.rgb + fill_light_contribution + back_light_contribution + key_light_contribution) * color.a;
        
        // Output the final color
        gl_FragColor = vec4(final_color, color.a);
    """


    warpFragmentShader = """
    //Fragment Shader Code here.


    //Set the rate of change for this effect.
    float frame = floor(u_time * (u_fps));
   
    //Get coordinates between 0 and 1
    vec2 uv = v_tex_coord.st;


    //Create Distortion using Perlin Noise
    vec2 distort = Noise2D(uv * u_scale, frame * u_speed);


    //Center the effect.  
    //Probably should consider centering the UV instead of this, but it works as is.
    distort = distort * 2 - 1;
   
    //Smoothing to help remove hard edges from the main warp.
    distort = smoothstep(u_minSmooth, u_maxSmooth, distort);  
   
    //Create another distortion to create bouncing edges.
    vec2 invertDistort = Noise2D(uv * u_flipScale, frame * u_flipSpeed);
   
    //This makes the effect invert itself every other frame, creating the edge adjustments.
    //Thanks Endiment for the assist on optimizing this!
    float frameMod = step(mod(frame, 2), 0.01);
    invertDistort = (invertDistort * (1-frameMod)) + ((1-invertDistort) * frameMod);
   
    //Also centered, should probably just consider making a centered UV for the noise effect.
    invertDistort = invertDistort * 2. - 1.;  
    //Deliberately did NOT smooth the invert to keep its jagged edges.
   
    //The dampening needs to be fairly severe based on the normal Perlin noise calculations.
    //We converted them into intensity variables to make them more accessible to manage for script writers.
    vec2 distortedUV = uv + distort * (u_warpIntensity * 0.0001) + invertDistort * (u_flipIntensity * 0.0001);
   


    vec4 color = texture2D(tex0, distortedUV);
    //Uncomment to visualize the noise using the provided settings.
    //color = vec4(1,1,1,1); // White
    //vec3 biLamp = vec3(distort.x * 0.2 + 0.5, 0, distort.y * 0.2 + 0.5);
    //color.rgb *= mix(vec3(1.), biLamp, 1);
   
    //Uncomment to visualize the inverted noise using the provided settings
    //This produces rapid flashing, so uncomment with caution.
    //color = vec4(1,1,1,1); //White
    //vec3 lavaLamp = vec3(invertDistort.x * 0.2 + 0.5, invertDistort.y * 0.2 + 0.5, 1);
    //color.rgb *= mix(vec3(1.), lavaLamp, 1);


    gl_FragColor = color;
    """


    TakeOnMeFragmentShader = """
    //Fragment Shader Code here.


    //Set the rate of change for this effect.
    float frame = floor(u_time * (u_fps));
   
    //Get coordinates between 0 and 1
    vec2 uv = v_tex_coord.st;


    //Create Distortion using Perlin Noise
    vec2 distort = Noise2D(uv * u_scale, frame * u_speed);


    //Center the effect.  
    //Probably should consider centering the UV instead of this, but it works as is.
    distort = distort * 2 - 1;
   
    //Smoothing to help remove hard edges from the main warp.
    distort = smoothstep(u_minSmooth, u_maxSmooth, distort);  
   
    //Create another distortion to create bouncing edges.
    vec2 invertDistort = Noise2D(uv * u_flipScale, frame * u_flipSpeed);
   
    //This makes the effect invert itself every other frame, creating the edge adjustments.
    //Thanks Endiment for the assist on optimizing this!
    float frameMod = step(mod(frame, 2), 0.01);
    invertDistort = (invertDistort * (1-frameMod)) + ((1-invertDistort) * frameMod);
   
    //Also centered, should probably just consider making a centered UV for the noise effect.
    invertDistort = invertDistort * 2. - 1.;  
    //Deliberately did NOT smooth the invert to keep its jagged edges.
   
    //The dampening needs to be fairly severe based on the normal Perlin noise calculations.
    //We converted them into intensity variables to make them more accessible to manage for script writers.
    vec2 distortedUV = uv + distort * (u_warpIntensity * 0.0001) + invertDistort * (u_flipIntensity * 0.0001);
   


    vec4 color = texture2D(tex0, distortedUV);
    //Uncomment to visualize the noise using the provided settings.
    //color = vec4(1,1,1,1); // White
    //vec3 biLamp = vec3(distort.x * 0.2 + 0.5, 0, distort.y * 0.2 + 0.5);
    //color.rgb *= mix(vec3(1.), biLamp, 1);
   
    //Uncomment to visualize the inverted noise using the provided settings
    //This produces rapid flashing, so uncomment with caution.
    //color = vec4(1,1,1,1); //White
    //vec3 lavaLamp = vec3(invertDistort.x * 0.2 + 0.5, invertDistort.y * 0.2 + 0.5, 1);
    //color.rgb *= mix(vec3(1.), lavaLamp, 1);
   
    if (color.a == 0) discard;
    vec3 hsv = rgb2hsv(color.rgb);


    if (hsv.z < u_intensity || hsv.y < 0.0025) {  // Adjust the thresholds as needed
        color *= vec4(0.01,0.01,0.01,1.0);
    } else {
    color= u_color; //Set fill color to the supplied color
}
    gl_FragColor = color;
    """


    #Shader Registration


    renpy.register_shader("MakeVisualNovels.PerlinWarp",
        variables=commonVars+perlinShaderVars,
        vertex_functions="",
        fragment_functions=perlinFunctions,
        vertex_200="",
        fragment_200=warpFragmentShader)


    renpy.register_shader("MakeVisualNovels.AnimatedAberration",
        variables=commonVars+aberrationVars,
        vertex_functions="",
        fragment_functions="",
        vertex_200="",
        fragment_200=aAberrationShader)


    renpy.register_shader("MakeVisualNovels.StillAberration",
        variables=commonVars+aberrationVars,
        vertex_functions="",
        fragment_functions="",
        vertex_200="",
        fragment_200=sAberationShader)


    renpy.register_shader("MakeVisualNovels.256colors",
    variables=commonVars,
    vertex_functions="",
    fragment_functions="",
    vertex_200="",
    fragment_200=colorDepth256Shader)
   
    renpy.register_shader("MakeVisualNovels.16colors",
    variables=commonVars,
    vertex_functions="",
    fragment_functions="",
    vertex_200="",
    fragment_200=colorDepth16Shader)
   
    #lmao
    renpy.register_shader("MakeVisualNovels.TakeOnMe",
        variables=commonVars+perlinShaderVars+intensityOperations+colorOperations,
        vertex_functions="",
        fragment_functions=perlinFunctions+hsvFunctions,
        vertex_200="",
        fragment_200=TakeOnMeFragmentShader)
   
    renpy.register_shader("MakeVisualNovels.VHS",
        variables=commonVars+colorOperations,
        fragment_300=vhsShader)


    renpy.register_shader("MakeVisualNovels.Static",
        variables=commonVars+colorOperations+intensityOperations+toggleMode,
        fragment_300=staticNoiseShader)


    renpy.register_shader("MakeVisualNovels.SimulatedLighting",
        variables=commonVars+simulatedLightingVars,
        fragment_300=simulatedLightingShader)

    renpy.register_shader("MakeVisualNovels.Manga",
        variables=commonVars+intensityOperations+colorOperations,
        vertex_functions="",
        fragment_functions=hsvFunctions,
        vertex_200="",
        fragment_200=mangaStyleShader)








