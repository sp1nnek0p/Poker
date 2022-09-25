suits = ['♠','♣','♥','♦']
cards_numbers = ['1', '2', '3', '4', '5','6','7','8','9','10','11', '12', '13']

# Standard 52 Card Deck, 1 = A, 11 = J, 12 = Q, 13 = K
cards = [k + i for i in suits for k in cards_numbers]
