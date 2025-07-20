from manim import *

class Wave(ThreeDScene):
    def construct(self):
        axes2d = Axes(
            x_range=[-10, 10],
            y_range=[-2, 2, 1],
            x_length=12,
            y_length=4,
            tips=False,
            axis_config={"color": WHITE}
        )

        axes_labels = axes2d.get_axis_labels()

        # Time tracker for animation
        time_tracker = ValueTracker(0)

        # Function to generate the wave dynamically
        def wave_function(x):
            return np.sin(x - time_tracker.get_value())

        wave = always_redraw(lambda: axes2d.plot(wave_function, color=BLUE))

        self.play(Create(axes2d), Create(axes_labels))
        self.add(wave)

        # Animate the wave moving
        self.play(time_tracker.animate.set_value(10), run_time=5, rate_func=linear)

        self.wait()
