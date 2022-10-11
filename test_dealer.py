"""
    Testing the dealer prom the poker class
"""

from poker import Poker
from cards import cards

dealer = Poker()

for i in dealer.deal_cards(cards, 5):
    print(i)
print(dealer.deal_cards(cards))
