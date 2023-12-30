import math
import random

import pygame
from pygame import mixer
from SpaceObject import Player
from SpaceObject import  EnemyGroup
from SpaceObject import  Bullet
# Intialize the pygame
pygame.init()

# create the screen
screenwidth = 800
screenheight = 600
screen = pygame.display.set_mode((screenwidth, screenheight))

# Background
background = pygame.image.load('resource/background.png')

# Sound
mixer.music.load("resource/background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('resource/ufo.png')
pygame.display.set_icon(icon)


player1 = Player(screen , 'resource/player.png')
enemies = EnemyGroup(screen , 'resource/enemy.png' , 6)
bullet = Bullet(screen , 'resource/bullet.png')
running = True
while running:

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    eventList =pygame.event.get()
    for event in eventList:
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player1.setChangeX(-5)
            if event.key == pygame.K_RIGHT:
                player1.setChangeX(5)
            if event.key == pygame.K_UP:
                player1.setChangeY(-5)
            if event.key == pygame.K_DOWN:
                player1.setChangeY(5)
            if event.key == pygame.K_SPACE:
                positionX =player1.getPositionX()
                bullet.fire(positionX , 480)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                player1.setChangeX(0)
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player1.setChangeY(0)

    enemies.changePosition()
    player1.changePosition()
    bullet.changePosition()
    pygame.display.update()

if __name__ =="__main__":
    pass