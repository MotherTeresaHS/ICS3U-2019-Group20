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
import neopixel


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
    sound.mute(True)
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

        # Wait for 3 seconds
        time.sleep(3.0)
        game_splash_scene()


        # redraw sprite list

def game_splash_scene():

      # this function is the Main menu


    # an image bank for CircuitPython
    image_bank_3 = stage.Bank.from_bmp16("game_splash_scene.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    sprites = []

    snakob = []

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
    sound.mute(True)
    sound.play(snake_sound)

    game = stage.Stage(ugame.display, 60)

    game.layers = text + snakob + [background]

    game.render_block()
   
    while True:
        # get user input
        # update game logic
        time.sleep(4.0)
        # redraw sprite list
        game.render_sprites(snakob)
        game.tick()
        main_menu_scene()

def main_menu_scene():


    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_4, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

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
    def show_snakes():
        # I know this is a function that is using variables outside of itself!
        #   BUT this code is going to be used in 2 places :)
        # make an alien show up on screen in the x-axis
        for snakob_number in range(len(snakes)):
            if snakes[snake_number].x < 0: # meaning it is off the screen, so available to move on the screen
                snakes[snake_number].move(random.randint(6 + constants.SPRITE_SIZE, constants.SCREEN_X - constants.SPRITE_SIZE), constants.OFF_TOP_SCREEN)


                break

    # buttons that you want to keep state information on
    a_button = constants.button_state["button_up"]
    b_button = constants.button_state["button_up"]
    start_button = constants.button_state["button_up"]
    select_button = constants.button_state["button_up"]

    # get sound ready

    pew_sound = open("swords.wav", 'rb')  # to change the wav volume: https://audioalter.com/volume/
    boom_sound = open("squish.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("SPRITES.bmp")
    # a list of sprites that will be updated every frame
    sprites = []
    
    image_bank_5 = stage.Bank.from_bmp16("background_for_game_scene.bmp")
    
    background_for_game_scene = []

    # create lasers for when we shoot
    rocks = []
    for rock_number in range(constants.TOTAL_NUMBER_OF_ROCKS):
        a_single_rock = stage.Sprite(image_bank_1, 15, constants.OFF_SCREEN_X, constants.OFF_SCREEN_X)
        rocks.append(a_single_rock)

    # create aliens
    snakes = []
    for snake_number in range(constants.TOTAL_NUMBER_OF_SNAKES):
        a_single_snake = stage.Sprite(image_bank_1, 7, constants.OFF_SCREEN_X, constants.OFF_SCREEN_X)
        snakes.append(a_single_snake)
    
    cloud = []
    a_single_cloud = stage.Sprite(image_bank_1, 11, constants.OFF_SCREEN_X, constants.OFF_SCREEN_X)
    cloud.append(a_single_cloud)
    
    def show_clouds(): 
        a_single_cloud.move(snakob_bank.x + constants.SNAKOB_SPEED, snakob_bank.y)
        a_single_cloud.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
        
        

    # current number of aliens that should be moving down screen, start with just 1

    snake_count = 1
    show_snakes()

    # add text at top of screen for score


    snakob = []
    snakob_bank = stage.Sprite(image_bank_1, 13, int(constants.SCREEN_X / 2), constants.SCREEN_Y - constants.SPRITE_SIZE)
    snakob.append(snakob_bank) # insert at the top of sprite list
    # append sword
    swords = []
    swords_bank = stage.Sprite(image_bank_1, 8, int((constants.SCREEN_X / 2) + 14), ((constants.SCREEN_Y - 4) - constants.SPRITE_SIZE))
    swords.append(swords_bank) # insert at the top of sprite list
    swords1_bank = stage.Sprite(image_bank_1, 9, int(constants.OFF_SCREEN_X), (constants.OFF_SCREEN_X - constants.SPRITE_SIZE))
    swords.append(swords1_bank) # insert at the top of sprite list

    # sets the background to image 0 in the bank
<<<<<<< HEAD
    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)
=======
    background = stage.Grid(image_bank_1, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y) 

>>>>>>> 91153dfa2f82b7ddff471ab2af198745db728112
    for x_location in range(constants.SCREEN_GRID_X):
        for y_location in range(constants.SCREEN_GRID_Y):
            boolean = random.randint(0 ,1)
            if boolean == 0:
                tile_picked = 0
            if boolean == 1:
                tile_picked = 14
            background.tile(x_location, y_location, tile_picked)

    snake_count = 1
    show_snakes()

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
<<<<<<< HEAD
    game.layers = cloud + snakob + snakes + swords + sprites + rocks + [background]
=======

    game.layers = snakob + snakes + swords + sprites + rocks + [background]
>>>>>>> 91153dfa2f82b7ddff471ab2af198745db728112
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()


    # repeat forever, game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        #print(keys)

        rocks_number =5


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

        # update game logic
        if keys & ugame.K_RIGHT != 0 or keys & ugame.K_LEFT != 0 or keys & ugame.K_DOWN != 0 or keys & ugame.K_UP != 0:
            a_single_cloud.move((snakob_bank.x - 3) + constants.SNAKOB_SPEED, (snakob_bank.y + 2))
            
        
        if keys & ugame.K_RIGHT == 0 and keys & ugame.K_LEFT == 0 and keys & ugame.K_DOWN == 0 and keys & ugame.K_UP == 0:
            a_single_cloud.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
            
        # if right D-Pad is pressed
        if keys & ugame.K_RIGHT != 0:
            # if ship moves off right screen, move it back

            if snakob_bank.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                snakob_bank.x = constants.SCREEN_X - constants.SPRITE_SIZE
            if swords_bank.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                swords_bank.x = constants.SCREEN_X - constants.SPRITE_SIZE
            # else move ship right
            else:
                snakob_bank.move(snakob_bank.x + constants.SNAKOB_SPEED, snakob_bank.y)
                swords_bank.move((snakob_bank.x + 14)+ constants.SNAKOB_SPEED, (snakob_bank.y) - 4)
                swords1_bank.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                

        # if left D-Pad is pressed
        if keys & ugame.K_LEFT != 0:
            # if ship moves off left screen, move it back
            if snakob_bank.x < 0:
                snakob_bank.x = 0
            if swords_bank.x < 16:
                swords_bank.x = 16
            # else move ship left
            else:
                snakob_bank.move(snakob_bank.x - constants.SNAKOB_SPEED, snakob_bank.y)
                swords1_bank.move((snakob_bank.x - 14) - constants.SNAKOB_SPEED, (snakob_bank.y - 4))
                swords_bank.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
    
        if keys & ugame.K_UP != 0:
            # if ship moves off up screen, move it back
            if snakob_bank.y < 0:
                snakob_bank.y = 0
            else:
                snakob_bank.move(snakob_bank.x, snakob_bank.y - 1)
                swords_bank.move((snakob_bank.x + 14), snakob_bank.y - 4)
                swords1_bank.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                snakob_direction = "up"

        # if left D-Pad is pressed
        if keys & ugame.K_DOWN != 0:
            # if ship moves off down screen, move it back
            if snakob_bank.y > 116:
                snakob_bank.y = 116
            # else move ship down
            else:
                snakob_bank.move(snakob_bank.x, snakob_bank.y + 1)
                swords_bank.move((snakob_bank.x + 14), snakob_bank.y - 4)
                swords1_bank.move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                snakob_direction = "down"
        
        if a_button == constants.button_state["button_just_pressed"]:
             if rocks[rock_number].x < 0:
                    rocks[rock_number].move(snakob_bank.x, snakob_bank.y)
                    break

        for rock_number in range(len(rocks)):
            if rocks[rock_number].x > 0:
                rocks[rock_number].move(rocks[rock_number].x, rocks[rock_number].y - constants.SNAKOB_SPEED)
            if rocks[rock_number].y < constants.OFF_TOP_SCREEN:
                rocks[rock_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)

        # each frame move the aliens down the screen
        for snake_number in range(len(snakes)):
            if snakes[snake_number].x > 0: # meaning it is on the screen
                snakes[snake_number].move(snakes[snake_number].x, snakes[snake_number].y + constants.SNAKE_SPEED)
                if snakes[snake_number].y > constants.SCREEN_Y:
                    snakes[snake_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                    show_snakes() # make it randomly show up at top again

        # each frame check if any of the lasers are touching any of the aliens
        for rock_number in range(len(rocks)):
            if rocks[rock_number].x > 0 :
                for snake_number in range(len(snakes)):
                    if snakes[snake_number].x > 0:
                        # https://circuitpython-stage.readthedocs.io/en/latest/#stage.collide
                        # and https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other
                        # the first 4 numbers are the coordinates of A box
                        # since the laser is thin, it made it thinner and slightly smaller
                        #
                        # the second 4 numbers are the alien, it is more of a box so I just made it slightly smaller
                        #
                        # if you slow down the FPS, then you can see the interaction more easily to alter these numbers
                        if stage.collide(rocks[rock_number].x + 6, rocks[rock_number].y + 2,
                                         rocks[rock_number].x + 11, rocks[rock_number].y + 12,
                                         snakes[snake_number].x + 1, snakes[snake_number].y,
                                         snakes[snake_number].x + 15, snakes[snake_number].y + 15):
                            # you hit an alien
                            snakes[snake_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            rocks[rock_number].move(constants.OFF_SCREEN_X, constants.OFF_SCREEN_Y)
                            # add 1 to the score
                            score += 1
                            score_text.clear()
                            score_text.cursor(0, 0)
                            score_text.move(1, 1)
                            score_text.text("Score: {0}".format(score))
                            # this will freeze the screen for a split second, but we have no option
                            game.render_block()
                            # play sound effect
                            sound.stop()
                            sound.play(boom_sound)
                            show_snake()
                            show_snake()
                            snake_count = snake_count + 1

        # each frame check if any of the aliens are touching the ship
        for snake_number in range(len(snakes)):
            if snakes[snake_number].x > 0:
                # https://circuitpython-stage.readthedocs.io/en/latest/#stage.collide
                # and https://stackoverflow.com/questions/306316/determine-if-two-rectangles-overlap-each-other
                if stage.collide(snakes[snake_number].x + 1, snakes[snake_number].y,
                                 snakes[snake_number].x + 15, snakes[snake_number].y + 15,
                                 snakob_bank.x, snakob_bank.y,
                                 snakob_bank.x + 15, snakob_bank.y + 15):
                                     
                    # alien hit the ship
                    # Wait for 1 seconds
                    time.sleep(4.0)
                    # need to release the NeoPixels
                    sound.stop()
                

        # redraw sprite list
        game.render_sprites(snakob + cloud + sprites + swords + rocks + snakes)
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
            menu_scene()
            #break

        # redraw sprite list


if __name__ == "__main__":
<<<<<<< HEAD
    blank_white_reset_scene()
=======
    blank_white_reset_scene()
>>>>>>> 91153dfa2f82b7ddff471ab2af198745db728112
