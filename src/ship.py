import arcade
import defines

class Ship:
    def __init__(self, initial_x):
        self.x = initial_x
        self.dir = defines.directions.STOP
        self.speed = 5

    def show(self):
        arcade.draw_rectangle_filled(self.x, 10, 20, 20, arcade.color.WHITE)

    def move(self):
        self.x += self.dir*self.speed

    def set_dir(self, direction):
        self.dir = direction
