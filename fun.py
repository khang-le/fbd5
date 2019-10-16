#!/usr/bin/env python3
# Created by: Khang Le
# Created on: October 2019

# Creates a sprite on pybadge

import ugame
import stage
import constants


def game_scence():

    # this function is a scence
    image_bank_1 = stage.Bank.from_bmp16("space_aliens.bmp")
    background = stage.Grid(image_bank_1, constants.SCREEN_X,
                            constants.SCREEN_Y)
    sprites = []
    ship = stage.Sprite(image_bank_1, 5,
                        int(constants.SCREEN_X/2 - constants.SPRITE_SIZE/2),
                        int(constants.SCREEN_Y - constants.SPRITE_SIZE +
                            constants.SPRITE_SIZE / 2))
    sprites.append(ship)
    game = stage.Stage(ugame.display, constants.FPS)
    game.layers = sprites + [background]
    game.render_block()

    while True:
        keys = ugame.buttons.get_pressed()
        if keys & ugame.K_RIGHT != 0:
            if ship.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                ship.move(constants.SCREEN_X - constants.SPRITE_SIZE, ship.y)
            else:
                ship.move(ship.x + 1, ship.y)
        if keys & ugame.K_LEFT != 0:
            if ship.x < 0:
                ship.move(0, ship.y)
            else:
                ship.move(ship.x - 1, ship.y)

        game.render_sprites(sprites)
        game.tick()


if __name__ == "__main__":
    game_scence()
