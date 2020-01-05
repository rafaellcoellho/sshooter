import arcade
from random import randrange
import defines

class Alien(arcade.Sprite):
    def __init__(self, initial_x, initial_y):
        super().__init__()

        base = ':resources:images/space_shooter/'
        texture_options = [
            'playerShip1_green.png',
            'playerShip2_orange.png',
            'playerShip3_orange.png'
        ]
        selected_texture = base + texture_options[randrange(0, 3, 1)]

        texture = arcade.load_texture(selected_texture, scale=0.35)
        self.textures.append(texture)
        self.set_texture(0)

        self.speed = 1
        self.angle = 180
        self.center_x = initial_x
        self.center_y = initial_y
        self.dir = defines.directions.RIGHT
    
    def update(self):
        self.center_x += self.dir*self.speed
    
    def shift_down(self):
        self.dir *= -1
        self.center_y -= 5
