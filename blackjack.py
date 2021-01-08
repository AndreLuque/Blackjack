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
LIGHT_RED = (230, 0, 0)

class Player ():
    def __init__(self, money, card1, card2, card, bet, totalCards, ace):
        self.money = money
        self.card1 = card1
        self.card2 = card2
        self.card = card
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
                    player.ace = False    
            elif player.card1[0] == 'A':
                player.ace = True
                if player.totalCards + 11 <= 21:
                    player.totalCards += 11
                else:
                    player.totalCards += 1
                    player.ace = False
            elif player.card1[0] == '1' and player.card1[1] == '0':
                if player.totalCards + 10 <= 21:
                    player.totalCards += 10
                else:
                    player.ace = False             
            else:
                if player.totalCards + int(player.card1[0]) <= 21:
                   player.totalCards += int(player.card1[0]) 
                else:
                    player.totalCards += int(player.card1[0]) - 10 
                    player.ace = False  
        else:
            if player.card1[0] == 'J' or player.card1[0] == 'Q' or player.card1[0] == 'K':
                player.totalCards += 10 
            elif player.card1[0] == 'A':
                if player.totalCards + 11 <= 21:
                    player.totalCards += 11
                    player.ace = True
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
                    player.ace = False 
            elif player.card2[0] == 'A':
                player.ace = True
                if player.totalCards + 11 <= 21:
                    player.totalCards += 11
                else:
                    player.totalCards += 1
                    player.ace = False   
            elif player.card2[0] == '1' and player.card2[1] == '0':
                if player.totalCards + 10 <= 21:
                    player.totalCards += 10
                else:
                    player.ace = False               
            else:
                if player.totalCards + int(player.card2[0]) <= 21:
                   player.totalCards += int(player.card2[0]) 
                else:
                    player.totalCards += int(player.card2[0]) - 10  
                    player.ace = False 
        else:
            if player.card2[0] == 'J' or player.card2[0] == 'Q' or player.card2[0] == 'K':
                player.totalCards += 10 
            elif player.card2[0] == 'A':
                if player.totalCards + 11 <= 21:
                    player.totalCards += 11
                    player.ace = True
                else:
                    player.totalCards += 1
            elif player.card2[0] == '1' and player.card2[1] == '0':
                player.totalCards += 10            
            else:
                player.totalCards += int(player.card2[0])   
    else:
        if player.ace == True:
            if player.card[0] == 'J' or player.card[0] == 'Q' or player.card[0] == 'K':
                if player.totalCards + 10 <= 21:
                    player.totalCards += 10
                else:
                    player.ace = False     
            elif player.card[0] == 'A':
                player.ace = True
                if player.totalCards + 11 <= 21:
                    player.totalCards += 11
                else:
                    player.totalCards += 1
                    player.ace = False   
            elif player.card[0] == '1' and player.card[1] == '0':
                if player.totalCards + 10 <= 21:
                    player.totalCards += 10
                else:
                    player.ace = False 
            else:
                if player.totalCards + int(player.card[0]) <= 21:
                   player.totalCards += int(player.card[0]) 
                else:
                    player.totalCards += int(player.card[0]) - 10
                    player.ace = False   
        else:
            if player.card[0] == 'J' or player.card[0] == 'Q' or player.card[0] == 'K':
                player.totalCards += 10 
            elif player.card[0] == 'A':
                if player.totalCards + 11 <= 21:
                    player.totalCards += 11
                    player.ace = True
                else:
                    player.totalCards += 1
            elif player.card[0] == '1' and player.card[1] == '0':
                player.totalCards += 10            
            else:
                player.totalCards += int(player.card[0])                              

def playSound(sound:str) -> None:
    #Reproduce el sonido elegido
    play = pygame.mixer.Sound(sound)
    play.play()

