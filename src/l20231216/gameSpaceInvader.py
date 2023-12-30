import random
import functools
from pygame import mixer
import pygame
class MovableObject:
    def __init__(self, screen: pygame.Surface, imageFile: str):
        self.screen = screen
        self.spaceObject = pygame.image.load(imageFile)
        self.maxX = self.screen.get_width() - self.spaceObject.get_width()
        self.maxY = self.screen.get_height() - self.spaceObject.get_height()

    def move(self, x, y):
        self.screen.blit(self.spaceObject, (x,y))

    def setChangeX(self , x):
        self.changeX = x
    def setChangeY(self, y):
        self.changeY = y

    def stop(self):
        self.setChangeX(0)
        self.setChangeY(0)
    #def move(self , rect: pygame.rect.Rect):
    #    self.screen.blit(self.spaceObject , rect)

class Player(MovableObject):
    def __init__(self, screen:pygame.Surface , imageFile: str):
        super().__init__(screen  , imageFile)
        self.positionX = (self.screen.get_width() - self.spaceObject.get_width())//2
        self.positionY = self.screen.get_height() - self.spaceObject.get_height()
        self.setChangeX(0)
        self.setChangeY(0)

    def getPositionX(self):
        return self.positionX
    def changePosition(self):
        self.positionX +=self.changeX
        self.positionY +=self.changeY
        if self.positionX <=0:
            self.positionX = 0
        elif self.positionX >= self.maxX:
            self.positionX = self.maxX
        if self.positionY<=0:
            self.positionY =0
        elif self.positionY>= self.maxY:
            self.positionY=self.maxY
        self.move(self.positionX , self.positionY)

class Enemy(MovableObject):
    def __init__(self, screen:pygame.Surface , imageFile: str):
        super().__init__(screen  , imageFile)
        self.setChangeX(4)
        self.setChangeY(40)
        self.reset()
    def reset(self):
        self.positionX = random.randint(0, self.maxX)
        self.positionY = random.randint(50, 150)

    def changePosition(self):
        self.positionX += self.changeX
        #self.positionY += self.changeY
        if self.positionX>self.maxX:
            self.positionX = 0
            self.positionY += self.changeY
        # if self.positionY>= self.maxY:
        #     self.positionY = 0
        self.move(self.positionX , self.positionY)

class EnemyGroup:
    def __init__(self , screen:pygame.Surface , imageFile: str ,count:int):
        self.count = count
        self.enemies =[Enemy(screen , imageFile) for i in range(0 , self.count)]
        # for i in range(0 , self.count):
        #     self.enemies.append( Enemy(screen,imageFile))
    def changePosition(self):
        for enemy in self.enemies:
            enemy.changePosition()

    def getTheDeepPosition(self):
        ypositions =[ enemy.positionY for enemy in self.enemies]
        return  functools.reduce(max , ypositions)

    def stop(self):
        map( lambda enemy: enemy.stop(), self.enemies)

class Bullet(MovableObject):
    def __init__(self, screen:pygame.Surface , imageFile: str):
        super().__init__(screen, imageFile)
        self.changeX = 0
        self.changeY = -10
        # Ready - You can't see the bullet on the screen
        # Fire - The bullet is currently moving
        self.reset()

    def reset(self):
        self.bulletY= self.maxY+ self.spaceObject.get_height()
        self.bullet_state = "ready"

    def fire(self , x , y):
        if self.bullet_state == "ready":
            self.bullet_state = "fire"
            self.postitionX = x +16
            self.postitionY = y +10
            self.move(self.postitionX , self.postitionY)
    def changePosition(self):
        if self.bullet_state == "fire":
            self.postitionY += self.changeY
            if self.postitionY<=0:
                self.reset()
            else:
                self.move(self.postitionX , self.postitionY)

class Game:
    def __init__(self, width , height):
        pygame.init()
        self.screenwidth = width
        self.screenheight = height
        self.screen = pygame.display.set_mode((self.screenwidth , self.screenheight))
        self.background = pygame.image.load('resource/background.png')
        # Sound
        mixer.music.load("resource/sounds/background.wav")
        mixer.music.play(-1)

        # Caption and Icon
        pygame.display.set_caption("Space Invader")
        icon = pygame.image.load('resource/ufo.png')
        pygame.display.set_icon(icon)

        self.player = Player(self.screen, 'resource/player.png')
        self.enemies = EnemyGroup(self.screen, 'resource/enemy.png', 6)
        self.bullet = Bullet(self.screen, 'resource/bullet.png')
        self.running = True
        self.over = False
    def run(self):
        while self.running:
            self.screen.fill((0,0,0))
            self.screen.blit(self.background,(0,0))
            for event in pygame.event.get():
                self.handleEvent(event)
            self.updateScreen()
    def updateScreen(self):
        self.enemies.changePosition()
        self.player.changePosition()
        self.bullet.changePosition()
        pygame.display.update()

    def isGameOver(self):
        return self.enemies.getTheDeepPosition() >= self.screenheight

    def gameOver(self):
        self.enemies.stop()
        self.player.stop()
        self.bullet.stop()
        self.over = True
        print("game over!!!")

    def handleEvent(self,event):
        if event.type == pygame.QUIT:
            self.running = False
        if self.over:
            return
        elif self.isGameOver():
            self.gameOver()
            return
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.player.setChangeX(-5)
            if event.key == pygame.K_RIGHT:
                self.player.setChangeX(5)
            if event.key == pygame.K_UP:
                self.player.setChangeY(-5)
            if event.key == pygame.K_DOWN:
                self.player.setChangeY(5)
            if event.key == pygame.K_SPACE:
                positionX = self.player.getPositionX()
                self.bullet.fire(positionX, 480)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.player.setChangeX(0)
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.player.setChangeY(0)

if __name__ =="__main__":
    game = Game(800 , 600)
    game.run()