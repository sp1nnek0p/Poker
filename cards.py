suits = ['♠','♣','♥','♦']
cards_numbers = ['1', '2', '3', '4', '5','6','7','8','9','10','11', '12', '13']

# Standard 52 Card Deck, 1 = A, 11 = J, 12 = Q, 13 = K
cards = [k + i for i in suits for k in cards_numbers]


def replace_to_suits(self, hand: list) -> list:
    """
        Accepts a list of your hand of cards
        Replaces 1, 11, 12, 13 with A, J, Q, K respectively
        Returns your hand with new formating
    """
    card_numbers = []
    for n in hand:
        if n[:-1] == '1':
            card_numbers.append('A' + n[-1])
        elif n[:-1] == '11':
            card_numbers.append('J' + n[-1])
        elif n[:-1] == '12':
            card_numbers.append('Q' + n[-1])
        elif n[:-1] == '13':
            card_numbers.append('K' + n[-1])
        else:
            card_numbers.append(n)
    return card_numbers