from manim import *

class Demo(Scene):
    def add_x_labels(self):
        x_labels = [
            MathTex(r"\pi"), MathTex(r"2 \pi"),
            MathTex(r"3 \pi"), MathTex(r"4 \pi"),
        ]

        for i in range(len(x_labels)):
            x_labels[i].next_to(np.array([-1 + 2*i, 0, 0]), DOWN)
            self.add(x_labels[i])
            
    def construct(self):
        tracker = ValueTracker(0)

        axes1 = Axes(   
            x_range = [-1, 3],
            y_range = [-5, 5],
            x_axis_config = {"include_numbers": True},
        ).shift(LEFT*4).scale(.5)
        

        axes2 = Axes(
            x_range = [-1, 3],
            y_range = [-5, 5]
        ).shift(2 * UP + RIGHT * 4).scale(.5)

        axes3 = Axes(
            x_range = [-1, 3],
            y_range = [-5, 5]
        ).shift(2 * DOWN + RIGHT * 4).scale(.5)


        w1 = always_redraw(lambda: axes1.plot(lambda x: np.sin(5*x- tracker.get_value()), x_range = [-1, 3], color = RED))
        w2 = always_redraw(lambda: axes2.plot(lambda x : np.sin(x + 30*DEGREES - tracker.get_value()), color = TEAL))
        w3 = always_redraw(lambda: axes3.plot(lambda x: np.sin(x - 30*DEGREES - tracker.get_value()), color = GREEN))

        w1lab = axes1.get_graph_label(w1,
                                  label = "sin(x)",
                                  direction = 2*UP,
                                  x_val = -1.5,
                                  color = RED
                                  )
        w2lab = axes2.get_graph_label(w2,
                                  label = MathTex("sin(x + 30^{\\circ})"),
                                  direction = DOWN * 2,
                                  x_val = -1,
                                  color = TEAL)
        w3lab = axes3.get_graph_label(w3,
                                  label = MathTex("sin(x - 30^{\\circ})"),
                                  direction = UP * 2,
                                  x_val = 1,
                                  color = GREEN
                                  )
        

        axesgrp = VGroup(axes1, axes2, axes3)
        wavegrp = VGroup(w1, w2, w3, w1lab, w2lab, w3lab)
        self.add(axesgrp)
        self.play(Create(wavegrp))
        self.play(tracker.animate.set_value(10),
                  run_time = 5,
                  rate_func = linear
                  )