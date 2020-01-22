.. _apples:

Apples
==========

First, you must make a list in which you can store the apples. To make the program run a lot more smooth, and less glitchy, make the list contain only one apple. When that apple has been consumed by the sprite, or it hasnt been touched for its timeframe, change its location.

.. code-block:: python
  :linenos:
  
    apples = []
    apple_bank = stage.Sprite(image_bank_1, 12, int(constants.OFF_SCREEN_X), (constants.OFF_SCREEN_X - constants.SPRITE_SIZE))
    apples.append(apple_bank)
    timer = 0

Your character starts with two health points, if you lose a health point, and wish to regain said health point, or wish to gain an extra health point to get to a maximum of three, you must collide with an apple. The apples spawn at random times in random locations on the screen. You must make sure that they don't spawn right away, and that they spawn in random locations.

.. code-block:: python
  :linenos:

    # makes the apples randomly apear on screen
        apple_bank.move(random.randint(0 + constants.SPRITE_SIZE,
                                        constants.SCREEN_X -
                                        constants.SPRITE_SIZE),
                                        random.randint(0 + constants.SPRITE_SIZE,
                                        constants.SCREEN_Y -
                                        constants.SPRITE_SIZE))

The last thing you will need is something to detect if the Snakob has collided with (picked up) the apple. To do this you will need a for loop watching if a series of coordinates (hitbox) on each have intersected. If this happens, the apple is removed from the screen, and placed in another random location in a couple seconds. At this point, your characters health should have increased by one, unless it is already at 3 health.

.. code-block:: python
  :linenos:
  
    for ammo_number in range(len(apples)):
            if apples[ammo_number].x > 0:
                if snakob_bank.x > 0:
                    if stage.collide(apples[ammo_number].x + 6,
                                     apples[ammo_number].y + 3,
                                     apples[ammo_number].x + 10,
                                     apples[ammo_number].y + 13,
                                     snakob_bank.x + 1,
                                     snakob_bank.y + 1,
                                     snakob_bank.x + 14,
                                     snakob_bank.y + 14):
                        apples[ammo_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                        health_hearts = health_hearts + 1
                        sound.stop()
                        sound.play(health_sound)
                        if health_hearts == 4:
                            health_hearts = 3
                        health_text.clear()
                        health_text.cursor(0, 2)
                        health_text.move(1, 2)
                        health_text.text("Health: {0}".format(health_hearts))

The apples should now be fully functional.