import time
import random

# Purpose: -- BlackJack game the goal is to reach 21 with out going over the player that is closest wins. --
#
# Constraints: -- Players must get to 20 but not go over if he/she is over they bust if the dealer gets closer to 21
#                dealer wins--
#
# Expected Results: -- two player game one player wins by getting 21 or the player that is closest to 21 wins. --
#
#
# Version		Author		   Date		          Description
# ---------------------------------------------------------------
# 1.0         Rick Reyes	  16 Jan. 2022	         Blackjack game.


# Intro
print('          ♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠')
print('          ♠                       ♠')
print('          ♥       BlackJack       ♥')
print('          ♦                       ♦')
print('          ♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠♣♦♥♠')
print()
time.sleep(1)
print('    ♦♠ Welcome to the game of BlackJack ♣♥')
print()
print()
time.sleep(1)

# input ask the player if they would like to play. / Intro.
play_game = input('Would you like to begin (Y/N): ')
if play_game == 'n' or play_game == 'N':
    print("Guess BlackJack isn't for you maybe next time.")
elif play_game == 'y' or play_game == 'Y':
    print()
    print('The goal of the game is to reach a total of 21.')
    time.sleep(2)
    print("It's you vs the dealer, in order to win you need to be closest to 21 or get 21 if your over you bust.\n")
    time.sleep(2)
    print("Let's Begin!")
# Game process begins.
player_card = random.randint(1, 11)
print('Your card is: ', player_card)
# Loop for 21 begins.
while player_card <= 21:
    player = input('Would you like another card? Y/N')
    if player == 'y' or player == 'Y':
        new_card = random.randint(1, 11)
        print('Your new card is', new_card)
        player_card = int(player_card) + int(new_card)
        print('You have a', player_card)
        if player_card > 21:
            print('Your over 21 you BUST! Dealer Wins!')
            break
    if player == 'n' or player == 'N':
        print('Dealers turn')
        dealer_card = random.randint(1, 11)
        while dealer_card <= 21:
            for dealer_card in range(5):
                print('Dealer is deciding...')
                time.sleep(0.05)
                deal_card = random.randint(1, 11)
                dealer_card = int(dealer_card) + int(deal_card)
        break
# Dealers processing
'''dealer_card = random.randint(1, 11)
while dealer_card <= 21:
    print('Dealer is deciding...')
    time.sleep(5)
    deal_card = random.randint(1, 11)
    dealer_card = int(dealer_card) + int(deal_card)
'''
input()  # using this input() to keep the window open.
