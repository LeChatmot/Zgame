import random
import pygame
import player
import zombie

#class jeu
class Game:

    def __init__(self):

        #def si le jeu a commencé
        self.is_playing = False

        #creer le joueur
        self.all_player = pygame.sprite.Group()
        self.player = player.Player(self)
        self.all_player.add(self.player)

        #groupe monstre
        self.all_zombies = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.vague()

    def game_over(self):
        #jeu a neuf
        self.all_zombies = pygame.sprite.Group()
        self.player.health = self.player.maxhealth
        self.is_playing = False


    def update(self, screen):

        #player
        screen.blit(self.player.image, self.player.rect)

        #barre du joueur
        self.player.update_health_bar(screen)

        #projectile actuel
        for projectile in self.player.all_projectiles:
            projectile.move()

        for zombie in self.all_zombies:
            if random.randint(0,2) == 2:
                zombie.zmove()
            zombie.update_health_bar(screen)

        #projectiles
        self.player.all_projectiles.draw(screen)

        #zombies
        self.all_zombies.draw(screen)

        #Nord-Est
        if self.pressed.get(pygame.K_RIGHT) and self.pressed.get(pygame.K_UP) and self.player.rect.x < screen.get_width()-50 and self.player.rect.y > 0:
            self.player.moveRight()
            self.player.moveUp()
            self.player.sens = 3
        #Sud-Est
        elif self.pressed.get(pygame.K_RIGHT) and self.pressed.get(pygame.K_DOWN) and self.player.rect.x < screen.get_width()-50 and self.player.rect.y < screen.get_height()-50:
            self.player.moveRight()
            self.player.moveDown()
            self.player.sens = 5
        #Nord-Ouest
        elif self.pressed.get(pygame.K_LEFT) and self.pressed.get(pygame.K_UP) and self.player.rect.x > 0 and self.player.rect.y > 0:
            self.player.moveLeft()
            self.player.moveUp()
            self.player.sens = 1
        #Sud-Ouest
        elif self.pressed.get(pygame.K_LEFT) and self.pressed.get(pygame.K_DOWN) and self.player.rect.x > 0 and self.player.rect.y < screen.get_height()-50:
            self.player.moveLeft()
            self.player.moveDown()
            self.player.sens = 7
        #Est
        elif self.pressed.get(pygame.K_RIGHT) and self.player.rect.x < screen.get_width()-50 :
            self.player.moveRight()
            self.player.sens = 4
        #Ouest
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.moveLeft()
            self.player.sens = 8
        #Nord
        elif self.pressed.get(pygame.K_UP) and self.player.rect.y > 0:
            self.player.moveUp()
            self.player.sens = 2
        #Sud
        elif self.pressed.get(pygame.K_DOWN) and self.player.rect.y < screen.get_height()-50:
            self.player.moveDown()
            self.player.sens = 6

    def check_colision(self, sprite, sprite_group):
        return pygame.sprite.spritecollide(sprite, sprite_group, False, pygame.sprite.collide_mask)

    def spawn_zombies(self):
        zombie_ = zombie.Zombie(self)
        self.all_zombies.add(zombie_)

    def vague(self):
        for i in range(random.randint(3,10)):
            self.spawn_zombies()