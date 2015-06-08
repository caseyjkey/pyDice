__author__ = 'alek hrycaiko'

# A simple dice (die? dice?) rolling tool made to gain experience with pygame!

import random
import pygame
#globals
pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
DICE_NUMBER = 2
FIRST_DICE = 0
SECOND_DICE = 0
#Defines colours (not built in)
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

pygame.display.set_caption("Dice Roller (with images!)")
gameDisplay = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
clock = pygame.time.Clock()
already_rolled = False

# Import Images for Dice 1-6
dice_one = pygame.image.load("dice_one.png")
dice_two = pygame.image.load("dice_two.png")
dice_three = pygame.image.load("dice_three.png")
dice_four = pygame.image.load("dice_four.png")
dice_five = pygame.image.load("dice_five.png")
dice_six = pygame.image.load("dice_six.png")


def roll_a_dice():
    """
    # Two dice are randomlly rolled and have their values returned.

    >>> roll_dice()
    0
    >>> roll_dice()
    1
    >>> roll_dice()
    6
    """
    dice = random.randrange(1, 6);

    return dice

def display_dice(first, second):
    display_first(first)
    display_second(second)
# determines which first dice is used
def display_first(first):
    if (first == 1):
        gameDisplay.blit(dice_one,(SCREEN_WIDTH/4,0))
    elif (first == 2):
        gameDisplay.blit(dice_two,(SCREEN_WIDTH/4,0))
    elif (first == 3):
        gameDisplay.blit(dice_three,(SCREEN_WIDTH/4,0))
    elif (first == 4):
        gameDisplay.blit(dice_four, (SCREEN_WIDTH/4, 0))
    elif (first == 5):
        gameDisplay.blit(dice_five, (SCREEN_WIDTH/4, 0))
    elif (first == 6):
        gameDisplay.blit(dice_six, (SCREEN_HEIGHT/4, 0))
# determines which second dice is used
def display_second(second):
    if (second == 1):
        gameDisplay.blit(dice_one,(SCREEN_WIDTH/2,0))
    elif (second == 2):
        gameDisplay.blit(dice_two,(SCREEN_WIDTH/2,0))
    elif (second == 3):
        gameDisplay.blit(dice_three,(SCREEN_WIDTH/2,0))
    elif (second == 4):
        gameDisplay.blit(dice_four, (SCREEN_WIDTH/2, 0))
    elif (second == 5):
        gameDisplay.blit(dice_five, (SCREEN_WIDTH/2, 0))
    elif (second == 6):
        gameDisplay.blit(dice_six, (SCREEN_HEIGHT/2, 0))
# tells the user how to roll
def produce_button_message(text):
    our_font = pygame.font.SysFont("monospace", 15)
    #render the text now
    produce_text = our_font.render(text, 1, red)
    gameDisplay.blit(produce_text, (SCREEN_WIDTH/8, SCREEN_HEIGHT/5))

# produce the roll results (in text)
def produce_roll_message(text):
    our_font = pygame.font.SysFont("monospace", 15)
    #render the text now. 1 refers to aliasing.
    produce_text = our_font.render(text, 1, red)
    gameDisplay.blit(produce_text, (SCREEN_WIDTH/8, SCREEN_HEIGHT/2))

# our roll will display message with our roll converted to text form, alongside
def before_roll():
    produce_button_message("Please hit space to roll your dice")

def our_roll():
     #Completed roll Message. Cast int to str to output the message clearly
     text = "You've completed your roll " + str(FIRST_DICE) + "," + str(SECOND_DICE) + "."
     print(text)
     produce_roll_message(text)

# We don't want our roll value output before the first roll occurs.
roll_occur = False
while already_rolled == False:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            already_rolled = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:#these values below don't get saved. I need to save them somehow :(
             FIRST_DICE = roll_a_dice()
             SECOND_DICE = roll_a_dice()
             roll_occur = True

    gameDisplay.fill(white)
    before_roll()
    display_dice(FIRST_DICE, SECOND_DICE)
    # If the roll is requested, our_roll will execute.
    if (roll_occur):
        our_roll()
    pygame.display.update()
    clock.tick(30)
# Once the loop exits, the program will quit.
# Loop will exit when the 'Exit' button on the window is clicked.This bit of code just ensures you can actually
# click that and exit.
pygame.quit()
quit()
