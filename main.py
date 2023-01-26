import pygame
import random
import time
from button import Button
pygame.init()

clock = pygame.time.Clock

# Constants
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 510

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

GREEN_ON = (0, 255, 0)
GREEN_OFF = (0, 227, 0)
RED_ON = (255, 0, 0)
RED_OFF = (227, 0, 0)
BLUE_ON = (0, 0, 255)
BLUE_OFF = (0, 0, 227)
YELLOW_ON = (255, 255, 0)
YELLOW_OFF = (227, 227, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT = pygame.font.Font(pygame.font.get_default_font(), 16)

# Pass in respective sounds for each color
GREEN_SOUND = pygame.mixer.Sound("bell1.mp3") # bell1
RED_SOUND = pygame.mixer.Sound("bell2.mp3") # bell2
BLUE_SOUND = pygame.mixer.Sound("bell3.mp3") # bell3
YELLOW_SOUND = pygame.mixer.Sound("bell4.mp3") # bell4

# Button Objects
green = Button(GREEN_ON, GREEN_OFF, GREEN_SOUND, 10, 20)
red = Button(RED_ON, RED_OFF, RED_SOUND, 260, 20)
blue = Button(BLUE_ON, BLUE_OFF, BLUE_SOUND, 10, 270)
yellow = Button(YELLOW_ON, YELLOW_OFF, YELLOW_SOUND, 260, 270)

# Variables
colors = ["green", "red", "blue", "yellow"]
cpu_sequence = []
choice = ""

# Score Text
score = 0
score_text = FONT.render("Score: ", True, WHITE)

def draw_board():
    SCREEN.fill(BLACK)
    green.draw(SCREEN)
    red.draw(SCREEN)
    blue.draw(SCREEN)
    yellow.draw(SCREEN)
    score_text = FONT.render("Score: " + str(score), True, WHITE)
    SCREEN.blit(score_text, score_text.get_rect())

def cpu_turn():
    choice = random.choice(colors)
    cpu_sequence.append(choice)
    if choice == "green":
        green.update(SCREEN)
    if choice == "red":
        red.update(SCREEN)
    if choice == "blue":
        blue.update(SCREEN)
    if choice == "yellow":
        yellow.update(SCREEN)

def repeat_cpu_sequence():
    if(len(cpu_sequence) != 0):
        for color in cpu_sequence:
            if color == "green":
                green.update(SCREEN)
            elif color == "red":
                red.update(SCREEN)
            elif color == "blue":
                blue.update(SCREEN)
            else:
                yellow.update(SCREEN)
            pygame.time.wait(500)

def player_turn():
    turn_time = time.time()
    players_sequence = []
    while time.time() <+ turn_time + 3 and len(players_sequence) < len(cpu_sequence):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                if(green.selected(pos)):
                    green.update(SCREEN)
                    players_sequence.append("green")
                    check_sequence(players_sequence)
                    turn_time = time.time()

                if(red.selected(pos)):
                    red.update(SCREEN)
                    players_sequence.append("red")
                    check_sequence(players_sequence)
                    turn_time = time.time()

                if(blue.selected(pos)):
                    blue.update(SCREEN)
                    players_sequence.append("blue")
                    check_sequence(players_sequence)
                    turn_time = time.time()

                if(yellow.selected(pos)):
                    yellow.update(SCREEN)
                    players_sequence.append("yellow")
                    check_sequence(players_sequence)
                    turn_time = time.time()

    if not time.time() <= turn_time + 3:
        game_over()

def check_sequence(player_sequence):
    global score
    if player_sequence != cpu_sequence[:len(player_sequence)]:
        game_over()

def game_over():
    pygame.quit()
    quit()

# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            quit()
        pygame.display.update()

        draw_board() # draws buttons onto pygame screen
        repeat_cpu_sequence() # repeats cpu sequence if it's not empty
        cpu_turn() # cpu randomly chooses a new color
        player_turn() # player tries to recreate cpu sequence
        score += 1
        pygame.time.wait(1000) # waits one second before repeating cpu sequence