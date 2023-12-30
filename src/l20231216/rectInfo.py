import pygame
import  sys
if __name__ == '__main__':
    pygame.init()
    player = pygame.image.load("resource/player.png")
    screen = pygame.display.set_mode(( 800, 600))
    playerRect =player.get_rect()
    print( type(playerRect))
    print( playerRect.topleft )
    screen.fill((255,255,255))
    playerRect.topleft = (0,0)
    screen.blit(player , playerRect)
    playerRect.topright= (800 , 0)
    print(player.get_rect().topright)
    screen.blit(player , playerRect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #pygame.display.update()
