from manim import *

class Demo(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(theta = PI/6, phi = PI/3)

        a = ThreeDAxes(
            x_range = [-10, 10],
            y_range = [-10, 10],
            z_range = [-10, 10]
        )
        alabel = a.get_axis_labels()
        
        tracker = ValueTracker(0)
        def para(u, v):
            x = u
            y = v
            z = np.sin(x - tracker.get_value())
            return z
        
        trigplane = always_redraw(lambda: a.plot_surface(
            para,
            resolution = (25, 25),
            u_range = (-5, 5),
            v_range = (-5, 5),
            color = BLUE
        ))

        g1 = VGroup(a, alabel, trigplane)
        # self.add(g1)
        self.play(Create(g1))
        self.play(
            tracker.animate.set_value(10),
            run_time = 5,
            rate_func = linear
            )