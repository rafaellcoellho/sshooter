import arcade
from defines import window,directions,angles, TITLE
from ship import Ship
from bullet import Bullet
from alien import Alien
from random import randrange

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)

        self.ship = None
        self.bullets = arcade.SpriteList()
        self.aliens = arcade.SpriteList()

    def setup(self):
        self.ship = Ship()
        for i in range(6):
            self.aliens.append(
                Alien(i * 80 + 80, window.HEIGHT-60)
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

        in_edge = False
        for alien in self.aliens:
            if randrange(200) == 0:
                self.bullets.append(
                    Bullet(
                        alien.center_x,
                        angles.FACE_DOWN,
                        top=alien.bottom
                    )
                )
            if alien.right > window.WIDTH or alien.left < 0:
                in_edge = True
                break
        if in_edge:
            for alien in self.aliens:
                alien.shift_down()

        for bullet in self.bullets:
            aliens_hit = arcade.check_for_collision_with_list(bullet, self.aliens)
            if aliens_hit != []:
                aliens_hit[0].remove_from_sprite_lists()
                bullet.remove_from_sprite_lists()
            
            player_hit = arcade.check_for_collision(bullet, self.ship)
            if player_hit:
                print('Game Over')
                arcade.close_window()


        for bullet in self.bullets:
            if bullet.top > window.HEIGHT or bullet.top < 0:
                bullet.remove_from_sprite_lists()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.LEFT:
            self.ship.set_dir(directions.LEFT)
        elif key == arcade.key.RIGHT:
            self.ship.set_dir(directions.RIGHT)

    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.LEFT and self.ship.dir == directions.LEFT:
            self.ship.set_dir(directions.STOP)
        elif key == arcade.key.RIGHT and self.ship.dir == directions.RIGHT:
            self.ship.set_dir(directions.STOP)
        elif key == arcade.key.SPACE:
            self.bullets.append(
                Bullet(
                    self.ship.center_x,
                    angles.FACE_UP,
                    bottom=self.ship.top
                )
            )
        elif key == arcade.key.ESCAPE:
            arcade.close_window()


def main():
    game = Game(window.WIDTH, window.HEIGHT, TITLE)
    game.setup()
    arcade.run()

if __name__ == "__main__":
    main()
