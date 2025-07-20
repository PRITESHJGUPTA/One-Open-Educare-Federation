from manim import *

class Wave(ThreeDScene):
    def construct(self):
        #self.set_camera_orientation(theta = PI/6, phi = PI/3)

        axes2d = Axes(
            x_range = [-10, 10],
            y_range = [-10, 10, 2],
            x_length = 12,
            y_length = 10,
            tips = False,
            x_axis_config = {
                "numbers_to_include": np.arange(-10, 11, 1)
            }
        )
        axes_labels = axes2d.get_axis_labels()

        time_tracker = ValueTracker(0)
        sin_wave = always_redraw(
            lambda: axes2d.plot(
                lambda x: np.sin(x - time_tracker.get_value()),color=BLUE))

        cos_wave = always_redraw(
            lambda: axes2d.plot(
                lambda x: np.cos(x - time_tracker.get_value()),color=RED))

        g1 = VGroup(axes2d, axes_labels)
        self.play(Create(g1))
        self.add(sin_wave, cos_wave)
        self.play(
            time_tracker.animate.set_value(10),
            run_time = 5,
            rate_func = linear
            )
        self.wait()