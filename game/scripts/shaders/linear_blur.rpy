init -1000 python:
    """
    // author: gre
    // license: MIT
    """
    renpy.register_shader("sgwni.linear_blur", variables="""
        uniform sampler2D tex0;
        uniform sampler2D tex1;
        uniform float u_lod_bias;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;

        uniform float u_renpy_progress;
        uniform float u_sgwni_intensity;
        uniform float u_sgwni_passes;
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        int passes = int(u_sgwni_passes);
        float intensity = u_sgwni_intensity;
        vec2 uv = v_tex_coord.st;

        vec4 c1 = vec4(0.0);
        vec4 c2 = vec4(0.0);

        float disp = intensity*(0.5-distance(0.5, u_renpy_progress));
        for (int xi=0; xi<passes; xi++)
        {
            float x = float(xi) / float(passes) - 0.5;
            for (int yi=0; yi<passes; yi++)
            {
                float y = float(yi) / float(passes) - 0.5;
                vec2 v = vec2(x,y);
                float d = disp;
                c1 += texture2D(tex0, uv + d*v, u_lod_bias);
                c2 += texture2D(tex1, uv + d*v, u_lod_bias);
            }
        }
        c1 /= float(passes*passes);
        c2 /= float(passes*passes);

        gl_FragColor = mix(c1, c2, u_renpy_progress);
    """)

init -999 python:
    from renpy.display.transition import Transition, null_render, render
    class LinearBlur(Transition):
        """
        :doc: transition function
        :args: (time, intensity=0.1, passes=10, alpha=False, time_warp=None)
        :name: LinearBlur

        Returns a transition that blurs the screen as it dissolves from the old scene to the new scene.

        `time`
            The time the transition will take.

        `intensity`
            Multiplier for the intensity of the blur.

        `passes`
            The number of passes the blur makes. A high enough number will always negatively impact performance.

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

        def __init__(self, time, intensity=0.1, passes=10, old_widget=None, new_widget=None, alpha=False, time_warp=None, **properties):
            super(LinearBlur, self).__init__(time, **properties)

            self.time = time
            self.passes = passes
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
                rv.add_shader("sgwni.linear_blur")
                rv.add_uniform("u_renpy_progress", complete)
                rv.add_uniform("u_sgwni_intensity", self.intensity)
                rv.add_uniform("u_sgwni_passes", self.passes)
                rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap)

            rv.blit(bottom, (0, 0), focus=False, main=False)
            rv.blit(top, (0, 0), focus=True, main=True)

            renpy.display.render.redraw(self, 0)

            return rv

    # Curry
    from renpy.curry import curry
    cLinearBlur = curry(LinearBlur)


init -998:
    define linearblur = cLinearBlur(0.2)
    define linearblurbolee = cLinearBlur(0.5)
    define linearblurfast = cLinearBlur(0.1)
