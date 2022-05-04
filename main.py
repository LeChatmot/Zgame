import pygame
import math
import game
import map
import random


pygame.init()


pygame.display.set_caption("Zgame")
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
running = True
pause = False

windowSize = pygame.display.get_window_size()

bg = pygame.image.load("sprites/herbe.png")
bg = pygame.transform.scale(bg,(windowSize[0],windowSize[1]))

#charger la banniere
banner = pygame.image.load("sprites/banner.jpg")
banner = pygame.transform.scale(banner,(banner.get_width()*2,banner.get_height()*2))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)
banner_rect.y = math.ceil(screen.get_height()/4)

#charger boutton
button = pygame.image.load("sprites/button.png")
button = pygame.transform.scale(button,(500,250))
button_rect = button.get_rect()
button_rect.x = math.ceil(screen.get_width()*0.35)
button_rect.y = math.ceil(screen.get_height()/4)+banner.get_height()+10

#curseur
cursor = pygame.image.load("sprites/cursor.png")
cursor = pygame.transform.scale(cursor,(30,30))
cursor_rect = cursor.get_rect()

game = game.Game()

sec_to_shoot = 0

pX=-10
pY=random.randint(0,windowSize[1]-10)

while running:
    if not pause:
        pygame.mouse.set_visible(False)

        #back ground
        screen.blit(bg,(0,0))


        #verifier si le jeu a commencé
        if game.is_playing:
            game.update(screen)
        else:
            screen.blit(button, button_rect)
            screen.blit(banner, banner_rect)

        screen.blit(cursor, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        pygame.display.flip()

        for event in pygame.event.get() :

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause
                else:
                    game.pressed[event.key] = True

            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                #colision bouton jouer
                if button_rect.collidepoint(event.pos):
                    #lance le jeu
                    game.start()


        if pygame.mouse.get_pressed(num_buttons=3) == (1,0,0):
            if sec_to_shoot == 100:
                sec_to_shoot = 0
                game.player.launch()
            else:
                sec_to_shoot += 1

    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = not pause

        screen.blit(bg, (0, 0))
        screen.blit(cursor, (pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]))
        pygame.display.flip()