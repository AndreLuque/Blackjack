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
RED = (200, 0, 0)
DARKER_RED = (150, 0, 0)

class Player ():
    def __init__(self, money, card1, card2, bet, totalCards, ace):
        self.money = money
        self.card1 = card1
        self.card2 = card2
        self.bet = bet
        self.totalCards = totalCards
        self.ace = ace

def pointsCard(player:Player, numberCard:int) -> None:
    if numberCard == 1:
        if player.ace == True:
            if player.card1[0] == 'J' or player.card1[0] == 'Q' or player.card1[0] == 'K':
                if player.totalCards + 10 <= 21:
                    player.totalCards += 10
                else:
                    None    
            elif player.card1[0] == 'A':
                player.ace = True
                if player.totalCards + 11 <= 21:
                    player.totalCards += 11
                else:
                    player.totalCards += 1
            elif player.card1[0] == '1' and player.card1[1] == '0':
                if player.totalCards + 10 <= 21:
                    player.totalCards += 10
                else:
                    None             
            else:
                if player.totalCards + int(player.card1[0]) <= 21:
                   player.totalCards += int(player.card1[0]) 
                else:
                    player.totalCards += int(player.card1[0]) - 10  
        else:
            if player.card1[0] == 'J' or player.card1[0] == 'Q' or player.card1[0] == 'K':
                player.totalCards += 10 
            elif player.card1[0] == 'A':
                player.ace = True
                if player.totalCards + 11 <= 21:
                    player.totalCards += 11
                else:
                    player.totalCards += 1  
            elif player.card1[0] == '1' and player.card1[1] == '0':
                player.totalCards += 10          
            else:
                player.totalCards += int(player.card1[0])   
    elif numberCard == 2:
        if player.ace == True:
            if player.card2[0] == 'J' or player.card2[0] == 'Q' or player.card2[0] == 'K':
                if player.totalCards + 10 <= 21:
                    player.totalCards += 10
                else:
                    None    
            elif player.card2[0] == 'A':
                player.ace = True
                if player.totalCards + 11 <= 21:
                    player.totalCards += 11
                else:
                    player.totalCards += 1  
            elif player.card2[0] == '1' and player.card2[1] == '0':
                if player.totalCards + 10 <= 21:
                    player.totalCards += 10
                else:
                    None              
            else:
                if player.totalCards + int(player.card2[0]) <= 21:
                   player.totalCards += int(player.card2[0]) 
                else:
                    player.totalCards += int(player.card2[0]) - 10  
        else:
            if player.card2[0] == 'J' or player.card2[0] == 'Q' or player.card2[0] == 'K':
                player.totalCards += 10 
            elif player.card2[0] == 'A':
                player.ace = True
                if player.totalCards + 11 <= 21:
                    player.totalCards += 11
                else:
                    player.totalCards += 1
            elif player.card2[0] == '1' and player.card2[1] == '0':
                player.totalCards += 10            
            else:
                player.totalCards += int(player.card2[0])                     

