.. _menu_scene:

Menu Scene
===========

The menu scene is how you get into the main game or look at the rules. Like all scenes previous, the first thing that needs to be done is to set the image bank, which in this case is the gamesprites image bank. You must then use a for loop to itterate through each tile and place a plain blank tile as the background.

.. code-block:: python
  :linenos:

    image_bank_4 = stage.Bank.from_bmp16("tree.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_4, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

You will also need to set up button detection for the start and select buttons, as they will be how you swap scenes later on.

.. code-block:: python
  :linenos:

    # Reupdating keys
    keys = 0

    # Buttons to keep state information on
    start_button = constants.button_state["button_up"]

There are also three instances of text: the title, and two instructional texts, one reading 'press start to begin' and the other saying 'press select for rules'. Like previous scenes, you must create a list to contain the text. Then create the text with the appropriate dimensions, palette (mt game studios palette), and coordinates. Append each text to the list.

.. code-block:: python
  :linenos:

    text = []

    text1 = stage.Text(width=50, height=30, font=None, palette=constants.CUSTOM_PALETTE, buffer=None)
    text1.move(23, 30)
    text1.text("SNAKOB'S FOREST")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.CUSTOM_PALETTE, buffer=None)
    text2.move(37, 55)
    text2.text("PRESS START")
    text.append(text2)

You will then need to make a larger model of the game scene spaceship show up on this scene. To do this, create a list to hold your sprites, then append the left and right sides of the spaceship to the list. Line up the coordinates so that the two sprites connect to create a larger scale spaceship.

.. code-block:: python
  :linenos:

  sprites = []

    background.tile(2, 2, 0)


    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    top_right_of_tree = stage.Sprite(image_bank_4, 13, 65, 116)
    sprites.append(top_right_of_tree)
    top_middle_of_tree = stage.Sprite(image_bank_4, 14, 81, 116)
    sprites.append(top_middle_of_tree)
    top_of_tree = stage.Sprite(image_bank_4, 9, 65, 100)
    sprites.append(top_of_tree)
    top_left_of_tree = stage.Sprite(image_bank_4, 10, 81, 100)
    sprites.append(top_left_of_tree)
    middle_right_of_tree = stage.Sprite(image_bank_4, 5, 65, 84)
    sprites.append(middle_right_of_tree)
    middle_of_tree = stage.Sprite(image_bank_4, 6, 81, 84)
    sprites.append(middle_of_tree)
    middle_left_of_tree = stage.Sprite(image_bank_4, 4, 49, 84)
    sprites.append(middle_left_of_tree)
    bottem_right_of_tree = stage.Sprite(image_bank_4, 7, 97, 84)
    sprites.append(bottem_right_of_tree)
    bottem_midle_of_tree = stage.Sprite(image_bank_4, 1, 65, 68)
    sprites.append(bottem_midle_of_tree)
    bottem_left_of_tree = stage.Sprite(image_bank_4, 3, 81, 68)
    sprites.append(bottem_left_of_tree)
    verybottem_right_of_tree = stage.Sprite(image_bank_4, 2, 97, 68)
    sprites.append(verybottem_right_of_tree)
    verybottem_middle_of_tree = stage.Sprite(image_bank_4, 11, 97, 100)
    sprites.append(verybottem_middle_of_tree)

    stars = []
    while True:
        time.sleep(1.0)
        stars = []
        for cloud_number in range(constants.STAR_NUMBER):
            star = stage.Sprite(image_bank_4, 15, random.randint(0, 160),random.randint(0, 128))
            stars.append(star)

As it is for every other scene, you must once again set your frame rate to 60, paint the sprite, text and background layers and render the initial scene screen.

.. code-block:: python
  :linenos:

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + sprites + stars + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

Next you must get the start and select buttons working. In your game loop, set keys to detect if either of the two buttons are pressed. Use an if statement to detect whether the start button is pressed or not. If the start button is pressed, swap to the game scene by calling the game scene function.

.. code-block:: python
  :linenos:

        # get user input
        keys = ugame.buttons.get_pressed()

        # update game logic
        if keys & ugame.K_START != 0:  # Start button
            keys = 0
            ugame.K_START = 0
            game_scene()
            break


Also insert a render into your game loop to ensure that the sprites on screen stay rendered.

.. code-block:: python
  :linenos:

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick()

You should now have a properly functioning menu scene.