def main():  
    pygame.init()


    
    #Establecemos la pantalla, sus dimensiones y su nombre
    dimensions = [1000, 600]
    screen = pygame.display.set_mode(dimensions) 
    pygame.display.set_caption('BLACKJACK')
    #Inicializamos el booleano para salir del todo del juego
    exit = False
    #Inicializamos el booleano para salir de una pantalla
    done = False
    #Iniciamos el juego
    #Todas las cartas con la que se pueden jugar
    listCards = ['2C', '2D', '2H', '2S', '3C', '3D', '3H', '3S', '4C', '4D', '4H', '4S', '5C', '5D', '5H', '5S', '6C', '6D',
                 '6H', '6S', '7C', '7D', '7H', '7S', '8C', '8D', '8H', '8S', '9C', '9D', '9H', '9S', '10C', '10D', '10H', '10S',
                 'JC', 'JD', 'JH', 'JS','QC', 'QD', 'QH', 'QS','KC', 'KD', 'KH', 'KS','AC', 'AD', 'AH', 'AS']      
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
    
    #Inicializamos el booleano playAgain para ver si el usuario quiere volver a jugar
    playAgain = True
    while playAgain and not exit:
        #Creamos al juagdor y el crupier
        player = Player(1000, '', '', '', 50, 0, False)
        crupier = Player(0, '', '', '', 0, 0, False)
        while not exit and player.money >= 50:
            #inicializamos el booleano done hasta que salga de la pantalla de introduccion
            done = False
            #Aqui almacenamos las cartas que ya estan en juego y por lo tanto no se pueden repetir
            listUsedCards = []       
            #Almacenamos las nuevas cartas del jugador y del crupier que vamos a introducir en el juego
            listNewCardsP = []
            listNewCardsC = []
            #Ponemos la posicion inicial del menu de apuestas y de la apuesta
            betMenu_y = 300
            bet_x = 300
            #Posicion incial de las cartas
            cardp1_x = 1100
            cardp2_x = 1100
            cardc1_x = 1100
            cardc2_x = 1100
            #Posicion inicial de cada carta nueva que introducimos del crupier y del jugador
            cardp_x = 1100
            cardc_x = 1100
            #Posicion inicial de cada una de las nuevas cartas
            newCard_x  = 330
            newCard_y = 380
            #Para poner la carta en una altura mas baja
            change_y = 0
            #Inicializamos el booleano para ver si la apuesta es definitiva
            deal = False
            #Booleano para ver si el usuario quiere otra carta
            hit = False
            #Booleano para ver si el usuario se quiere quedar
            stand = False
            #Inicializamos para que cuente los puntos de cada carta una vez
            count = 0
            #Con la apuesta inicial reducimos el dinero del juagdor
            player.money += -50
            #Reniciamos los valores de los juagdores
            player.card1 = ''
            player.card2 = ''
            player.card = ''
            player.totalCards = 0
            player.bet = 50
            player.ace = False
            crupier.card1 = ''
            crupier.card2 = ''
            crupier.card = ''
            crupier.totalCards = 0
            crupier.ace = False
            #the initial bet
            initialBet = 50
            #Generamos colores aleatorios para nuestras fichas
            listColors = []
            for i in range(6):
                listColors += [(random.randrange(256), random.randrange(256), random.randrange(256))]
            #We start the clock
            clock = pygame.time.Clock()

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
                            elif 200 <= pos[0] <= 330 and 230 <= pos[1] <= 300 and count == 3:
                                hit = True
                            elif 700 <= pos[0] <= 830 and 230 <= pos[1] <= 300 and count == 3:
                                stand = True
                            #Si coincide con la posicion de una de las fichas aumentamos la apuesta
                            elif ((pos[0] - 75) ** 2 + (pos[1] - 397) ** 2) <= 2500 and not deal:
                                if player.money >= 5:
                                    player.bet += 5
                                    player.money += -5
                                    initialBet += 5
                            elif ((pos[0] - 220) ** 2 + (pos[1] - 397) ** 2) <= 2500 and not deal:
                               if player.money >= 10:
                                   player.bet += 10
                                   player.money += -10
                                   initialBet += 10
                            elif ((pos[0] - 361) ** 2 + (pos[1] - 397) ** 2) <= 2500 and not deal:
                               if player.money >= 25:
                                   player.bet += 25
                                   player.money += -25
                                   initialBet += 25
                            elif ((pos[0] - 80) ** 2 + (pos[1] - 517) ** 2) <= 2500 and not deal:
                               if player.money >= 50:
                                   player.bet += 50
                                   player.money += -50
                                   initialBet += 50
                            elif ((pos[0] - 220) ** 2 + (pos[1] - 517) ** 2) <= 2500 and not deal:
                               if player.money >= 100:
                                   player.bet += 100
                                   initialBet += 100
                                   player.money += -100
                            elif ((pos[0] - 361) ** 2 + (pos[1] - 517) ** 2) <= 2500 and not deal:
                               if player.money >= 250:
                                   player.bet += 250
                                   player.money += -250
                                   initialBet += 250                               
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
                screen.blit(text, [bet_x - 30, 215])
                text = font.render('$', True, LIGHT_GREEN)
                screen.blit(text, [bet_x - 70, 215])
                #Ponemos las fichas
                for i in range(6):
                    if i < 3:
                        pygame.draw.circle(screen, listColors[i], (80 + (i * 140), betMenu_y + 100), 50)
                        pygame.draw.circle(screen, WHITE, (80 + (i * 140), betMenu_y + 100), 50, 3)
                    else:
                        pygame.draw.circle(screen, listColors[i], (80 + ((i - 3) * 140), betMenu_y + 220), 50)
                        pygame.draw.circle(screen, WHITE, (80 + ((i - 3) * 140), betMenu_y + 220), 50, 3)
                font = pygame.font.Font('Anton.ttf', 50)
                text = font.render('5', True, WHITE)
                screen.blit(text, [67, betMenu_y + 63])     
                text = font.render('10', True, WHITE)
                screen.blit(text, [198, betMenu_y + 63]) 
                text = font.render('25', True, WHITE)
                screen.blit(text, [335, betMenu_y + 63]) 
                text = font.render('50', True, WHITE)
                screen.blit(text, [55, betMenu_y + 183]) 
                text = font.render('100', True, WHITE)
                screen.blit(text, [187, betMenu_y + 183]) 
                text = font.render('250', True, WHITE)
                screen.blit(text, [323, betMenu_y + 183])        
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
                            cardp1_x += -40
                            if 1100 > cardp1_x >= 1060:
                                playSound('carddeal.ogg')
                        else: 
                            cardp1_x = 430
                            if count == 0:
                                pointsCard(player, 1)
                                count += 1
                            if cardc1_x > 430:
                                cardc1_x += -40
                                if 1100 > cardc1_x >= 1060:
                                    playSound('carddeal.ogg')
                            else: 
                                cardc1_x = 430   
                                if cardp2_x > 480:
                                    cardp2_x += -40
                                    if 1100 > cardp2_x >= 1060:
                                        playSound('carddeal.ogg')
                                else: 
                                    cardp2_x = 480 
                                    if count == 1:
                                        pointsCard(player, 2) 
                                        count += 1 
                                    if cardc2_x > 480:
                                        cardc2_x += -40
                                        if 1100 > cardc2_x >= 1060:
                                            playSound('carddeal.ogg')
                                    else: 
                                        cardc2_x = 480 
                                        if count == 2:
                                            pointsCard(crupier, 2)
                                            count += 1   
                        #Creamos los botones de hit y stand para determinar si el usuario quiere mas cartas o no                    
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

                        if hit and cardp_x == 1100 and not stand:
                            #Get a random card that has not been used
                            r1 = random.randrange(0, 52)
                            while r1 in listUsedCards:
                                r1 = random.randrange(0, 52)
                            listUsedCards += [r1] 
                            #Start the movement of the card
                            cardp_x += -40       
                        hit = False 

                        #Update and draw the position of the card that is currently in motion 
                        if 530 < cardp_x < 1100:
                            cardp_x += -40
                            #Load the card into the game
                            card = pygame.image.load(listCards[r1] + '.jpg').convert()   
                            card = pygame.transform.scale(card, (106, 157)) 
                            screen.blit(card, [cardp_x, 330])
                        elif cardp_x <= 530:
                            cardp_x = 1100
                            #Add to the cards that we need to load 
                            listNewCardsP += [r1]
                            #Update the amount of points
                            player.card = listCards[r1]
                            pointsCard(player, 3)

                        #showing all the new cards for the player in the game    
                        for i in range(len(listNewCardsP)):
                            #Load the card into the game
                            card = pygame.image.load(listCards[listNewCardsP[i]] + '.jpg').convert()   
                            card = pygame.transform.scale(card, (106, 157)) 
                            if i % 2 == 0:  
                                newCard_x = 430
                            else:
                                newCard_x = 480    
                            change_y = 50 * (i // 2)
                            screen.blit(card, [newCard_x, 380 + change_y])

                        if player.totalCards > 21:
                            if count == 5:    
                                done = True
                                time.sleep(3)
                            if player.bet == 0:
                                count += 1
                            if count >= 4:
                                #flip the crup`s other card around 
                                card = pygame.image.load(crupier.card1 + '.jpg').convert()  
                                card = pygame.transform.scale(card, (106, 157))   
                                screen.blit(card, [cardc1_x, 50])
                                pygame.draw.rect(screen, LIGHT_RED, (0, 0, 330, 100))
                                font = pygame.font.Font('Anton.ttf', 70)
                                text = font.render('BUST!', True, WHITE)
                                screen.blit(text, [80, -5]) 
                            #Adding the points of the flipped card
                            if count == 3:
                                pointsCard(crupier, 1)
                                count += 1
                            #Bring the players money to zero    
                            if player.bet > 0:
                                player.bet += -5
                            elif player.bet <= 0 and initialBet != 0:
                                initialBet = 0
                            if player.bet < 0 and initialBet != 0:
                                player.bet = 0

                        else:
                            if stand:
                                #flip the crup`s other card around 
                                card = pygame.image.load(crupier.card1 + '.jpg').convert()  
                                card = pygame.transform.scale(card, (106, 157))   
                                screen.blit(card, [cardc1_x, 50])
                                #Adding the points of the flipped card
                                if count == 3:
                                    pointsCard(crupier, 1)
                                    count += 1
                                card = pygame.image.load(crupier.card2 + '.jpg').convert()  
                                card = pygame.transform.scale(card, (106, 157))   
                                screen.blit(card, [cardc2_x, 50])   
                                if cardc_x == 1100 and crupier.totalCards < 17:
                                    #Get a random card that has not been used
                                    r2 = random.randrange(0, 52)
                                    while r2 in listUsedCards:
                                        r2 = random.randrange(0, 52)
                                    listUsedCards += [r2]
                                    #Start the movement of the card
                                    cardc_x += -40
                            #Keep displaying and getting new cards until 21 or above
                            if crupier.totalCards < 17:
                                if 530 < cardc_x < 1100: 
                                    card = pygame.image.load(listCards[r2] + '.jpg').convert()   
                                    card = pygame.transform.scale(card, (106, 157)) 
                                    screen.blit(card, [cardc_x, 50])
                                    cardc_x += -40
                                elif cardc_x <= 530:
                                    cardc_x = 1100
                                    #Add to the cards that we need to load 
                                    listNewCardsC += [r2]
                                    #Update the amount of points
                                    crupier.card = listCards[r2]
                                    pointsCard(crupier, 3)   

                            #showing all the new cards for the crup in the game    
                            for i in range(len(listNewCardsC)):
                                #Load the card into the game
                                card = pygame.image.load(listCards[listNewCardsC[i]] + '.jpg').convert()   
                                card = pygame.transform.scale(card, (106, 157)) 
                                if i % 2 == 0:
                                    newCard_x = 430
                                else:
                                    newCard_x = 480    
                                change_y = -50 * (i // 2)
                                screen.blit(card, [newCard_x, 0 + change_y])    
                            #Once the crup is donde getting new cards we compare them to see who won    
                            if crupier.totalCards >= 17:
                                #Once we know who won , we want it to show visuallly by gradually increasing or decreasing the money in the middle of
                                #the screen and then adding it to the players bank
                                if crupier.totalCards > 21:
                                    if player.bet < initialBet * 2:
                                        player.bet += 5   
                                    elif player.bet >= initialBet * 2 and initialBet != 0:
                                        player.money += player.bet
                                        initialBet = 0
                                    if player.bet > initialBet * 2 and initialBet != 0:
                                        player.bet = initialBet * 2   
                                    #Show message                            
                                    pygame.draw.rect(screen, LIGHT_GREEN, (0, 0, 300, 100))
                                    text = font.render('PLAYER WINS!', True, WHITE)
                                    screen.blit(text, [30, 10])      
                                elif crupier.totalCards > player.totalCards:
                                    if player.bet > 0:
                                        player.bet += -5
                                    elif player.bet <= 0 and initialBet != 0:
                                        initialBet = 0
                                    if player.bet < 0 and initialBet != 0:
                                        player.bet = 0  
                                    #Show message    
                                    pygame.draw.rect(screen, LIGHT_RED, (0, 0, 300, 100))
                                    text = font.render('DEALER WINS!', True, WHITE)
                                    screen.blit(text, [30, 10])      
                                elif crupier.totalCards < player.totalCards:
                                    if player.bet < initialBet * 2:
                                        player.bet += 5
                                    elif player.bet >= initialBet * 2 and initialBet != 0:
                                        player.money += player.bet
                                        initialBet = 0
                                    if player.bet > initialBet * 2 and initialBet != 0:
                                        player.bet = initialBet * 2   
                                    #Show message    
                                    pygame.draw.rect(screen, LIGHT_GREEN, (0, 0, 300, 100))
                                    text = font.render('PLAYER WINS!', True, WHITE)
                                    screen.blit(text, [30, 10])      
                                elif player.totalCards == crupier.totalCards:
                                    if initialBet != 0:
                                        player.money += player.bet
                                        initialBet = 0
                                    #Show message    
                                    pygame.draw.rect(screen, LIGHT_BLUE, (0, 0, 300, 100))
                                    text = font.render('TIE!', True, WHITE)
                                    screen.blit(text, [100, 10])    
                                #After the money has reached the desired value we set a variable to 0 and have a counter so that the player has time to visualize
                                #what happened    
                                if initialBet == 0:
                                    count += 1
                                    if count == 30:
                                        done = True
                #Until the users clicks the deal button We will keep showing it                         
                if not deal:
                    buttonColor = DARK_GRAY
                    if  45 <= pos[0] <= 225 and 235 <= pos[1] <= 290: 
                        buttonColor = DARKER_GRAY
                    pygame.draw.rect(screen, buttonColor, (45, 235, 180, 55)) 
                    font = pygame.font.Font('Anton.ttf', 40)
                    text = font.render('DEAL', True, WHITE)
                    screen.blit(text, [100, 230])
                #Refresh the screen    
                pygame.display.flip()
            #Frames per second    
            clock.tick(60)

        #We change it to false and the user must press the button to play again    
        playAgain = False
        #We initialize done back to false
        done = False
        #Pantalla de final de juego y boton para jugar de nuevo
        while not exit and not done:     
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
                        playAgain = True
            #Ponemos la pantalla en blanco              
            screen.fill(WHITE)
            #Cargamos el fondo de pantalla y lo plasmamos
            background = pygame.image.load("background.jpg").convert()
            screen.blit(background, [0, 0])
            font = pygame.font.Font('CasinoShadow-italic.ttf', 120)
            #Draw the rectangle where the game over message will be
            pygame.draw.rect(screen, DARK_GRAY, (150, 150, 680, 150))
            #Escribimos el titulo de blackjack
            text = font.render("Game Over", True, WHITE)
            screen.blit(text, [200, 180])
            #Ponemos el boton para empezar el juego
            buttonColor = DARK_GRAY
            if  270 <= pos[0] <= 750 and 310 <= pos[1] <= 385: 
                buttonColor = DARKEST_GRAY
            pygame.draw.rect(screen, buttonColor, (270, 310, 480, 75))
            font = pygame.font.Font('CasinoFlat.ttf', 40)
            text = font.render("Press to Play Again", True, WHITE)
            screen.blit(text, [320, 330])
            #Refrescamos la pantalla, actualizamos la imagen 
            pygame.display.flip()
        time.sleep(1)
        #Poner la pantalla del final despues de perder el dinero        
    pygame.quit()

if __name__ == '__main__': main()