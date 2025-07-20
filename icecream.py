from manim import *

class Gola(ThreeDScene):
    def construct(self):

        self.set_camera_orientation(theta = PI/6, phi = PI/3)

        a1 = ThreeDAxes(
            x_range = [-10, 10, 2],
            y_range = [-10, 10, 2],
            z_range = [-10, 10, 2],
            x_length = 10,
            y_length = 10, 
            z_length = 7
        )
        labels = a1.get_axis_labels()

        cone1 = Cone(
            base_radius = 2,
            height = 5,
            direction = [0, 0, 1],
            fill_color = LIGHT_BROWN
        ).flip([0, 1, 0])

        mango = Sphere(
            center = [0, 0, 0],
            radius = 2,
            v_range = (PI/2, PI),
            resolution = (100, 100)
        ).set_color(YELLOW_E)

        chocolate = Sphere(
            center = [0, 1, 1],
            radius = 1.5,
            resolution = (100, 100)
        ).set_color(DARK_BROWN)

        pista = Sphere(
            center = [0, -1, 1],
            radius = 1.5,
            resolution = (100, 100)
        ).set_color(GREEN_B)

        cherry = Sphere(
            center = [0, 0, 2.5],
            radius = 0.35,
            resolution = (100, 100)
        ).set_color(RED_B)

        g1 = VGroup(cone1, mango, chocolate, pista, cherry)
        self.play(Create(g1))
        # self.begin_ambient_camera_rotation(rate = 0.5)
        # self.wait()
        # self.stop_ambient_camera_rotation()
