import pygame
import projectile
import math

#class joueur
class Player(pygame.sprite.Sprite):

    """
    sens:

    1   2   3
    8   X   4
    7   6   5

    """

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.sens = 6
        self.health = 100
        self.maxhealth = 100
        self.poids = 0
        self.maxpoids = 200
        self.armor = 0
        self.maxarmor = 100
        self.attaque = 20
        self.velocity = 1
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("sprites/player.png")
        self.origine_image = self.image
        self.rect = self.image.get_rect()
        self.rect.x = pygame.display.get_window_size()[0]/2
        self.rect.y = pygame.display.get_window_size()[1]/2


    def update_health_bar(self, surface):

        # dessiner la barre
        pygame.draw.rect(surface, (0, 0, 0), [self.rect.x, self.rect.centery - 35, int(self.maxhealth / 2), 5])
        if self.health > self.maxhealth / 4:
            pygame.draw.rect(surface, (111, 210, 45), [self.rect.x, self.rect.centery - 35, int(self.health / 2), 5])
        else:
            pygame.draw.rect(surface, (255, 29, 29), [self.rect.x, self.rect.centery - 35, int(self.health / 2), 5])

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            #le joueur a plus de point de vie
            self.game.game_over()

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

    def launch(self):
        self.all_projectiles.add(projectile.Projectile(self))

    def moveRight(self):
        self.rotate()
        #collision
        if not self.game.check_colision(self,self.game.all_zombies):
            self.rect.x += self.velocity

    def moveLeft(self):
        self.rotate()
        # collision
        if not self.game.check_colision(self, self.game.all_zombies):
            self.rect.x -= self.velocity

    def moveUp(self):
        self.rotate()
        # collision
        if not self.game.check_colision(self, self.game.all_zombies):
            self.rect.y -= self.velocity

    def moveDown(self):
        self.rotate()
        # collision
        if not self.game.check_colision(self, self.game.all_zombies):
            self.rect.y += self.velocity