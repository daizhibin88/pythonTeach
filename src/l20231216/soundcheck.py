import time

import pygame
if __name__ == '__main__':
    pygame.init()
    background =pygame.mixer.Sound("resource/sounds/explosion.wav")
    background.play()
    pygame.time.delay(2000)
    print( background.get_volume())
    background.set_volume(0.1)
    print(background.get_volume())
    background.play()
    pygame.time.delay(2000)
    pygame.mixer.music.load("resource/sounds/background.wav")
    pygame.mixer.music.play(-1 , 0.0)
    pygame.time.delay(2000)
