import math
import random
import functools
from pygame import mixer
import pygame
from typing_extensions import Self
class MovableObject:

    def __init__(self, screen: pygame.Surface, imageFile: str):
        self.screen = screen
        self.spaceObject = pygame.image.load(imageFile)
        self.maxX = self.screen.get_width() - self.spaceObject.get_width()
        self.maxY = self.screen.get_height() - self.spaceObject.get_height()
        self.positionX= 0
        self.positionY= 0

    def move(self):
        self.screen.blit(self.spaceObject, (self.positionX,self.positionY))

    def setChangeX(self , x):
        self.changeX = x
    def setChangeY(self, y):
        self.changeY = y

    def stop(self):
        self.setChangeX(0)
        self.setChangeY(0)
    def distance(self , another: Self)->float:
        return math.sqrt( (self.positionX - another.positionX) **2  + (self.positionY - another.positionY)**2 )
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
    def getPositionY(self):
        return self.positionY
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
        self.move()

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
        self.move()

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
        deepPos = functools.reduce(max , ypositions)
        return deepPos

    def stop(self):
        map( lambda enemy: enemy.stop(), self.enemies)

    def __iter__(self):
        return  iter( self.enemies )

class Bullet(MovableObject):
    epsilon = 27
    def __init__(self, screen:pygame.Surface , imageFile: str):
        super().__init__(screen, imageFile)
        self.changeX = 0
        self.changeY = -10
        # Ready - You can't see the bullet on the screen
        # Fire - The bullet is currently moving
        self.reset()
        self.explosionSound = mixer.Sound("resource/sounds/explosion.wav")

    def reset(self):
        self.positionY= self.maxY+ self.spaceObject.get_height()
        self.bullet_state = "ready"

    def fire(self , x , y):
        if self.bullet_state == "ready":
            self.bullet_state = "fire"
            self.positionX = x +16
            self.positionY = y +10
            self.move()
    def changePosition(self):
        if self.bullet_state == "fire":
            self.positionY += self.changeY
            if self.positionY<=0:
                self.reset()
            else:
                self.move()

    def CollisionEnemy(self , enemies:EnemyGroup):
        if self.bullet_state =="ready":
            return ()
        collisionEnemies =[enemy for enemy in enemies if self.distance(enemy)< self.epsilon]
        return collisionEnemies

    def explore(self):
        self.explosionSound.play()
        self.reset()


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
        self.score = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.over_text = pygame.font.Font('freesansbold.ttf', 64).render("GAME OVER", True, (255, 255, 255))

    def run(self):
        while self.running:
            self.screen.fill((0,0,0))
            self.screen.blit(self.background,(0,0))
            for event in pygame.event.get():
                self.handleEvent(event)
            if self.isGameOver():
                self.over =True
            self.handleCollision()
            self.updateScreen()
    def updateScreen(self):
        self.enemies.changePosition()
        self.player.changePosition()
        self.bullet.changePosition()
        self.show_score()
        self.showGameOver()
        pygame.display.update()

    def handleCollision(self):
        collisionEnemies:list[Enemy] =self.bullet.CollisionEnemy(self.enemies)
        if len(collisionEnemies) >0:
            self.bullet.explore()
            for enemy in collisionEnemies:
                enemy.reset()
            self.score +=1

    def isGameOver(self):
        return self.enemies.getTheDeepPosition() >= self.screenheight

    def show_score(self):
        score = self.font.render("Score : " + str(self.score), True, (255, 255, 255))
        self.screen.blit(score, (10, 10))

    def showGameOver(self):
        if self.over :
            x =(self.screen.get_width()- self.over_text.get_width())/2
            y =(self.screen.get_height() - self.over_text.get_height())/2
            self.screen.blit(self.over_text, (x, y))

    def gameOver(self):
        self.enemies.stop()
        self.player.stop()
        self.bullet.stop()
        self.over = True
        print("game over!!!")

    def handleEvent(self,event):
        if event.type == pygame.QUIT:
            self.running = False
        if self.over :
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
                positionY =self.player.getPositionY()
                self.bullet.fire(positionX, positionY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                self.player.setChangeX(0)
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                self.player.setChangeY(0)

if __name__ =="__main__":
    game = Game(800 , 600)
    game.run()