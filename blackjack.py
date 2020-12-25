#-----------------------------------------------------------------------
# blackjack.py
# Description:
# Author: André Luiz Queiroz Costa
# Date: 21/12/2020
# Version: 1.0
#-----------------------------------------------------------------------
import random
import time
from typing import List
import pygame

BLACK = (0, 0 ,0)
WHITE = (255, 255, 255)
GREEN = (0, 120, 0)
LIGHT_GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 120)
LIGHT_BLUE = (0, 0, 200)
VIOLET = (98, 0, 255)
LIGHT_GRAY= (175,175,175)
DARK_GRAY = (150,150,150)
DARKER_GRAY = (125, 125, 125)
DARKEST_GRAY = (100, 100, 100)
LIGHTER_GRAY = (200, 200, 200)

class Player ():
    def __init__(self, money, card1, card2, bet):
        self.money = money
        self.card1 = card1
        self.card2 = card2
        self.bet = bet

def main():  
    #Inicializamos el booleano playAgain para ver si el usuario quiere volver a jugar
    playAgain = True
    #Inicializamos el booleano para salir del todo del juego
    exit = False
    #Iniciamos el juego
    pygame.init()
    while playAgain and not exit:
        #solo se jugará otra vez si el usuario lo decida
        playAgain = False
        #inicializamos el booleano done hasta que salga de la pantalla de introduccion
        done = False
        #Creamos al juagdor y el crupier
        player = Player(1000, '', '', 50)
        crupier = Player(0, '', '', 0)
        #Ponemos la posicion inicial del menu de apuestas y du desplazamiento
        betMenu_y = 300
        changeBM_y = 0
        #Inicializamos el booleano para ver si la apuesta es definitiva
        deal = False
        #Establecemos la pantalla, sus dimensiones y su nombre
        dimensions = [1000, 600]
        screen = pygame.display.set_mode(dimensions) 
        pygame.display.set_caption('BLACKJACK')
        #We start the clock
        clock = pygame.time.Clock()
        while not done and not exit:
            #Conseguimos la posicones del raton
            pygame.mouse.set_visible(1)
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():  
                if event.type == pygame.QUIT: # Si el usuario hace click sobre cerrar, saldrá del programa
                    exit = True               
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        exit = True
                elif event.type == pygame.MOUSEBUTTONDOWN and  350 <= pos[0] <= 830 and 300 <= pos[1] <= 375:
                        done = True
            #Ponemos la pantalla en blanco              
            screen.fill(WHITE)
            #Cargamos el logo de las cartas y lo plasmamos
            BJlogo = pygame.image.load("introscreen.png").convert()
            screen.blit(BJlogo, [10, 100])
            font = pygame.font.Font('CasinoShadow-italic.ttf', 130)
            #Escribimos el titulo de blackjack
            text = font.render("Blackjack", True, BLACK)
            screen.blit(text, [280, 180])
            #Ponemos el boton para empezar el juego
            buttonColor = BLACK
            if  350 <= pos[0] <= 830 and 300 <= pos[1] <= 375: 
                buttonColor = DARK_GRAY
            pygame.draw.rect(screen, buttonColor, (350, 300, 480, 75))
            font = pygame.font.Font('CasinoFlat.ttf', 40)
            text = font.render("Press to start game", True, WHITE)
            screen.blit(text, [400, 320])
            #Refrescamos la pantalla, actualizamos la imagen 
            pygame.display.flip()

        time.sleep(1)    
        done = False
        while not done and not exit:
            #Conseguimos la posicion del raton
            pygame.mouse.set_visible(1)
            pos = pygame.mouse.get_pos()
            for event in pygame.event.get():  
                if event.type == pygame.QUIT: # Si el usuario hace click sobre cerrar, saldrá del programa
                    exit = True               
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        exit = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        None  
            #Cubrimos la pantalla de verde                
            screen.fill(GREEN)
            #Creamos el menu donde se hará la apuesta
            pygame.draw.rect(screen, LIGHT_BLUE, (0, betMenu_y, 450, 30)) 
            pygame.draw.rect(screen, BLUE, (0, betMenu_y + 30, 450, 270))            
            font = pygame.font.Font('Anton.ttf', 18)
            text = font.render("BANK:", True, WHITE)
            screen.blit(text, [50, 300])
            text = font.render(str(player.money), True, WHITE)
            screen.blit(text, [100, 300])
            #Ponemos el dinero que el usuario haya puesto para apostar
            font = pygame.font.Font('Anton.ttf', 65)
            text = font.render(str(player.bet), True, WHITE)
            screen.blit(text, [300, 215])
            text = font.render('$', True, LIGHT_GREEN)
            screen.blit(text, [260, 215])
            #Ponemos las fichas

            #Boton de all-in 

            #Boton de Deal, empezará el juego
            if not deal:
                buttonColor = DARK_GRAY
                if  45 <= pos[0] <= 225 and 235 <= pos[1] <= 290: 
                    buttonColor = DARKER_GRAY
                pygame.draw.rect(screen, buttonColor, (45, 235, 180, 55)) 
                font = pygame.font.Font('Anton.ttf', 40)
                text = font.render('DEAL', True, WHITE)
                screen.blit(text, [100, 230])

                
            pygame.display.flip()










        clock.tick(100)    
    pygame.quit()

if __name__ == '__main__': main()