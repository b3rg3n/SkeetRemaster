init -1000 python:
    """
    // Author: mikolalysenko
    // License: MIT
    """
    renpy.register_shader("sgwni.dreamy", variables="""
        uniform sampler2D tex0;
        uniform sampler2D tex1;
        uniform float u_lod_bias;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;

        uniform float u_renpy_progress;
    """, fragment_functions="""
        vec2 offset(float progress, float x, float theta) {
            float phase = progress*progress + progress + theta;
            float shifty = 0.03*progress*cos(10.0*(progress+x));
            return vec2(0, shifty);
        }
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        float progress = u_renpy_progress;
        vec2 uv = v_tex_coord.st;

        gl_FragColor = mix(
            texture2D(tex0, uv + offset(progress, uv.x, 0.0), u_lod_bias),
            texture2D(tex1, uv + offset(1.0-progress, uv.x, 3.14), u_lod_bias),
            progress
        );
    """)

init -999 python:
    from renpy.display.transition import Transition, null_render, render
    class Dreamy(Transition):
        """
        :doc: transition function
        :args: (time=2.0, alpha=False, time_warp=None)
        :name: Dreamy

        Returns a transition that displays a dreamy wobble as it fades from the old scene to the new scene.

        `time`
            The time the transition will take.

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

        def __init__(self, time=2.0, old_widget=None, new_widget=None, alpha=False, time_warp=None, **properties):
            super(Dreamy, self).__init__(time, **properties)

            self.time = time
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
                rv.add_shader("sgwni.dreamy")
                rv.add_uniform("u_renpy_progress", complete)
                rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap)

            rv.blit(bottom, (0, 0), focus=False, main=False)
            rv.blit(top, (0, 0), focus=True, main=True)

            renpy.display.render.redraw(self, 0)

            return rv

    # Curry
    from renpy.curry import curry
    cDreamy = curry(Dreamy)


init -998:
    define dissdreamy = cDreamy(1)
