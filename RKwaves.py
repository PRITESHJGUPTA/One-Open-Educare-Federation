from manim import *

class Waves(ThreeDScene):
    def construct(self):
        a = ThreeDAxes(
            x_range = [-10, 10],
            y_range = [-10, 10],
            z_range = [-10, 10]
        )

        tracker = ValueTracker(0)
        w1 = always_redraw(lambda: a.plot(lambda x : np.sin(x - tracker.get_value()), color = RED))

        grp = VGroup(a, w1)
        self.play(Create(grp))
        self.play(tracker.animate.set_value(10),
                  run_time = 5,
                  rate_func = linear
                  )
        self.wait()