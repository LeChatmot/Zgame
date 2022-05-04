import pygame
import random
import math


class Zombie(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.player = self.game.player
        self.health = 100
        self.max_health = 100
        self.velocity = 1
        self.attack = 0.2
        self.sens = 6
        self.image = pygame.image.load("sprites/zombie.png")
        self.origine_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,1080)
        self.rect.y = -50
        self.rotate()

    def damage(self,amount):
        self.health -= amount

        if self.health <= 0:
            self.rect.x = random.randint(0,1080)
            self.rect.y = -50
            self.health = self.max_health

    def update_health_bar(self,surface):

        #dessiner la barre
        pygame.draw.rect(surface, (0, 0, 0), [self.rect.x, self.rect.centery - 35, int(self.max_health / 2), 5])
        if self.health>self.max_health/4:
            pygame.draw.rect(surface, (111, 210, 45), [self.rect.x , self.rect.centery - 35, int(self.health/2), 5])
        else:
            pygame.draw.rect(surface, (255, 29, 29), [self.rect.x , self.rect.centery - 35, int(self.health/2), 5])

    def rotate(self):
        if self.sens == 1:
            self.angle = 225
            self.image = pygame.transform.rotozoom(self.origine_image,self.angle,1)
        elif self.sens == 2:
            self.angle = 180
            self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        elif self.sens == 3:
            self.angle = 135
            self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        elif self.sens == 4:
            self.angle = 90
            self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        elif self.sens == 5:
            self.angle = 45
            self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        elif self.sens == 6:
            self.angle = 0
            self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        elif self.sens == 7:
            self.angle = 315
            self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)
        elif self.sens == 8:
            self.angle = 270
            self.image = pygame.transform.rotozoom(self.origine_image, self.angle, 1)

    def zmove_left(self):
        if not self.game.check_colision(self, self.game.all_player): #and not self.game.check_colision(self, self.game.all_zombies):
            self.rect.x -= self.velocity
    def zmove_right(self):
        if not self.game.check_colision(self, self.game.all_player): #and not self.game.check_colision(self, self.game.all_zombies):
            self.rect.x += self.velocity
    def zmove_up(self):
        if not self.game.check_colision(self, self.game.all_player): #and not self.game.check_colision(self, self.game.all_zombies):
            self.rect.y -= self.velocity
    def zmove_down(self):
        if not self.game.check_colision(self, self.game.all_player): #and not self.game.check_colision(self, self.game.all_zombies):
            self.rect.y += self.velocity
        #degat joueur
        else:
            self.game.player.damage(self.attack)

    def get_sens(self):

        sens = self.sens

        targetY = self.player.rect.centery
        targetX = self.player.rect.centerx

        myradians = math.atan2(targetY - self.rect.centery, targetX - self.rect.centerx)

        mydeegres = math.degrees(myradians)

        if mydeegres <= -120 and mydeegres > -150:
            sens = 1
        elif mydeegres <= -60 and mydeegres > -120:
            sens = 2
        elif mydeegres <= -30 and mydeegres > -60:
            sens = 3
        elif mydeegres <= 30 and mydeegres > -30:
            sens = 4
        elif mydeegres <= 60 and mydeegres > 30:
            sens = 5
        elif mydeegres <= 120 and mydeegres > 60:
            sens = 6
        elif mydeegres <= 150 and mydeegres > 120:
            sens = 7
        elif mydeegres <= 180 and mydeegres > 150:
            sens = 8

        return sens

    def zmove(self):
        self.sens = self.get_sens()
        self.rotate()
        if self.sens == 1:
            self.zmove_left()
            self.zmove_up()
        elif self.sens == 2:
            self.zmove_up()
        elif self.sens == 3:
            self.zmove_up()
            self.zmove_right()
        elif self.sens == 4:
            self.zmove_right()
        elif self.sens == 5:
            self.zmove_down()
            self.zmove_right()
        elif self.sens == 6:
            self.zmove_down()
        elif self.sens == 7:
            self.zmove_down()
            self.zmove_left()
        elif self.sens == 8:
            self.zmove_left()