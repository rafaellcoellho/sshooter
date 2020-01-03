import arcade
import defines

class Bullet(arcade.Sprite):
    def __init__(self, initial_x, angle, top=None, bottom=None):
        super().__init__()

        texture = arcade.load_texture(':resources:images/space_shooter/laserBlue01.png', scale=0.5)
        self.textures.append(texture)
        self.set_texture(0)

        self.speed = 5
        self.center_x = initial_x
        self.angle = angle
        if top != None:
            self.top = top
        elif bottom != None:
            self.bottom = bottom
    
    def update(self):
        if self.angle == defines.angles.FACE_UP:
            self.center_y += defines.directions.UP*self.speed
        else:
            self.center_y += defines.directions.DOWN*self.speed
