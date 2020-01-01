import arcade
import directions as d

class Ship:
    def __init__(self, initial_x):
        self.x = initial_x
        self.dir = d.directions.STOP
        self.speed = 5

    def show(self):
        arcade.draw_rectangle_filled(self.x, 10, 20, 20, arcade.color.WHITE)

    def move(self):
        self.x += self.dir
    
    def set_dir(self, direction):
        self.dir = direction*self.speed