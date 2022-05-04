import pygame

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.velocity = 5
        self.player = player
        self.sens = player.sens
        self.image = pygame.image.load("sprites/balle.png")
        self.image = pygame.transform.scale(self.image, (5,10))
        self.origine_image = self.image
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.x = self.player.rect.centerx
        self.rect.y = self.player.rect.centery

    """
    
    angle:
    
    225   180   135
    270    X    90
    315    0    45
    
    sens:

    1   2   3
    8   X   4
    7   6   5

    """

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


    def remove_p(self):
        self.player.all_projectiles.remove(self)

    def move_Nord(self):
        self.rect.y -= self.velocity

    def move_Sud(self):
        self.rect.y += self.velocity

    def move_Ouest(self):
        self.rect.x -= self.velocity

    def move_Est(self):
        self.rect.x += self.velocity

    def move(self):
        if self.sens == 1:
            self.rotate()
            self.move_Nord()
            self.move_Ouest()
        elif self.sens == 2:
            self.rotate()
            self.move_Nord()
        elif self.sens == 3:
            self.rotate()
            self.move_Nord()
            self.move_Est()
        elif self.sens == 4:
            self.rotate()
            self.move_Est()
        elif self.sens == 5:
            self.rotate()
            self.move_Sud()
            self.move_Est()
        elif self.sens == 6:
            self.rotate()
            self.move_Sud()
        elif self.sens == 7:
            self.rotate()
            self.move_Sud()
            self.move_Ouest()
        elif self.sens == 8:
            self.rotate()
            self.move_Ouest()

        #colision monstre
        for monster in self.player.game.check_colision(self, self.player.game.all_zombies):
            #supprimer le projectile
            self.remove_p()
            #infliger des degat
            monster.damage(self.player.attaque)

        #destruction
        if self.rect.x > 1920 or self.rect.y > 1080 or self.rect.x < 0 or self.rect.y < 0:
            self.remove_p()
