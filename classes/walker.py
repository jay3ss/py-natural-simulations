"""Random Walker from Khan Academy's course on Natural Simulations"""


class Walker:
    def __init__(self, width, height, radius, update_cb):
        self.x_pos = int(width / 2)
        self.y_pos = int(height / 2)
        self.radius = int(radius)

        self.update = update_cb

    def walk(self):
        dx, dy = self.update()
        self.x += self.radius * dx
        self.y += self.radius * dy

    @property
    def x(self):
        return self.x_pos

    @x.setter
    def x(self, x):
        self.x_pos = x

    @property
    def y(self):
        return self.y_pos

    @y.setter
    def y(self, y):
        self.y_pos = y
