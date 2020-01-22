.. _asteroid_collisions:

Asteroid Collisions
===================

Now that the most important elements of the game are working, we now need to program how the game will end. The game is supposed to end when an asteroid hit box collides with the spaceship hit box. There are however two things we need to worry about first. There are two main objectives to the game: to destroy as many lasers as you can, and to survive for as long as you can. In the lasers section, I showed you how to keep track of the number of asteroids destroyed. To calculate how long the player survived, all we need is the start time. Initialize a variable outside the game loop for the start time. Have this variable use the time.time(*number of seconds to sleep*) function from the time module. This variable will then equal the exact epoch time the player entered the game scene at. In case you do not understand what epoch time is, I explained it on the game over page of the menus section.

.. code-block:: python
  :linenos:

    # This variable records the time the game scene launched
    start_time = time.time()

Now we can begin working on how the game ends. The game ends when an asteroid touches the player's spaceship, so we will need more collision detection just like I have done for the ammo packs and lasers. Create four for loops (one for each asteroid list respectively) in the game loop, and have them itterate through their respective asteroid list to see if the asteroid hit box has overlapped with the spaceship hit box. If an asteroid hits the spaceship, play the crash sound. You must then use the time.sleep() function to freeze the game in place for four seconds. This will aid in a seemless transition from your game scene to your game over scene. After the pause, be sure to put a sound.stop() to stop any sounds still playing before transitioning to the game over scene. Lastly, call the game over scene, and pass it your asteroids destroyed variable and your start time variable.

.. code-block:: python
  :linenos:

        # detects collision in snakes and snakob
        for left_snake_number in range(len(left_snakes)):
            if left_snakes[left_snake_number].x > 0:
                if stage.collide(left_snakes[left_snake_number].x + 1,
                                 left_snakes[left_snake_number].y + 1,
                                 left_snakes[left_snake_number].x + 15,
                                 left_snakes[left_snake_number].y + 15,
                                 snakob_bank.x + 3, snakob_bank.y + 3, snakob_bank.x + 12, snakob_bank.y + 12):
                    left_snakes[left_snake_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    sound.stop()
                    sound.play(crash_sound)
                    health_hearts = health_hearts - 1
                    health_text.clear()
                    health_text.cursor(0, 2)
                    health_text.move(1, 2)
                    health_text.text("Health: {0}".format(health_hearts))
                    
        # detects collision in snakes and snakob
        for bottom_snake_number in range(len(bottom_snakes)):
            if bottom_snakes[bottom_snake_number].x > 0:
                if stage.collide(bottom_snakes[bottom_snake_number].x + 1,
                                 bottom_snakes[bottom_snake_number].y + 1,
                                 bottom_snakes[bottom_snake_number].x + 15,
                                 bottom_snakes[bottom_snake_number].y + 15,
                                 snakob_bank.x + 3, snakob_bank.y + 3, snakob_bank.x + 12, snakob_bank.y + 12):
                    bottom_snakes[bottom_snake_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    sound.stop()
                    sound.play(crash_sound)
                    health_hearts = health_hearts - 1
                    health_text.clear()
                    health_text.cursor(0, 2)
                    health_text.move(1, 2)
                    health_text.text("Health: {0}".format(health_hearts))


        # This detects a collision between snakob and snakes going right
        for right_snake_number in range(len(right_snakes)):
            if right_snakes[right_snake_number].x > 0:
                if stage.collide(right_snakes[right_snake_number].x + 1,
                                 right_snakes[right_snake_number].y + 1,
                                 right_snakes[right_snake_number].x + 15,
                                 right_snakes[right_snake_number].y + 15,
                                 snakob_bank.x + 3, snakob_bank.y + 3, snakob_bank.x + 12, snakob_bank.y + 12):
                    right_snakes[right_snake_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    sound.stop()
                    sound.play(crash_sound)
                    health_hearts = health_hearts - 1
                    health_text.clear()
                    health_text.cursor(0, 2)
                    health_text.move(1, 2)
                    health_text.text("Health: {0}".format(health_hearts))

    # This detects a collision between snakob and snakes going up
        for top_snake_number in range(len(top_snakes)):
            if top_snakes[top_snake_number].x > 0:
                if stage.collide(top_snakes[top_snake_number].x + 1,
                                 top_snakes[top_snake_number].y + 1,
                                 top_snakes[top_snake_number].x + 15,
                                 top_snakes[top_snake_number].y + 15,
                                 snakob_bank.x + 3, snakob_bank.y + 3, snakob_bank.x + 12, snakob_bank.y + 12):
                    top_snakes[top_snake_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    sound.stop()
                    sound.play(crash_sound)
                    health_hearts = health_hearts - 1
                    health_text.clear()
                    health_text.cursor(0, 2)
                    health_text.move(1, 2)
                    health_text.text("Health: {0}".format(health_hearts))

Assuming you have followed all the steps correctly, you should now have a fully functional game scene.