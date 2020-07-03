# Original Code by Learning-Still 3/7/2020
import functions
from hand import Hand
import graphics
import pygame
from pygame.locals import *
import sys
import time

rules = ""
# Start Game
graphics.window()
# Ask if they want to see rules
graphics.displayText("*** BLACKJACK  ***", 400, 0)

graphics.displayText("Do you want to see the rules? (Y/N)", 5, 20)
pygame.display.update()

#uses Y or N keys to determine if the rules need to be displayed
while rules != "Y" and rules != "N":
    for event in pygame.event.get():
        if event.type == KEYUP:
            if event.key == K_y:
                rules = "Y"
            elif event.key == K_n:
                rules ="N"

#if y is pressed rules displayed. New graphics window set up blank screen and timer keeps it open
if rules == "Y":
    graphics.window()
    graphics.displayText(" Both you and the computer are dealt 2 cards. ", 5,5)
    graphics.displayText("However, you can only see one of the computer's cards.",5, 25)
    graphics.displayText("All cards are face value except:", 5, 45)
    graphics.displayText("Jack (J), Queen (Q) and King (K) are all worth 10.", 10, 65)
    graphics.displayText("Ace (A) can be worth 11 or 1.", 10, 85)
    graphics.displayText("The aim of the game is to get closer to 21 points than the computer without going over (busting).", 5, 105)
    graphics.displayText("You can twist ( press t) to get another card (so you have three) or stick ( press s) to stay with the cards you have", 5, 125)
    graphics.displayText("You go first.", 5, 145)
    graphics.displayText("Have fun and good luck!", 5, 165)

    pygame.display.update()
    time.sleep(15)

# game loop - will run into red x clicked
while True:

    # Uses Hand class to make a hand for the player and a hand for the computer.
    playerHand = Hand("player")
    compHand = Hand("comp")

    # card positions
    playerXpos = 5
    PLAYER_Y_POS = 200
    compXpos = 5
    COMP_Y_POS = 25
    PLAYER_TOTAL_Y = 185
    COMP_TOTAL_Y = 13
    # reset window
    graphics.window()

    # indicate where each players hand is
    graphics.displayText("Player:", 5, PLAYER_Y_POS - 15)
    graphics.displayText("Computer:", 5, COMP_Y_POS - 15)
    # picks two cards for each hand
    for card in range(2):
        playerXpos = functions.deal_Card(playerHand, playerXpos, PLAYER_Y_POS)
        compXpos = functions.deal_Card(compHand, compXpos, COMP_Y_POS)
    # only one of the comps cards can be shown- rect covers it up
    graphics.coverUp(compXpos, COMP_Y_POS)


    #gets and displays the total of each hand
    compTotal =str(functions.get_total(compHand))
    playerTotal =str(functions.get_total(playerHand))

    graphics.displayText(playerTotal, playerXpos, PLAYER_TOTAL_Y)

    pygame.display.update()

    #Players turn is first
    turn = "player"
    playerMove = ""


            #Player picks move. if t pressed, new card added until either total is over 21 or s is  pressed
    while playerMove != "stick" and (int(playerTotal) <= 21 and int(compTotal) <= 21):
        if turn == playerHand.get_user():
            for event in pygame.event.get():
                if event.type == KEYUP:
                    if event.key == K_t:
                        playerMove = "twist"
                    elif event.key == K_s:
                        playerMove = "stick"



            if playerMove == "twist":
                playerXpos = functions.deal_Card(playerHand, playerXpos, PLAYER_Y_POS)
                playerTotal = functions.get_total(playerHand)

                # Check for ace - change to 1 if bust
                functions.ace_swap(playerHand, playerTotal)

                #Displays new total
                playerTotal = str(functions.get_total(playerHand))
                graphics.displayText(playerTotal, playerXpos, PLAYER_TOTAL_Y)
                pygame.display.update()
                time.sleep(1.5)

            elif playerMove == "stick":
                turn = "comp"


        if turn == compHand.get_user():
            #Redraws second card
            graphics.draw_card(compXpos-72, COMP_Y_POS, compHand.get_card_faces()[1])
            #comp move
            compXpos = functions.comp_move(compHand, compXpos, COMP_Y_POS)
            #Displays comps new total
            compTotal =str(functions.get_total(compHand))
            graphics.displayText(compTotal, compXpos, COMP_TOTAL_Y)
            pygame.display.update()
            time.sleep(3)



    #Determine if anyone busts, and who wins.
    graphics.window()
    # last total were strings - int needed for calculations
    playerTotal = int(playerTotal)
    compTotal = int(compTotal)

    if playerTotal > 21:
        graphics.displayText("You bust! You lost.", 200, 200)

    elif compTotal > 21:
        graphics.displayText("Comp bust! You won!", 200, 200)

    elif playerTotal == compTotal:
        graphics.displayText("You both have the same scores. It's a tie!", 200, 200)

    elif playerTotal > compTotal:
        graphics.displayText("You are closer to 21 then the computer. You won!", 200, 200)

    else:
        graphics.displayText("The computer was closer to 21. You lost.", 200, 200)

    pygame.display.update()
    time.sleep(3)

    #exit sequence
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()






