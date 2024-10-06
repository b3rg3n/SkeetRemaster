init -1000 python:
    """
    // Author: Zeh Fernando
    // License: MIT
    """
    renpy.register_shader("sgwni.dreamy_zoom", variables="""
        uniform sampler2D tex0;
        uniform sampler2D tex1;
        uniform float u_lod_bias;
        attribute vec2 a_tex_coord;
        varying vec2 v_tex_coord;
        uniform vec2 res0;

        uniform float u_renpy_progress;
        uniform float u_sgwni_rotation;
        uniform float u_sgwni_scale;
    """, fragment_functions="""
        #define DEG2RAD 0.03926990816987241548078304229099 // 1/180*PI
        #define white_duration 0.1
    """, vertex_200="""
        v_tex_coord = a_tex_coord;
    """, fragment_200="""
        float progress = u_renpy_progress;
        float rotation = u_sgwni_rotation;
        float ratio = res0.x / res0.y;
        float scale = u_sgwni_scale;
        vec2 uv = v_tex_coord.st;

        // Massage parameters
        float phase = progress < 0.5 ? progress * 2.0 : (progress - 0.5) * 2.0;
        float angleOffset = progress < 0.5 ? mix(0.0, rotation * DEG2RAD, phase) : mix(-rotation * DEG2RAD, 0.0, phase);
        //float angleOffset = progress < 0.5 ? mix(0.0, rotation * DEG2RAD, phase) : mix(rotation * DEG2RAD, 0.0, phase);
        float newScale = progress < 0.5 ? mix(1.0, scale, phase) : mix(scale, 1.0, phase);

        vec2 center = vec2(0, 0);

        // Calculate the source point
        vec2 assumedCenter = vec2(0.5, 0.5);
        vec2 p = (uv.xy - vec2(0.5, 0.5)) / newScale * vec2(ratio, 1.0);

        // This can probably be optimized (with distance())
        float angle = atan(p.y, p.x) + angleOffset;
        float dist = distance(center, p);
        p.x = cos(angle) * dist / ratio + 0.5;
        p.y = sin(angle) * dist + 0.5;
        vec4 c = progress < 0.5 ? texture2D(tex0, p, u_lod_bias) : texture2D(tex1, p, u_lod_bias);

        // Finally, apply the color
        gl_FragColor = c + (
            progress < (0.5 - white_duration)
                ? mix(0.0, 1.0, phase + white_duration * 2.0)
                : progress > (0.5 + white_duration)
                ? mix(1.0, 0.0, phase - white_duration * 2.0)
                : 1.0
        );
    """)

init -999 python:
    from renpy.display.transition import Transition, null_render, render
    class DreamyZoom(Transition):
        """
        :doc: transition function
        :args: (time, rotation=6.0, scale=1.2, alpha=False, time_warp=None)
        :name: DreamyZoom

        Returns a transition that zooms, rotates, and fades to white from the old scene to the new scene.

        `time`
            The time the transition will take.

        `rotation`
            How many degrees of rotation to apply to the scene during the transition.

        `scale`
            How much to scale the scene during the transition.

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

        def __init__(self, time, rotation=6.0, scale=1.2, old_widget=None, new_widget=None, alpha=False, time_warp=None, **properties):
            super(DreamyZoom, self).__init__(time, **properties)

            self.time = time
            self.rotation = rotation
            self.old_widget = old_widget
            self.new_widget = new_widget
            self.events = False
            self.scale = scale
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
                rv.add_shader("sgwni.dreamy_zoom")
                rv.add_uniform("u_renpy_progress", complete)
                rv.add_uniform("u_sgwni_rotation", self.rotation)
                rv.add_uniform("u_sgwni_scale", self.scale)
                rv.add_property("mipmap", renpy.config.mipmap_dissolves if (self.style.mipmap is None) else self.style.mipmap)

            rv.blit(bottom, (0, 0), focus=False, main=False)
            rv.blit(top, (0, 0), focus=True, main=True)

            renpy.display.render.redraw(self, 0)

            return rv

    # Curry
    from renpy.curry import curry
    cDreamyZoom = curry(DreamyZoom)


init -998:
    define dreamyzoom = cDreamyZoom(1)
