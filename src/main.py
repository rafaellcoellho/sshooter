import arcade
import defines
import ship
import bullet
import alien

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.ship = None
        self.bullets = arcade.SpriteList()
        self.aliens = arcade.SpriteList()

    def setup(self):
        self.ship = ship.Ship()
        for i in range(6):
            self.aliens.append(
                alien.Alien(i * 80 + 80, defines.window.HEIGHT-60)
            )

    def on_draw(self):
        arcade.start_render()
        self.ship.draw()
        self.bullets.draw()
        self.aliens.draw()

    def on_update(self, delta_time):
        self.ship.update()
        self.bullets.update()
        self.aliens.update()

        edge = False

        for alien in self.aliens:
            if alien.right > defines.window.WIDTH or alien.left < 0:
                edge = True
        
        if edge == True:
            for alien in self.aliens:
                alien.shift_down()

        for bullet in self.bullets:
            if bullet.top > defines.window.HEIGHT or bullet.top < 0:
                bullet.remove_from_sprite_lists()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.ship.set_dir(defines.directions.LEFT)
        elif key == arcade.key.RIGHT:
            self.ship.set_dir(defines.directions.RIGHT)

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT and self.ship.dir == defines.directions.LEFT:
            self.ship.set_dir(defines.directions.STOP)
        elif key == arcade.key.RIGHT and self.ship.dir == defines.directions.RIGHT:
            self.ship.set_dir(defines.directions.STOP)
        elif key == arcade.key.SPACE:
            self.bullets.append(
                bullet.Bullet(
                    self.ship.center_x,
                    defines.angles.FACE_UP,
                    bottom=self.ship.top
                )
            )
        elif key == arcade.key.ESCAPE:
            arcade.close_window()


def main():
    game = Game(defines.window.WIDTH, defines.window.HEIGHT, defines.TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
