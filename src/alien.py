import arcade
from defines import directions as d

class Flower:
    def __init__(self, initial_x, initial_y):
        self.x = initial_x
        self.y = initial_y
        self.r = 30
        self.dir = d.directions.RIGHT

    def show(self):
        arcade.draw_circle_filled(self.x, self.y, self.r, arcade.color.BLUE)
