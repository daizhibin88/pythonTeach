import pygame
import  sys
if __name__ == '__main__':
    pygame.init()
    for font in  pygame.font.get_fonts():
        print( font)

    system_font =pygame.font.SysFont('impaact', 40)
    downloaded_font  = pygame.font.Font("resource/fonts/SuperFunky-lgmWw.ttf", 40)

    #Render the text text
    text1 = system_font.render("This is Impact!", True , "blue" , "silver")
    text2 = downloaded_font.render("This is Danger!", True , "blue" , "silver")

    system_font_rect = text1.get_rect()
    user_font_rect = text2.get_rect()
    system_font_rect.center = (800//2 , 600//2)
    user_font_rect.center =  (800//2 , 600//2 +100)

    screen = pygame.display.set_mode(( 800, 600))
    screen.fill((255,255,255))
    screen.blit(text1 , system_font_rect)
    screen.blit(text2 , user_font_rect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            #pygame.display.update()
