"""
    Testing the dealer prom the poker class
"""

from poker import Poker
from cards import cards

dealer = Poker()

for i in dealer.deal_cards(cards, 2):
    print(' '.join(dealer.replace_to_suits(i)), ':', dealer.calculate_hand(i))

hand = dealer.deal_cards(cards,6)
print(' '.join(dealer.replace_to_suits(hand)), '::', dealer.calculate_hand(hand))