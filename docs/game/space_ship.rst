.. _space_ship:

Space Ship
==========

The next step is to get your spaceship working. You have to start by creating a list that will hold your primary sprites (namely your spaceship). You will then need to create your spaceship sprite and append it to the list in the 0th position. Remember, this is done outside your game loop.

.. code-block:: python
  :linenos:

    image_bank_1 = stage.Bank.from_bmp16("SPRITES.bmp")
    snakob = []
    snakob_bank = stage.Sprite(image_bank_1, 13, int(constants.SCREEN_X / 2), constants.SCREEN_Y - constants.SPRITE_SIZE)
    snakob.append(snakob_bank) #

You will need to paint your sprite onto the screen. You can do this by adding your sprite list in front of your background. 

.. code-block:: python
  :linenos:

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = snakob + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

The next thing you will need to do to ensure it continues to show up is to have it rendered on screen. You do this at the bottom of the inside of your game loop.

.. code-block:: python
  :linenos:

    game.render_sprites(snakob)
    game.tick()

You will need to paint and render any new sprite list you add using the same methods. Finally, you will want to make sure your spaceship will be able to move, and keep it from moving off screen. This is all done in the game loop. The first thing you have to do is to set your keys to be watching if a button is being pressed. Next, since your user will be using the D-Pad to move around, you will want to add an if statement to detect if a specific button on the D-Pad. Depending on which button is pressed, your spaceship will move in a different direction. You will also want to make sure your spaceship can't move off screen. You can do this by putting an if statement inside your previous if statement. If the ship's X or Y coordinates goes off the screen limits indicated in your constants file, it will move the ship back on screen. There is also a variable that is changed each time a button on the D-Pad is pressed. This variable will be used later to determine the directions the lasers fire.

.. code-block:: python
  :linenos:

        if keys & ugame.K_RIGHT != 0 or keys & ugame.K_LEFT != 0 or keys & ugame.K_DOWN != 0 or keys & ugame.K_UP != 0:
            a_single_cloud.move((snakob_bank.x - 3) + constants.SNAKOB_SPEED, (snakob_bank.y + 2))

        # takes off cloud particles if none of the d pad is being pressed 
        if keys & ugame.K_RIGHT == 0 and keys & ugame.K_LEFT == 0 and keys & ugame.K_DOWN == 0 and keys & ugame.K_UP == 0:
            a_single_cloud.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # if right D-Pad is pressed
        if keys & ugame.K_RIGHT != 0:
            # if snakob moves off right screen, move it back
            if snakob_bank.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                snakob_bank.x = constants.SCREEN_X - constants.SPRITE_SIZE
            if swords_bank.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                swords_bank.x = constants.SCREEN_X - constants.SPRITE_SIZE
            # else move snakob right and sword
            else:
                snakob_bank.move(snakob_bank.x + constants.SNAKOB_SPEED, snakob_bank.y)
                swords_bank.move((snakob_bank.x + 14)+ constants.SNAKOB_SPEED, (snakob_bank.y) - 4)
                swords1_bank.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                snakob_direction = "right"


        # if left D-Pad is pressed
        if keys & ugame.K_LEFT != 0:
            # if snakob moves off left screen, move it back
            if snakob_bank.x < 0:
                snakob_bank.x = 0
            if swords_bank.x < 16:
                swords_bank.x = 16
            # else move snakob left and the sword
            else:
                snakob_bank.move(snakob_bank.x - constants.SNAKOB_SPEED, snakob_bank.y)
                swords1_bank.move((snakob_bank.x - 14) - constants.SNAKOB_SPEED, (snakob_bank.y - 4))
                swords_bank.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                snakob_direction = "left"

        # if left up-Pad is pressed
        if keys & ugame.K_UP != 0:
            # if snakob moves off up screen, move it back
            if snakob_bank.y < 0:
                snakob_bank.y = 0
            else:
                snakob_bank.move(snakob_bank.x, snakob_bank.y - constants.SNAKOB_SPEED)
                swords_bank.move((snakob_bank.x + 14), snakob_bank.y - 4)
                swords1_bank.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                snakob_direction = "up"


        # if left D-Pad is pressed
        if keys & ugame.K_DOWN != 0:
            # if snakob moves off down screen, move it back
            if snakob_bank.y > 116:
                snakob_bank.y = 116
            # else move snakob down and sword
            else:
                snakob_bank.move(snakob_bank.x, snakob_bank.y + constants.SNAKOB_SPEED)
                swords_bank.move((snakob_bank.x + 14), snakob_bank.y - 4)
                swords1_bank.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                snakob_direction = "down"