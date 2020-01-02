import arcade
import ship
import directions as d

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SCREEN_TITLE = "Space Invaders"

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.ship = ship.Ship(SCREEN_WIDTH/2)

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()
        self.ship.show()

    def on_update(self, delta_time):
        self.ship.move()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.ship.set_dir(d.directions.LEFT)
        elif key == arcade.key.RIGHT:
            self.ship.set_dir(d.directions.RIGHT)

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT and self.ship.dir == d.directions.LEFT:
            self.ship.set_dir(d.directions.STOP)
        elif key == arcade.key.RIGHT and self.ship.dir == d.directions.RIGHT:
            self.ship.set_dir(d.directions.STOP)


def main():
    game = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
