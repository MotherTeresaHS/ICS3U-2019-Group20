.. _lasers:

Lasers
==========

The next thing to get working is actually firing the lasers themselves. Like all the other sprites, they must first be created and added to a list. Make sure the list is both painted and rendered on screen. Similar to the asteroids, the lasers will be created and appended to a list with a for loop and will appear in purgatory off screen. 

.. code-block:: python
  :linenos:

   rocks = []
    rock_direction = []
    for rock_number in range(constants.TOTAL_NUMBER_OF_ROCKS):
        a_single_rock = stage.Sprite(image_bank_1, 15, constants.OFF_SCREEN_X, constants.OFF_SCREEN_X)
        rocks.append(a_single_rock)
        rock_direction.append("None")

The first think we will want to do before we program the lasers is to have a way to count the asteroids that have been hit by the lasers. To do this, initialize a variable equal to 0 to keep score outside your game loop. Every time an asteroid is hit with a laser, the score will increase by one.

.. code-block:: python
  :linenos:

    # Score counter for the asteroids
    rock_counter = 0

Lasers are fundamentaly the hardest and most tedious part of this program. Before we start working on the lasers, we need a method of firing them. The player must use the A button to fire their lasers after they pick up an ammo pack. We first need to set up a way of detecting the state of the A button as we want the lasers to fire when the button has just been pressed. This should be in the game loop.

.. code-block:: python
  :linenos:

        # A button to fire
        if keys & ugame.K_X != 0:
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

Now we need a way to move the lasers across the screen in the desired direction. To do this we will have a for loop in the game loop that continuosly itterate through all eight lasers.

.. code-block:: python
  :linenos:

        # Firing lasers
        for laser_number in range(len(rocks)):

There are three large chunks inside this for loop. The first is the singular projectile shot. If the laser isn't off screen in purgatory (because the player has pressed the A button), the laser will scroll in a specific direction according to the last button pressed on the D-Pad. Once the laser reaches off screen, it is moved back to purgatory to await its next use. The type of ammo and firing direction is then reupdated to zero as to not cause problems with future ammo packs collected and lasers fired.

