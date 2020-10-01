"""
Project:    War the 2 player Car Game
Date:       9/30/2020
Author:     Colin B. Chin Choy
"""

from random import shuffle
import platform
import os
import random
import keyboard

cardDeck = []
HELP =""
PLAYER_NAME = ""
BOT_NAME = ""
PLAYER_HAND=[]
BOT_HAND=[]
IN_PLAY_CARDS=[]
GAME_OVER = False
BOT_CHOICES = ["Hannah","Sam","John","Louie","Dalton","Henry","Rachael","Sally","Jasmine","Dexter"]
suits = ["H","D","S","C"]
faceCards = ["A","K","Q","J"]
cardQty = 52

class Player():
    def __init__(self,name,hand=[]):
        self.name = name
        self.hand = hand

    def oneCard(self):
        # print(self.hand)
        card = self.hand.pop(0)
        # print(card)
        return card

    def Win(self):
        for i in range(len(IN_PLAY_CARDS)):
            self.hand.append(IN_PLAY_CARDS.pop())

def loadScreen():
    VERSION = platform.python_version()
    VERS = list(VERSION)
    os.system("color 3")
    # print(VERS)
    print("                            __      __  _____ __________")
    print("                           /  \    /  \/  _  \ ______   \ ")
    print("                           \   \/\/   /  /_\  \|       _/  ")
    print("                            \        /    |    \    |   \  ")
    print("                            \__/\  /\_____|__  /____|_  /   ")
    print("                                  \/         \/       \/  ")
    print("   __  .__             _________                  .___   ________    ")
    print(" _/  |_|  |__   ____   \_   ___ \_____ _______  __| _/  /  _____/_____    _____   ____ ")
    print(" \   __\  |  \_/ __ \  /    \  \/\__  \ _  __ \ / __|  /   \  ___\__  \  /     \_/ __ \  ")
    print("  |  | |   Y  \  ___/  \     \____/ __ \|  | \/ /_/ |  \    \_\  \/ __ \|  Y Y  \  ___/  ")
    print("  |__| |___|  /\__  >   \______  (____  /___|  \____|   \______  (____  /__|_|  /\___ > ")
    print("            \/    \/          \/     \/           \/          \/     \/      \/     \/  ")
def initHelp():
    global HELP
    with open("help.txt") as f:
        HELP = f.readlines()
def printHelp():
    for i in range(len(HELP)):
        print(HELP[i])
    print("\n")
    # delay = input("Please press enter to continue")
    return
def acquirePlayers():
    global PLAYER_NAME
    global BOT_NAME
    PLAYER_NAME = input("Please enter your name for this game: ")
    BOT_NAME = random.choice(BOT_CHOICES)
def checkWinSuit(player_card,bot_card):
    global IN_PLAY_CARDS
    global PLAYER_HAND
    global BOT_HAND
    print(player_card)
    print(bot_card)
    if player_card == "H":
        print("first check")
        PLAYER1.Win()
        print(PLAYER1.name+" wins this round")
        print(len(PLAYER1.hand))
        delay = input("Please press enter to continue......(or 'h'+'enter' for help or 'q'+enter to Quit)")
        # return
    elif bot_card == "C":
        print("second check")
        PLAYER1.Win()
        print(PLAYER1.name+" wins this round")
        print(len(PLAYER1.hand))
        delay = input("Please press enter to continue......(or 'h'+'enter' for help or 'q'+enter to Quit)")
        # return
    elif player_card == "S" :
        print("third check")
        BOTPLAYER.Win()
        print(BOTPLAYER.name+" wins this round")
        print(len(BOTPLAYER.hand))
        delay = input("Please press enter to continue......(or 'h'+'enter' for help or 'q'+enter to Quit)")
        # return
    elif bot_card == "H" :
        print("fourth check")
        BOTPLAYER.Win()
        print(BOTPLAYER.name+" wins this round")
        print(len(BOTPLAYER.hand))
        delay = input("Please press enter to continue......(or 'h'+'enter' for help or 'q'+enter to Quit)")
    else:
        print("Fifth check")
        PLAYER1.Win()
        print(PLAYER1.name+" wins this round")
        print(len(PLAYER1.hand))
        delay = input("Please press enter to continue......(or 'h'+'enter' for help or 'q'+enter to Quit)")
        # return
    # print()
