import arcade
import defines

class Ship(arcade.Sprite):
    def __init__(self):
        super().__init__()

        texture = arcade.load_texture(':resources:images/space_shooter/playerShip1_orange.png', scale=0.35)
        self.textures.append(texture)
        self.set_texture(0)
        
        self.center_x = defines.window.WIDTH / 2
        self.center_y = 25
        self.dir = defines.directions.STOP
        self.speed = 5

    def update(self):
        self.center_x += self.dir*self.speed

        if self.left < 0:
            self.left = 0
        elif self.right > defines.window.WIDTH - 1:
            self.right = defines.window.WIDTH - 1

    def set_dir(self, direction):
        self.dir = direction
