import arcade
import ship
import defines

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.ship = ship.Ship(defines.window.WIDTH/2)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        self.ship.show()

    def on_update(self, delta_time):
        self.ship.move()

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


def main():
    game = Game(defines.window.WIDTH, defines.window.HEIGHT, defines.TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
