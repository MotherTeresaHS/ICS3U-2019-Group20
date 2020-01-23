.. _asteroids:

Asteroids
==========

Once you have your spaceship working you can now add functionality for the asteroids. To have asteroids at each side of the screen, you will need four different lists (one for each side). Use a for loop to create asteroids up to the set amount from your constants file, and append the asteroids to their lists. This is to be done outside your gameloop. Be sure your asteroids have been painted and rendered on screen.

.. code-block:: python
  :linenos:

    def reset_left_snake():
        # Sets and resets the start coordinates of snakes starting on the left
        for left_snake_number in range(len(left_snakes)):
            if left_snakes[left_snake_number].x < 0:
                left_snakes[left_snake_number].move(random.randint
                                                        (-100, 0 -
                                                        constants.SPRITE_SIZE),
                                                        random.randint
                                                        (0, constants.SCREEN_Y))
                break

    def reset_top_snake():
        # Sets and resets the start coordinates of snakes starting on the top
        for top_snake_number in range(len(top_snakes)):
            if top_snakes[top_snake_number].y < 0:
                top_snakes[top_snake_number].move(random.randint
                                                        (0, constants.SCREEN_X),
                                                        random.randint
                                                        (-100, 0 -
                                                         constants.SPRITE_SIZE))
                break

    def reset_right_snake():
        # Sets and resets the start coordinates of snakes starting on the right
        for right_snake_number in range(len(right_snakes)):
            if right_snakes[right_snake_number].x < 0:
                right_snakes[right_snake_number].move(random.randint
                                                            (constants.SCREEN_X, 228),
                                                            random.randint
                                                            (0, constants.SCREEN_Y))
                break

    def reset_bottom_snake():
        # Sets and resets the start coordinates of snakes starting on the bottom
        for down_snake_number in range(len(bottom_snakes)):
            if bottom_snakes[down_snake_number].y < 0:
                bottom_snakes[down_snake_number].move(random.randint
                                                        (0, constants.SCREEN_X),
                                                        random.randint
                                                        (160 + constants.SPRITE_SIZE,
                                                         260))
                break

    # Gets the left snakes ready 
    left_snakes = []
    for left_snake_number in range(constants.SNAKE_CREATION_TOTAL):
        single_left_snake = stage.Sprite(image_bank_1, 4,
                                            constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
        left_snakes.append(single_left_snake)
    reset_left_snake()

    # Gets the top snakes ready
    top_snakes = []
    for top_snake_number in range(constants.SNAKE_CREATION_TOTAL):
        single_up_snake = stage.Sprite(image_bank_1, 6,
                                          constants.OFF_SCREEN_X,
                                          constants.OFF_SCREEN_Y)
        top_snakes.append(single_up_snake)
    reset_top_snake()

    # Gets the right snakes ready
    right_snakes = []
    for right_snake_number in range(constants.SNAKE_CREATION_TOTAL):
        single_right_snake = stage.Sprite(image_bank_1, 7,
                                             constants.OFF_SCREEN_X,
                                             constants.OFF_SCREEN_Y)
        right_snakes.append(single_right_snake)
    reset_right_snake()

    # Gets the bottem snakes ready
    bottom_snakes = []
    for down_snake_number in range(constants.SNAKE_CREATION_TOTAL):
        single_down_snake = stage.Sprite(image_bank_1, 5,
                                            constants.OFF_SCREEN_X,
                                            constants.OFF_SCREEN_Y)
        bottom_snakes.append(single_down_snake)
    reset_bottom_snake()

    start_time = time.time()

When you have your asteroids ready, you will need to be able to have them move across the screen. Once again, each side of their screen will need a way to scroll asteroids. For this, create a for loop in your game loop that itterates through all the asteroids in a list. An if statement within will deterimine if the asteroid isn't in purgatory off screen, and will scroll across the screen in the desired direction. Within said if statement should be another if statement determining if the asteroid has reached the other side of the screen. If the asteroid has, it will be moved back into purgatory off screen and wait to be sent out again.

.. code-block:: python
  :linenos:

        # Scroll snakes from left of screen
        for left_snake_number in range(len(left_snakes)):
            if left_snakes[left_snake_number].x < constants.OFF_RIGHT_SCREEN:
                left_snakes[left_snake_number].move(
                left_snakes[left_snake_number].x + constants.SNAKE_SPEED,
                left_snakes[left_snake_number].y)
                if left_snakes[left_snake_number].x > constants.SCREEN_X:
                    left_snakes[left_snake_number].move(constants.OFF_SCREEN_X,
                                                              constants.OFF_SCREEN_Y)
                    reset_left_snake()

        # Scroll snakes from top of screen
        for top_snake_number in range(len(top_snakes)):
            if top_snakes[top_snake_number].y < constants.OFF_BOTTOM_SCREEN:
                top_snakes[top_snake_number].move(
                top_snakes[top_snake_number].x,
                top_snakes[top_snake_number].y + constants.SNAKE_SPEED)
                if top_snakes[top_snake_number].y > constants.SCREEN_Y:
                    top_snakes[top_snake_number].move(constants.OFF_SCREEN_X,
                                                            constants.OFF_SCREEN_Y)
                    reset_top_snake()

        # Scroll snakes from right of screen left
        for right_snake_number in range(len(right_snakes)):
            if right_snakes[right_snake_number].x > constants.OFF_LEFT_SCREEN:
                right_snakes[right_snake_number].move(
                right_snakes[right_snake_number].x - constants.SNAKE_SPEED,
                right_snakes[right_snake_number].y)
                if right_snakes[right_snake_number].x < 0 - constants.SPRITE_SIZE:
                    right_snakes[right_snake_number].move(constants.OFF_SCREEN_X,
                                                                constants.OFF_SCREEN_Y)
                    reset_right_snake()

        # Scroll snakes from bottom of screen
        for down_snake_number in range(len(bottom_snakes)):
            if bottom_snakes[down_snake_number].y > constants.OFF_TOP_SCREEN:
                bottom_snakes[down_snake_number].move(
                bottom_snakes[down_snake_number].x,
                bottom_snakes[down_snake_number].y - constants.SNAKE_SPEED)
                if bottom_snakes[down_snake_number].y < 0 - constants.SPRITE_SIZE:
                    bottom_snakes[down_snake_number].move(constants.OFF_SCREEN_X,
                                                                constants.OFF_SCREEN_Y)
                    reset_bottom_snake()

You should now have asteroids that scroll across the screen from all four directions and are able to reset themselves.