def createDeck():
    global cardDeck
    for s in range(len(suits)) :
        for i in range(2,11):
            card = []
            card.append(i)
            card.append(suits[s])
            cardDeck.append(card)
            # cardDeck.append(suits[s])
        for r in range(len(faceCards))  :
            card = []
            card.append(faceCards[r])
            card.append(suits[s])
            cardDeck.append(card)
            # cardDeck.append(suits[s])
    part_one = []
    part_two = []
    print("Deck Created")
    shuffle(cardDeck)
    print("Deck shuffled")
    for i in range(int(len(cardDeck)/2)) :
        part_one.append(cardDeck.pop())
    for n in range(len(cardDeck)):
        part_two.append(cardDeck.pop())
    for i in range(len(part_one)):
        cardDeck.append(part_one.pop())
        cardDeck.append(part_two.pop())
    print("Deck Riffled")
    for i in range(int(len(cardDeck)/2)) :
        part_one.append(cardDeck.pop())
    for n in range(len(cardDeck)):
        part_two.append(cardDeck.pop())
    for i in range(len(part_one)):
        cardDeck.append(part_two.pop())
    for n in range(len(part_one)):
        cardDeck.append(part_one.pop())
    print("Deck Cut")
def createHands():
    global PLAYER_HAND
    global BOT_HAND
    global cardDeck
    for i in range(int(len(cardDeck)/2)):
        PLAYER_HAND.append(cardDeck.pop())
        BOT_HAND.append(cardDeck.pop())
def cardValidation(card):
    a = card
    if str(a) == "A" :
        card = 14
        return card
    elif str(a) == "K" :
        card = 13
        return card
    elif str(a) == "Q" :
        card = 12
        return card
    elif str(a) == "J" :
        card = 11
        return card
    else:
        card = int(card)
        return card

loadScreen()
initHelp()
printHelp()
acquirePlayers()
createDeck()
createHands()
PLAYER1 = Player(PLAYER_NAME,PLAYER_HAND)
BOTPLAYER = Player(BOT_NAME,BOT_HAND)

while GAME_OVER != True :
    try:
        if keyboard.is_pressed('h'):
            printHelp()
            delay = input("Please press enter to continue......(or 'h'+'enter' for help or 'q'+enter to Quit)")
            continue
    except:
        continue
    try:
        if keyboard.is_pressed('q'):
            if len(PLAYER1.hand) > len(BOTPLAYER.hand):
                GAME_OVER = True
                print(PLAYER1.name+" wins the Game")
                break
            else:
                GAME_OVER = True
                print(BOTPLAYER.name+" wins the Game")
                break
    except:
        continue
    if len(PLAYER1.hand) == 0:
        GAME_OVER = True
        print(BOTPLAYER.name+" wins the Game")
        break
    elif len(BOTPLAYER.hand) == 0:
        GAME_OVER = True
        print(PLAYER1.name+" wins the Game")
        break
    else:
        IN_PLAY_CARDS.append(PLAYER1.oneCard())
        IN_PLAY_CARDS.append(BOTPLAYER.oneCard())
        card1 = cardValidation(IN_PLAY_CARDS[0][0])
        card2 = cardValidation(IN_PLAY_CARDS[1][0])
        card1_suit = IN_PLAY_CARDS[0][1]
        card2_suit = IN_PLAY_CARDS[1][1]
        print(card1,card1_suit)
        print(card2,card2_suit)
        if card1 == card2:
            checkWinSuit(card1_suit,card2_suit)
            continue
        elif card1 > card2:
            PLAYER1.Win()
            print(PLAYER1.name+" wins this round")
            print(len(PLAYER1.hand))
            delay = input("Please press enter to continue......(or 'h'+'enter' for help or 'q'+enter to Quit)")
        else:
            BOTPLAYER.Win()
            print(BOTPLAYER.name+" wins this round")
            print(len(BOTPLAYER.hand))
            delay = input("Please press enter to continue......(or 'h'+'enter' for help or 'q'+enter to Quit)")
