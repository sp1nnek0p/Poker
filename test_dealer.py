"""
    Testing the dealer from the poker class
"""

from poker import Poker
from cards import cards

dealer = Poker()

for i in dealer.deal_cards(cards, 5):
    print(' '.join(dealer.replace_to_suits(i)), ':', dealer.calculate_hand(i))

