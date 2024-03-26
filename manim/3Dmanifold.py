from manim import *

class SphereScene(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        sphere = Surface(
            lambda u, v: np.array([
                1.5*np.cos(u)*np.cos(v),
                1.5*np.cos(u)*np.sin(v),
                1.5*np.sin(u)
            ]), v_range=[0, TAU], u_range=[-PI / 2, PI / 2], checkerboard_colors=[RED_D, RED_E],
            resolution=(15, 32)).fade(0.5) #Resolution of the sphere

        plane = Square(side_length=3, fill_opacity=0.5, fill_color=BLUE)
        plane.rotate(PI / 2, axis=RIGHT)
        plane.shift(1.5 * OUT + 0.5 * IN)

        self.play(Create(sphere))
        self.play(Create(plane))
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(10)

# This was created using Bing Copilot