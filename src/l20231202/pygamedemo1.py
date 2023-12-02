import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth, screenheight))

# Background
background = pygame.image.load('background.png')

playerImg = pygame.image.load('player.png')
#print( f"width:{playerImg.get_width()}" )
#print( f"height:{playerImg.get_height()}" )
#playerX = 370
playerX = (screenwidth-playerImg.get_width())//2
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    eventList =pygame.event.get()
    #print ( len ( eventList ) )
    for event in eventList:
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_UP:
                playerY_change = -5
            if event.key == pygame.K_DOWN:
                playerY_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    playerY += playerY_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    if playerY<=0:
        playerY=0
    elif playerY>=536:
        playerY = 536
    #print(f"{playerX}, {playerY}")
    player(playerX, playerY)
    pygame.display.update()
