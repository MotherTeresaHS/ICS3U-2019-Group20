#!/usr/bin/env python3

# Created by: Cameron and RJ 
# Created on: Dec 2019
# This is the main file for Snakob's forest for CircuitPython

import ugame
import stage
import board
import neopixel
import time
import random
import constants


def blank_white_reset_scene():
    # this function is the splash scene game loop

    # do house keeping to ensure everythng is setup

    # set up the NeoPixels
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    pixels.deinit() # and turn them all off

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

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)

    text2.move(30, 110)
    text2.text("In association")
    text.append(text2)
    
    text3 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text3.move(5, 120)
    text3.text("with Snakob studios")
    text.append(text3)


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

        # Wait for 1 seconds
        time.sleep(1.0)
        main_menu_scene()

        # redraw sprite list

def game_splash_scene():

    # this function is the MT splash scene

    
    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1 seconds
        time.sleep(1.0)
        main_menu_scene()

        # redraw sprite list
    # this function is the game scene

def main_menu_scene():
    # this function is the Main menu

    # an image bank for CircuitPython
    image_bank_3 = stage.Bank.from_bmp16("tree.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_3, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    sprites = []

    background.tile(2, 2, 0)



    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    top_right_of_tree = stage.Sprite(image_bank_3, 13, 65, 116)
    sprites.append(top_right_of_tree)
    top_middle_of_tree = stage.Sprite(image_bank_3, 14, 81, 116)
    sprites.append(top_middle_of_tree)
    top_of_tree = stage.Sprite(image_bank_3, 9, 65, 100)
    sprites.append(top_of_tree)
    top_left_of_tree = stage.Sprite(image_bank_3, 10, 81, 100)
    sprites.append(top_left_of_tree)
    middle_right_of_tree = stage.Sprite(image_bank_3, 5, 65, 84)
    sprites.append(middle_right_of_tree)
    middle_of_tree = stage.Sprite(image_bank_3, 6, 81, 84)
    sprites.append(middle_of_tree)
    middle_left_of_tree = stage.Sprite(image_bank_3, 4, 49, 84)
    sprites.append(middle_left_of_tree)
    bottem_right_of_tree = stage.Sprite(image_bank_3, 7, 97, 84)
    sprites.append(bottem_right_of_tree)
    bottem_midle_of_tree = stage.Sprite(image_bank_3, 1, 65, 68)
    sprites.append(bottem_midle_of_tree)
    bottem_left_of_tree = stage.Sprite(image_bank_3, 3, 81, 68)
    sprites.append(bottem_left_of_tree)
    verybottem_right_of_tree = stage.Sprite(image_bank_3, 2, 97, 68)
    sprites.append(verybottem_right_of_tree)
    verybottem_middle_of_tree = stage.Sprite(image_bank_3, 11, 97, 100)
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
            star = stage.Sprite(image_bank_3, 15, random.randint(0, 160),random.randint(0, 128))
            stars.append(star)
            
        game.layers = text + sprites + stars + [background]
        game.render_block()




    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code


def game_scene():
    # this function is the game scene

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code


def game_over_scene(final_score):
    # this function is the game over scene

    # repeat forever, game loop
    while True:
        # get user input
        # update game logic

        # redraw sprite list
        pass # just a placeholder until you write the code



if __name__ == "__main__":
    blank_white_reset_scene()