.. code-block:: python
  :linenos:

            if rocks[rock_number].x > 0 :
                laser_direction = None
                if rock_direction[rock_number] == "down":
                    rocks[rock_number].move(rocks[rock_number].x, rocks[rock_number].y + constants.ROCK_SPEED)
                elif rock_direction[rock_number] == "up":
                    rocks[rock_number].move(rocks[rock_number].x, rocks[rock_number].y - constants.ROCK_SPEED)
                elif rock_direction[rock_number] == "left":
                    rocks[rock_number].move(rocks[rock_number].x - constants.ROCK_SPEED, rocks[rock_number].y)
                elif rock_direction[rock_number] == "right":
                    rocks[rock_number].move(rocks[rock_number].x + constants.ROCK_SPEED, rocks[rock_number].y)

                if rocks[rock_number].y < constants.OFF_TOP_SCREEN:
                    rocks[rock_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                if rocks[rock_number].y > 128:
                    rocks[rock_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                if rocks[rock_number].x > 160:
                    rocks[rock_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                if rocks[rock_number].x < 1:
                    rocks[rock_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    
The final thing you will need is a way to detect if there has been a collision between the lasers and asteroids. This will be done in a way similar to how a player picks up ammo packs. A for loop will itterate through both the asteroids and the lasers to determine if either of their hit boxes ever overlap. Like the ammo-spaceship collision detect, this is to be done in the game loop. If there is an overlap, the hit asteroid will be taken off screen and the proper reset asteroid function will be called. The laser that hit the asteroid will be moved back to purgatory. When any asteroid is hit, the impact sound plays to indicate an asteroid has been destroyed. The score variable also increases by one every time an asteroid is hit with a laser. As there are four different asteroid lists, there has to be four different for loops, one that detects collisions between a laser and an asteroid of its respective list.

.. code-block:: python
  :linenos:

        for rock_number in range(len(rocks)):
            if rocks[rock_number].x > 0:
                for left_snake_number in range(len(left_snakes)):
                    if left_snakes[left_snake_number].x > 0:
                        if stage.collide(left_snakes[left_snake_number].x + 1,
                                         left_snakes[left_snake_number].y + 1,
                                         left_snakes[left_snake_number].x + 15,
                                         left_snakes[left_snake_number].y + 15,
                                         rocks[rock_number].x + 3,
                                         rocks[rock_number].y + 3,
                                         rocks[rock_number].x + 13,
                                         rocks[rock_number].y + 13):
                            left_snakes[left_snake_number].move(constants.OFF_SCREEN_X,
                                                                 constants.OFF_SCREEN_Y)
                            rocks[rock_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            score += 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))
                            # this will freeze the screen for a split second, but we have no option
                            game.render_block()
                            left_snake_number = left_snake_number + 1

        # This detects if any rocks hit snakes heading down
        for rock_number in range(len(rocks)):
            if rocks[rock_number].x > 0:
                for top_snake_number in range(len(top_snakes)):
                    if top_snakes[top_snake_number].x > 0:
                        if stage.collide(top_snakes[top_snake_number].x + 1,
                                         top_snakes[top_snake_number].y + 1,
                                         top_snakes[top_snake_number].x + 15,
                                         top_snakes[top_snake_number].y + 15,
                                         rocks[rock_number].x + 3,
                                         rocks[rock_number].y + 3,
                                         rocks[rock_number].x + 13,
                                         rocks[rock_number].y + 13):
                            top_snakes[top_snake_number].move(constants.OFF_SCREEN_X,
                                                                constants.OFF_SCREEN_Y)
                            rocks[rock_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            score += 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))
                            # this will freeze the screen for a split second, but we have no option
                            game.render_block()
                            top_snake_number = top_snake_number + 1

        # This detects if any rocks hit snakes heading left
        for rock_number in range(len(rocks)):
            if rocks[rock_number].x > 0:
                for right_snake_number in range(len(right_snakes)):
                    if right_snakes[right_snake_number].x > 0:
                        if stage.collide(right_snakes[right_snake_number].x + 1,
                                         right_snakes[right_snake_number].y + 1,
                                         right_snakes[right_snake_number].x + 15,
                                         right_snakes[right_snake_number].y + 15,
                                         rocks[rock_number].x + 3,
                                         rocks[rock_number].y + 3,
                                         rocks[rock_number].x + 13,
                                         rocks[rock_number].y + 13):
                            right_snakes[right_snake_number].move(constants.OFF_SCREEN_X,
                                                                  constants.OFF_SCREEN_Y)
                            rocks[rock_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            score += 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))
                            # this will freeze the screen for a split second, but we have no option
                            game.render_block()
                            right_snake_number = right_snake_number + 1

        # This detects if any rocks hit snakes heading up
        for rock_number in range(len(rocks)):
            if rocks[rock_number].x > 0:
                for bottom_snake_number in range(len(bottom_snakes)):
                    if bottom_snakes[bottom_snake_number].x > 0:
                        if stage.collide(bottom_snakes[bottom_snake_number].x + 1,
                                         bottom_snakes[bottom_snake_number].y + 1,
                                         bottom_snakes[bottom_snake_number].x + 15,
                                         bottom_snakes[bottom_snake_number].y + 15,
                                         rocks[rock_number].x + 3,
                                         rocks[rock_number].y + 3,
                                         rocks[rock_number].x + 13,
                                         rocks[rock_number].y + 13):
                            bottom_snakes[bottom_snake_number].move(constants.OFF_SCREEN_X,
                                                                   constants.OFF_SCREEN_Y)
                            rocks[rock_number].move(constants.OFF_SCREEN_X,
                                                      constants.OFF_SCREEN_Y)
                            sound.stop()
                            sound.play(boom_sound)
                            score += 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))
                            # this will freeze the screen for a split second, but we have no option
                            game.render_block()
                            bottom_snake_number = bottom_snake_number + 1
                            
If you did everything correct you should now be able to fire three different types of lasers and have them destroy asteroids.