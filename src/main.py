import arcade
import ship
import defines

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.all_sprites_list = None
        self.ship_sprite = None

    def setup(self):
        self.all_sprites_list = arcade.SpriteList()

        self.ship = ship.Ship()
        self.ship.center_x = defines.window.WIDTH / 2
        self.ship.center_y = 25
        self.all_sprites_list.append(self.ship)

    def on_draw(self):
        arcade.start_render()
        self.all_sprites_list.draw()

    def on_update(self, delta_time):
        self.all_sprites_list.update()

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
        elif key == arcade.key.ESCAPE:
            arcade.close_window()


def main():
    game = Game(defines.window.WIDTH, defines.window.HEIGHT, defines.TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
