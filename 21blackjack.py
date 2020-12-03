# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 16:21:31 2020

@author: Linter
"""
import random
from art import logo

def message(player_cards, player_score, com_cards, com_score):
    print(f"\nyour card :{player_cards},your score: {player_score}")
    if len(com_cards) > 2:
        print(f"computer's card: {com_cards}, com score: {com_score}")
    else:
        print(f"computer's card: {com_cards[0]}")


def cal_score(name_cards):
    name_score = sum(name_cards)
    if name_score > 21 and 11 in name_cards:
        name_cards[name_cards.index(11)] = 1
        name_score = sum(name_cards)
    return  name_score


def get_card(name_cards, name_score):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    name_cards.append(random.choice(cards))
    name_score = cal_score(name_cards)
    return name_cards ,name_score

print(logo)

player = []
com = []
player_score = 0
com_score = 0

for car in range(2):
    player, player_score = get_card(player, player_score)
    com, com_score = get_card(com, com_score)

message(player, player_score, com, com_score)

start_game = True
while start_game:
    get_new_card = input("Type 'y' to get another card, type 'n' to pass: " ).lower()
    if get_new_card == 'y':
       player, player_score = get_card(player, player_score)
       message(player, player_score, com, com_score)
       if player_score > 21:
           print("you over 21, player is lose")
           start_game = False
    elif get_new_card == 'n':
       start_game = False

       
while com_score < 17 and player_score < 22:
   com, com_score = get_card(com, com_score)
   if com_score > 21:
       message(player, player_score, com, com_score)
       print("computer over 21, player is win")
       
           
if player_score < 22 and com_score < 22:
    print(f"\nyour card :{player},your score: {player_score}")
    print(f"computer's card: {com}, com score: {com_score}")
    if  player_score > com_score:
        print("player is win")
    elif player_score < com_score:
        print("player is lose")
    else:
        print("it is draw")
    


