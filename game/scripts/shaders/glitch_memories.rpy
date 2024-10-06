init -1000 python:
    """
    // author: Gunnar Roth
    // based on work from natewave
    // license: MIT
    """
    renpy.register_shader("sgwni.glitch_memories", variables="""
        uniform sampler2D tex0;
        uniform sampler2D tex1;
        uniform float u_lod_bias;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;

        uniform float u_renpy_progress;
        uniform float u_sgwni_intensity;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        float intensity = u_sgwni_intensity;
        vec2 p = v_tex_coord.st;

        // Effect code
        vec2 block = floor(p.xy / vec2(16));
        vec2 uv_noise = block / vec2(64);
        uv_noise += floor(vec2(u_renpy_progress) * vec2(1200.0, 3500.0)) / vec2(64);
        vec2 dist = u_renpy_progress > 0.0 ? (fract(uv_noise) - 0.5) * 0.3 *(1.0 - u_renpy_progress) : vec2(0.0);
        vec2 red = p + dist * 0.2 * intensity;
        vec2 green = p + dist * .3 * intensity;
        vec2 blue = p + dist * .5 * intensity;

        gl_FragColor = vec4(
            mix(texture2D(tex0, red, u_lod_bias), texture2D(tex1, red, u_lod_bias), u_renpy_progress).r,
            mix(texture2D(tex0, green, u_lod_bias), texture2D(tex1, green, u_lod_bias), u_renpy_progress).g,
            mix(texture2D(tex0, blue, u_lod_bias), texture2D(tex1, blue, u_lod_bias), u_renpy_progress).b,
            1.0
        );
    """)

init -999 python:
    from renpy.display.transition import Transition, null_render, render
    class GlitchMemories(Transition):
        """
        :doc: transition function
        :args: (time, intensity=0.2, alpha=False, time_warp=None)
        :name: GlitchMemories

        Returns a transition that creates a glitch effect as it dissolves from the old scene to the new scene.

        `time`
            The time the transition will take.

        `intensity`
            Multiplier for the intensity of the glitch effect.

        `alpha`
            Ignored.

        `time_warp`
            A function that adjusts the timeline. If not None, this should be a
            function that takes a fractional time between 0.0 and 1.0, and returns
            a number in the same range.
        """

        __version__ = 1

        def after_upgrade(self, version):
            if version < 1:
                self.alpha = False

        time_warp = None

        def __init__(self, time, intensity=0.2, old_widget=None, new_widget=None, alpha=False, time_warp=None, **properties):
            super(GlitchMemories, self).__init__(time, **properties)

            self.time = time
            self.intensity = intensity
            self.old_widget = old_widget
            self.new_widget = new_widget
            self.events = False
            self.alpha = alpha
            self.time_warp = time_warp

        def render(self, width, height, st, at):

            if renpy.game.less_updates:
                return null_render(self, width, height, st, at)

            if st >= self.time:
                self.events = True
                return render(self.new_widget, width, height, st, at)

            complete = min(1.0, st / self.time)

            if self.time_warp is not None:
                complete = self.time_warp(complete)

            bottom = render(self.old_widget, width, height, st, at)
            top = render(self.new_widget, width, height, st, at)

            width = min(top.width, bottom.width)
            height = min(top.height, bottom.height)

            rv = renpy.display.render.Render(width, height)

            rv.operation = renpy.display.render.DISSOLVE
            rv.operation_alpha = self.alpha or renpy.config.dissolve_force_alpha
            rv.operation_complete = complete

            if renpy.display.render.models:

                target = rv.get_size()

                if top.get_size() != target:
                    top = top.subsurface((0, 0, width, height))
                if bottom.get_size() != target:
                    bottom = bottom.subsurface((0, 0, width, height))

                rv.mesh = True
                rv.add_shader("sgwni.glitch_memories")
                rv.add_uniform("u_renpy_progress", complete)
                rv.add_uniform("u_sgwni_intensity", self.intensity)
                rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap)

            rv.blit(bottom, (0, 0), focus=False, main=False)
            rv.blit(top, (0, 0), focus=True, main=True)

            renpy.display.render.redraw(self, 0)

            return rv

    # Curry
    from renpy.curry import curry
    cGlitchMemories = curry(GlitchMemories)


init -998:
    define memglitch = cGlitchMemories(0.2)
    define memglitchstr = cGlitchMemories(2.0)
    define memglitchbolee = cGlitchMemories(0.5)