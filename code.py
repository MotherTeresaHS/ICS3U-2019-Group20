##!/usr/bin/env python3

# Created by: Cameron and RJ
# Created on: Dec 2019
# This is the main file for Snakob's forest for CircuitPython

import ugame
import stage
import board
import time
import random
import constants


def blank_white_reset_scene():
    # this function is the splash scene game loop

    # do house keeping to ensure everythng is setup

    # set up the NeoPixels

    # reset sound to be off
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1/2 seconds
        time.sleep(0.5)
        mt_splash_scene()
        # redraw sprite list

def mt_splash_scene():
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)



    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic
        # Wait for 1 seconds
        time.sleep(3.0)
        game_splash_scene()
        # Wait for 1 second


        # redraw sprite list

def game_splash_scene():
    # this function is the Game splash scene

    # Gets an image bank for CircuitPython
    image_bank_3 = stage.Bank.from_bmp16("game_splash_scene.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # set up the sprite list
    sprites = []

    # sets up the list for the giant sprite
    snakob = []

    # appends the snake into one big sprite
    background.tile(0, 2, 0)

    bottom_left = stage.Sprite(image_bank_3, 13, 65, 100)
    snakob.append(bottom_left)

    mid_tail = stage.Sprite(image_bank_3, 14, 81, 100)
    snakob.append(mid_tail)

    mid_left_neck = stage.Sprite(image_bank_3, 9, 65, 84)
    snakob.append(mid_left_neck)

    mid_right_neck = stage.Sprite(image_bank_3, 10, 81, 84)
    snakob.append(mid_right_neck)

    mid_left_side_face = stage.Sprite(image_bank_3, 5, 65, 68)
    snakob.append(mid_left_side_face)

    right_eye = stage.Sprite(image_bank_3, 6, 81, 68)
    snakob.append(right_eye)

    left_side_face = stage.Sprite(image_bank_3, 4, 49, 68)
    snakob.append(left_side_face)

    end_of_tongue = stage.Sprite(image_bank_3, 7, 97, 68)
    snakob.append(end_of_tongue)

    top_of_left_eye = stage.Sprite(image_bank_3, 1, 65, 52)
    snakob.append(top_of_left_eye)

    end_of_tail = stage.Sprite(image_bank_3, 3, 97, 52)
    snakob.append(end_of_tail)

    left_eyebrow = stage.Sprite(image_bank_3, 2, 81, 52)
    snakob.append(left_eyebrow)

    bulky_part_tail = stage.Sprite(image_bank_3, 8, 49, 84)
    snakob.append(bulky_part_tail)

    lower_tail = stage.Sprite(image_bank_3, 12, 49, 100)
    snakob.append(lower_tail)

    snake15 = stage.Sprite(image_bank_3, 15, 96, 100)
    snakob.append(snake15)

    # text for the splash screen
    text = []

    text1 = stage.Text(width=200, height=200, font=None, palette=constants.CUSTOM_PALETTE, buffer=None)
    text1.move(30, 40)
    text1.text("SNAKOB STUDIOS")
    text.append(text1)

    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    snake_sound = open("1234.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(snake_sound)

    game = stage.Stage(ugame.display, 60)

    game.layers = text + snakob + [background]

    game.render_block()
    while True:
        # get user input
        # update game logic
        time.sleep(3.0)
        # redraw sprite list
        main_menu_scene()

def main_menu_scene():
    # This is the main menu scene


    # gets image bank ready
    image_bank_4 = stage.Bank.from_bmp16("tree.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_4, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # gets the sprite list ready
    sprites = []

    background.tile(2, 2, 0)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    # This part puts the tree on the screen
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

    # gets the text ready
    text = []

    text1 = stage.Text(width=50, height=30, font=None, palette=constants.CUSTOM_PALETTE, buffer=None)
    text1.move(23, 30)
    text1.text("SNAKOB'S FOREST")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.CUSTOM_PALETTE, buffer=None)
    text2.move(37, 55)
    text2.text("PRESS START")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)

    # creates random stars to appear
    stars = []
    while True:
        time.sleep(1.0)
        stars = []
        for cloud_number in range(constants.STAR_NUMBER):
            star = stage.Sprite(image_bank_4, 15, random.randint(0, 160),random.randint(0, 128))
            stars.append(star)

        game.layers = text + sprites + stars + [background]
        game.render_block()

    # update game logic
        keys = ugame.buttons.get_pressed()
        #print(keys)
        if keys & ugame.K_START != 0:  # Start button
            game_scene()
            #break

def game_scene():
    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready
    pew_sound = open("blip.wav", 'rb')  # to change the wav volume: https://audioalter.com/volume/
    boom_sound = open("squish.wav", 'rb')
    crash_sound = open('boing3.wav', 'rb')
    health_sound = open('bloop_x.wav', 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # get image bank ready
    image_bank_1 = stage.Bank.from_bmp16("SPRITES.bmp")
    sprites = []

    # create rocks for when we shoot
    rocks = []
    rock_direction = []
    for rock_number in range(constants.TOTAL_NUMBER_OF_ROCKS):
        a_single_rock = stage.Sprite(image_bank_1, 15, constants.OFF_SCREEN_X, constants.OFF_SCREEN_X)
        rocks.append(a_single_rock)
        rock_direction.append("None")

    # create the particle cloud for when snakob moves
    cloud = []
    a_single_cloud = stage.Sprite(image_bank_1, 11, constants.OFF_SCREEN_X, constants.OFF_SCREEN_X)
    cloud.append(a_single_cloud)


    def show_clouds():
        # create the particle cloud for when snakob moves
        a_single_cloud.move(snakob_bank.x + constants.SNAKOB_SPEED, snakob_bank.y)
        a_single_cloud.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

    # This creates snakob
    snakob = []
    snakob_bank = stage.Sprite(image_bank_1, 13, int(constants.SCREEN_X / 2), constants.SCREEN_Y - constants.SPRITE_SIZE)
    snakob.append(snakob_bank) #

    # This creates the swords for snakobs left and right
    swords = []
    swords_bank = stage.Sprite(image_bank_1, 8, int((constants.SCREEN_X / 2) + 14), ((constants.SCREEN_Y - 4) - constants.SPRITE_SIZE))
    swords.append(swords_bank)
    swords1_bank = stage.Sprite(image_bank_1, 9, int(constants.OFF_SCREEN_X), (constants.OFF_SCREEN_X - constants.SPRITE_SIZE))
    swords.append(swords1_bank)

    # This creates the sparks for snakobs sword
    sparks = []
    spark_bank = stage.Sprite(image_bank_1, 10, int(constants.OFF_SCREEN_X), (constants.OFF_SCREEN_X - constants.SPRITE_SIZE))
    sparks.append(spark_bank)

    # Gets the score ready
    score = 0
    score_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    score_text.clear()
    score_text.cursor(0, 0)
    score_text.move(1, 1)
    score_text.text("Score: {0}".format(score))

    # get the health bar ready
    health_hearts = 2
    health_text = stage.Text(width=29, height=14, font=None, palette=constants.SCORE_PALETTE, buffer=None)
    health_text.clear()
    health_text.cursor(0, 2)
    health_text.move(1, 2)
    health_text.text("Health: {0}".format(health_hearts))

    # create the apple sprite
    apples = []
    apple_bank = stage.Sprite(image_bank_1, 12, int(constants.OFF_SCREEN_X), (constants.OFF_SCREEN_X - constants.SPRITE_SIZE))
    apples.append(apple_bank)
    timer = 0

    def health():
        # makes the apples apear on screen
        apple_bank.move(random.randint(0 + constants.SPRITE_SIZE,
                                        constants.SCREEN_X -
                                        constants.SPRITE_SIZE),
                                        random.randint(0 + constants.SPRITE_SIZE,
                                        constants.SCREEN_Y -
                                        constants.SPRITE_SIZE))

    # sets the background to image 0 in the bank and randomly generates the backround
    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            boolean = random.randint(0 ,1)
            if boolean == 0:
                tile_picked = 0
            if boolean == 1:
                tile_picked = 14
            background.tile(x_location, y_location, tile_picked)

    # sets the snake counts to these
    snake_count = 1
    snake_counter = 1

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


    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = apples + cloud + snakob + top_snakes + bottom_snakes + left_snakes + right_snakes + swords + sprites + rocks + [health_text] + [score_text] + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        #print(keys

        # sets rock number to zero
        rock_number = 0

        # chcecks if keys & ugame.K_X != 0: A button
        if keys & ugame.K_X != 0:  # A button
            if a_button == constants.button_state["button_up"]:
                a_button = constants.button_state["button_just_pressed"]
            elif a_button == constants.button_state["button_just_pressed"]:
                a_button = constants.button_state["button_still_pressed"]
        else:
            if a_button == constants.button_state["button_still_pressed"]:
                a_button = constants.button_state["button_released"]
            else:
                a_button = constants.button_state["button_up"]

        if keys & ugame.K_O != 0:  # B button
            if b_button == constants.button_state["button_up"]:
                b_button = constants.button_state["button_just_pressed"]
            elif b_button == constants.button_state["button_just_pressed"]:
                b_button = constants.button_state["button_still_pressed"]
        else:
            if b_button == constants.button_state["button_still_pressed"]:
                b_button = constants.button_state["button_released"]
            else:
                b_button = constants.button_state["button_up"]

        # IF one of the d pad is being pressed, move the prticles with snakob
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

        # if the a button is pressed, move rocks across the screen
        if a_button == constants.button_state["button_just_pressed"]:
            for rock_number in range(len(rocks)):
                if rock_number == 3:
                        break
                elif rocks[rock_number].x < 0:
                        rocks[rock_number].move(snakob_bank.x, snakob_bank.y)
                        rock_direction[rock_number] = snakob_direction
                        sound.stop()
                        sound.play(pew_sound)

        if b_button == constants.button_state["button_just_pressed"]:
            if swords1_bank.x < 0:
                spark_bank.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
            elif swords_bank.x < 0:
                spark_bank.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # makes the rocks move across the screen acoring to snakobs orientation
        for rock_number in range(len(rocks)):
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

        # this is the clock to make health packs apeer
        for counter in range(1, 61):
            if counter == 60:
                timer = timer + 1
                if timer == 300:
                    health()
                    timer = 0
                else:
                    continue

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

        # This detects if any rocks hit snakes heading right
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

        # this detects if snakob has collided with an apple
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

        # if the hearts are equal to zero, the game is over
        if health_hearts == 0:
            game_over_scene(score)

        # redraw sprite list
        game.render_sprites(snakob + apples + cloud + sprites + sparks + swords + rocks + bottom_snakes + top_snakes + left_snakes + right_snakes)
        game.tick() # wait until refresh rate finishes

def game_over_scene(final_score):
    # this function is the game over scene
    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []

    text0 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text0.move(22, 20)
    text0.text("Final Score: {:0>2d}".format(final_score))
    text.append(text0)

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(43, 60)
    text1.text("GAME OVER")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(32, 110)
    text2.text("PRESS SELECT")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input
        # update game logic
        keys = ugame.buttons.get_pressed()
        #print(keys)

        if keys & ugame.K_SELECT != 0:  # Start button
            keys = 0
            main_menu_scene()
            #break

        # redraw sprite list


if __name__ == "__main__":
    blank_white_reset_scene()