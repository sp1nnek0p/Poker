from poker import Poker
from cards import cards
import time
import os

if __name__ == "__main__":
    poker = Poker()
    while True:
        # Gets the a new hand from the Poker class using the 52 card deck imported from cards
        hand = poker.deal_cards(cards)
        # Sanitize the hand to contain A, J, Q, K
        card_suits = poker.replace_to_suits(hand)
        # Clear the console output
        os.system('cls')
        print("Shuffling . . . Shuffling . . . Shuffling . . .")
        time.sleep(.5)
        hand_string = ' '.join(card_suits) 
        print('Your Hand:', hand_string)
        print('You have:', poker.calculate_hand(hand))
        # Ask the user if he would like to draw another hand or quit
        answer = input("Push enter key to draw again or type 'N' to quit. :").lower()
        if answer == 'n':
            break

