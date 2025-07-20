from manim import *

class Temp(ThreeDScene):
    def construct(self):
        # self.set_camera_orientation(theta = PI/3, phi = PI/3)

        a = ThreeDAxes(
            x_range = [-10, 10],
            y_range = [-10, 10],
            z_range = [-10, 10]
        )

        tracker = ValueTracker(0)

        w1 = always_redraw(lambda: a.plot(lambda x: np.sin(x- tracker.get_value()), color = RED))
        w2 = always_redraw(lambda: a.plot(lambda x : np.sin(x + 30*DEGREES - tracker.get_value()), color = TEAL))
        w3 = always_redraw(lambda: a.plot(lambda x: np.sin(x - 30*DEGREES - tracker.get_value()), color = GREEN))

        w1lab = a.get_graph_label(w1,
                                  label = "sin(x)",
                                  direction = UP,
                                  x_val = -10,
                                  color = RED
                                  )
        w2lab = a.get_graph_label(w2,
                                  label = MathTex("sin(x + 30^{\\circ})"),
                                  direction = DOWN * 2,
                                  x_val = -10,
                                  color = TEAL)
        w3lab = a.get_graph_label(w3,
                                  label = MathTex("sin(x - 30^{\\circ})"),
                                  direction = UP * 2,
                                  x_val = 10,
                                  color = GREEN
                                  )
        
        c1 = Circle()
        
        # g = VGroup(a, w1, w2, w3, w1lab, w2lab, w3lab)
        wavegrp = VGroup(w1, w2, w3, w1lab, w2lab, w3lab)

        self.add(a)
        self.play(Create(wavegrp))
        self.play(tracker.animate.set_value(10),
                  run_time = 5,
                  rate_func = linear
                  )
        # self.play(Transform(wavegrp, c1))
        # self.play(Create(c1))
        self.wait(2)