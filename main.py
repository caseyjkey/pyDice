# A simple dice rolling tool made to gain experience with pygame!
import random
import pygame

# globals
pygame.init()
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
DICE_NUMBER = 2
FIRST_DICE = 0
SECOND_DICE = 0

# Colors  R    G    B
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

pygame.display.set_caption("Street Dice")
DISPLAYSURF = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
BASICFONT = pygame.font.SysFont("monospace", 15)
FPSCLOCK = pygame.time.Clock()
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
    Two dice are randomly rolled and have their values returned.

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


# tells the user how to roll
def produce_button_message(text):
    #  render the text now
    produce_text = BASICFONT.render(text, 1, RED)
    DISPLAYSURF.blit(produce_text, (SCREEN_WIDTH/8, SCREEN_HEIGHT/5))


# produce the roll results (in text)
def produce_roll_message(text):
    #  render the text now. 1 refers to aliasing.
    produce_text = BASICFONT.render(text, 1, RED)
    DISPLAYSURF.blit(produce_text, (SCREEN_WIDTH/8, SCREEN_HEIGHT/2 + 20))


# determines which first dice is used
def display_first(first):
    if first == 1:
        DISPLAYSURF.blit(dice_one, (SCREEN_WIDTH/4, 0))
    elif first == 2:
        DISPLAYSURF.blit(dice_two, (SCREEN_WIDTH/4, 0))
    elif first == 3:
        DISPLAYSURF.blit(dice_three, (SCREEN_WIDTH/4, 0))
    elif first == 4:
        DISPLAYSURF.blit(dice_four, (SCREEN_WIDTH/4, 0))
    elif first == 5:
        DISPLAYSURF.blit(dice_five, (SCREEN_WIDTH/4, 0))
    elif first == 6:
        DISPLAYSURF.blit(dice_six, (SCREEN_HEIGHT/4, 0))


# determines which second dice is used
def display_second(second):
    if second == 1:
        DISPLAYSURF.blit(dice_one, (SCREEN_WIDTH/2, 0))
    elif second == 2:
        DISPLAYSURF.blit(dice_two, (SCREEN_WIDTH/2, 0))
    elif second == 3:
        DISPLAYSURF.blit(dice_three, (SCREEN_WIDTH/2, 0))
    elif second == 4:
        DISPLAYSURF.blit(dice_four, (SCREEN_WIDTH/2, 0))
    elif second == 5:
        DISPLAYSURF.blit(dice_five, (SCREEN_WIDTH/2, 0))
    elif second == 6:
        DISPLAYSURF.blit(dice_six, (SCREEN_HEIGHT/2, 0))


def our_roll(player):
    #  Completed roll Message. Cast int to str to output the message clearly
    text = player + " rolled " + str(FIRST_DICE) + "," + str(SECOND_DICE) + "."
    print(text)
    produce_roll_message(text)

def roll():

    DISPLAYSURF.fill(WHITE)

    produce_button_message("Please hit space to roll your dice")
    display_dice(FIRST_DICE, SECOND_DICE)
    # If the roll is requested, our_roll will execute.
    if roll_occur:
        our_roll()
        roll_occur = False

    pygame.display.update()
    FPSCLOCK.tick(30)


""" -------------- Get # of Players, Get the players' names. -------------- """


def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == pygame.KEYDOWN:
            return event.key
        else:
            pass


def display_box(screen, message):
    """Print a message in a box in the middle of the screen"""
    pygame.draw.rect(screen, (0, 0, 0),
                   ((screen.get_width() / 2) - 100,
                    (screen.get_height() / 2) - 10,
                    200, 20), 0)
    pygame.draw.rect(screen, (255, 255, 255),
                   ((screen.get_width() / 2) - 102,
                    (screen.get_height() / 2) - 12,
                    204, 24), 1)
    if len(message) != 0:
        screen.blit(BASICFONT.render(message, 1, (255,255,255)),
                    ((screen.get_width() / 2) - 100, (screen.get_height() / 2) - 10))
    pygame.display.flip()


def ask(screen, question):
    """ask(screen, question) -> answer"""
    pygame.font.init()
    current_string = []
    display_box(screen, question + ": " + ''.join(current_string))
    while 1:
        inkey = get_key()
        if inkey == pygame.K_BACKSPACE:
            current_string = current_string[0:-1]
        elif inkey == pygame.K_RETURN:
            break
        elif inkey == pygame.K_MINUS:
            current_string.append("_")
        elif inkey <= 127:
            current_string.append(chr(inkey))
        display_box(screen, question + ": " + ''.join(current_string))
    return ''.join(current_string)

""" ------------------ END OF ASK FUNCTIONS ---------------------- """

def quit():
    pygame.display.quit()
    pygame.quit()
    exit()


""" 
Main Game Loop

1) Roll dice to see who goes first, usually highest first.

2) Each player puts their ante into the pot.

3) A point is obtained for rolling a 7 or 11. 

4) Penalties are paid for rolling a 2, 3, or 12 (craps). 

5) Two points wins the pot, given the second point survives the challenge round (see Rule 9).

6) Rolling a 4, 5, 6, 8, 9, or 10 (the numbers) is inconsequential, nothing happens, except when rolling doubles (See Rule 8: Rolling doubles, gives a re-roll). 

7) The penalty for rolling a 2 or a 12 is to match the ante into the pot. The penalty for rolling a 3 is to put half the ante into the pot. 

8) Rolling doubles, gives a re-roll. Rolling three doubles in a row eliminates the player from that game. 

9) When a player acquires the second point, the game continues for one more round. If any of the other players roll a 7 or 11 they do not receive a point. Their 7 or 11 is used to cancel the second point of the player set to win the game. If a player’s second point gets cancelled, the dice go back to the player that the point got cancelled from and the game continues, i.e., the only way to win the pot is to acquire two points and be able to keep the second point through this last round challenge.
"""
# get player names, determine who starts first
num_players = ask(DISPLAYSURF, "How many players?")
produce_button_message(num_players)



# We don't want our roll value output before the first roll occurs.
roll_occur = False
game_step = 1
while not already_rolled:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # these values below don't get saved. I need to save them somehow :(
                FIRST_DICE = roll_a_dice()
                SECOND_DICE = roll_a_dice()
                roll_occur = True

    DISPLAYSURF.fill(WHITE)

    produce_button_message("Please hit space to roll your dice")

    if roll_occur:
        if game_step == 1:
            # Create dictionary where key is the player order from 1 to n
            players = {}
            for player in range(1, int(num_players)+1):
                name = ask(DISPLAYSURF, "Player " + str(player) + "'s name")
                player_roll = None
                while player_roll is None:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            DISPLAYSURF.fill(WHITE)
                            FIRST_DICE = roll_a_dice()
                            SECOND_DICE = roll_a_dice()
                            player_roll = FIRST_DICE + SECOND_DICE
                            players[name] = player_roll
                            display_dice(FIRST_DICE, SECOND_DICE)
                            our_roll(name)

        # Outputs text of roll outcome
        #our_roll()



        roll_occur = False




    pygame.display.update()
    FPSCLOCK.tick(30)

# Once the loop exits, the program will quit.
# Loop will exit when the 'Exit' button on the window is clicked.This bit of code just ensures you can actually
# click that and exit.
quit()