def main():  
    #Inicializamos el booleano playAgain para ver si el usuario quiere volver a jugar
    playAgain = True
    #Inicializamos el booleano para salir del todo del juego
    exit = False
    #Iniciamos el juego
    #Todas las cartas con la que se pueden jugar
    listCards = ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D',
                 '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', '10C', '10D', '10H', '10S',
                 'JC', 'JD', 'JH', 'JS','QC', 'QD', 'QH', 'QS','KC', 'KD', 'KH', 'KS','AC', 'AD', 'AH', 'AS']
    #Aqui almacenamos las cartas que ya estan en juego y por lo tanto no se pueden repetir
    listUsedCards = []             
    pygame.init()
    while playAgain and not exit:
        #solo se jugará otra vez si el usuario lo decida
        playAgain = False
        #inicializamos el booleano done hasta que salga de la pantalla de introduccion
        done = False
        #Creamos al juagdor y el crupier
        player = Player(1000, '', '', 50, 0, False)
        crupier = Player(0, '', '', 0, 0, False)
        #Ponemos la posicion inicial del menu de apuestas y de la apuesta
        betMenu_y = 300
        bet_x = 300
        #Posicion incial de las cartas
        cardp1_x = 1100
        cardp2_x = 1100
        cardc1_x = 1100
        cardc2_x = 1100
        #Inicializamos el booleano para ver si la apuesta es definitiva
        deal = False
        #Inicializamos para que cuente los puntos de cada carta una vez
        count = 0
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
                        if 45 <= pos[0] <= 225 and 235 <= pos[1] <= 290:
                            deal = True
            #Cubrimos la pantalla de verde                
            screen.fill(GREEN)       

            #Creamos el menu donde se hará la apuesta
            pygame.draw.rect(screen, LIGHT_BLUE, (0, betMenu_y, 450, 30)) 
            pygame.draw.rect(screen, BLUE, (0, betMenu_y + 30, 450, 270))            
            font = pygame.font.Font('Anton.ttf', 18)
            text = font.render("BANK:", True, WHITE)
            screen.blit(text, [50, betMenu_y])
            text = font.render(str(player.money), True, WHITE)
            screen.blit(text, [100, betMenu_y])
            #Ponemos el dinero que el usuario haya puesto para apostar
            font = pygame.font.Font('Anton.ttf', 65)
            text = font.render(str(player.bet), True, WHITE)
            screen.blit(text, [bet_x, 215])
            text = font.render('$', True, LIGHT_GREEN)
            screen.blit(text, [bet_x - 40, 215])
            #Ponemos las fichas

            #Boton de all-in 

            #Boton de Deal, empezará el juego
            #Desplazamos la apuesta y el menu en caso de que el usuario pulse DEAL para empezar el juego 
            if deal:
                if betMenu_y < 570:
                    betMenu_y += 1
                elif betMenu_y >= 570:
                    betMenu_y = 570 
                if bet_x < 500:
                    bet_x += 1
                elif bet_x >= 500:
                    bet_x = 500 
                    #Ponemos el contador de las cartas
                    pygame.draw.circle(screen, LIGHTER_GRAY, (750, 400), 50)
                    font = pygame.font.Font('Anton.ttf', 50)
                    text = font.render(str(player.totalCards), True, WHITE)
                    screen.blit(text, [732, 365])
                    pygame.draw.circle(screen, LIGHTER_GRAY, (750, 100), 50)
                    font = pygame.font.Font('Anton.ttf', 50)
                    text = font.render(str(crupier.totalCards), True, WHITE)
                    screen.blit(text, [732, 65])
                    #Cogemos una 4 cartas al azar de la baraja sin que se repitan
                    if player.card1 == '':
                        r = random.randrange(0, 52)
                        while r in listUsedCards:
                            r = random.randrange(0, 52)
                        player.card1 = listCards[r]
                        listUsedCards += [r] 
                        r = random.randrange(0, 52)
                        while r in listUsedCards:
                            r = random.randrange(0, 52)
                        player.card2 = listCards[r]
                        listUsedCards += [r] 
                        r = random.randrange(0, 52)
                        while r in listUsedCards:
                            r = random.randrange(0, 52)
                        crupier.card1 = listCards[r]
                        listUsedCards += [r] 
                        r = random.randrange(0, 52)
                        while r in listUsedCards:
                            r = random.randrange(0, 52)
                        crupier.card2 = listCards[r]
                        listUsedCards += [r] 
                        print(player.card1, player.card2, crupier.card1, crupier.card2)    
                    #Cargamos las cartas a la pantalla
                    card = pygame.image.load(player.card1 + '.jpg').convert()   
                    card = pygame.transform.scale(card, (106, 157)) 
                    screen.blit(card, [cardp1_x, 330])
                    card = pygame.image.load('blue_back.jpg').convert() 
                    card = pygame.transform.scale(card, (106, 157))    
                    screen.blit(card, [cardc1_x, 50])
                    card = pygame.image.load(player.card2 + '.jpg').convert() 
                    card = pygame.transform.scale(card, (106, 157))  
                    screen.blit(card, [cardp2_x, 330]) 
                    card = pygame.image.load(crupier.card2 + '.jpg').convert()  
                    card = pygame.transform.scale(card, (106, 157))   
                    screen.blit(card, [cardc2_x, 50])
                    #Actualizamos la posicion de las cartas en secuencia y añadimos su puntuacion
                    if cardp1_x > 430:
                        cardp1_x += -20
                    else: 
                        cardp1_x = 430
                        if count == 0:
                            pointsCard(player, 1)
                            count += 1
                        if cardc1_x > 430:
                            cardc1_x += -20
                        else: 
                            cardc1_x = 430   
                            if cardp2_x > 480:
                                cardp2_x += -20
                            else: 
                                cardp2_x = 480 
                                if count == 1:
                                    pointsCard(player, 2) 
                                    count += 1 
                                if cardc2_x > 480:
                                    cardc2_x += -20
                                else: 
                                    cardc2_x = 480 
                                    if count == 2:
                                        pointsCard(crupier, 2)
                                        count += 1   
                    buttonColor = RED
                    if  200 <= pos[0] <= 330 and 230 <= pos[1] <= 300: 
                        buttonColor = DARKER_RED
                    pygame.draw.rect(screen, buttonColor, (200, 230, 130, 70)) 
                    font = pygame.font.Font('Anton.ttf', 50)
                    text = font.render('HIT', True, WHITE)
                    screen.blit(text, [235, 227])    
                    buttonColor = RED
                    if  700 <= pos[0] <= 830 and 230 <= pos[1] <= 300: 
                        buttonColor = DARKER_RED
                    pygame.draw.rect(screen, buttonColor, (700, 230, 130, 70)) 
                    font = pygame.font.Font('Anton.ttf', 46)
                    text = font.render('STAND', True, WHITE)
                    screen.blit(text, [713, 227])                

            if not deal:
                buttonColor = DARK_GRAY
                if  45 <= pos[0] <= 225 and 235 <= pos[1] <= 290: 
                    buttonColor = DARKER_GRAY
                pygame.draw.rect(screen, buttonColor, (45, 235, 180, 55)) 
                font = pygame.font.Font('Anton.ttf', 40)
                text = font.render('DEAL', True, WHITE)
                screen.blit(text, [100, 230])


            pygame.display.flip()










        clock.tick(200)    
    pygame.quit()

if __name__ == '__main__': main()