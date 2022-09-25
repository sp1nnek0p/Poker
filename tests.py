from poker import Poker
import os

# Variable for testing the functions
straight_flush = ['2♥','3♥','4♥','5♥','6♥']
not_straight_flush = ['1♥','3♥','4♥','5♥','8♥']

four_of_kind = ['2♥','2♣','2♦','5♥','2♠']
not_four_of_kind = ['2♥','2♣','3♦','5♥','2♠']

full_house = ['2♥','2♣','3♦','3♥','3♠']
not_full_house = ['2♥','3♣','3♦','3♥','3♠']

flush = ['2♥','3♥','5♥','7♥','8♥']
not_flush = ['2♥','3♥','5♠','7♥','8♠']

straight = ['9♥','10♣','11♦','12♥','13♠']
not_straight = ['2♥','3♣','3♦','3♥','3♠']

three_of_kind = ['9♥','9♣','9♦','12♥','13♠']
not_three_of_kind = ['9♥','9♣','8♦','12♥','13♠']

two_pair = ['9♥','9♣','10♦','13♥','13♠']
not_two_pair = ['9♥','9♣','8♦','12♥','13♠']

one_pair = ['9♥','9♣','10♦','11♥','13♠']
not_one_pair = ['1♥','9♣','8♦','12♥','13♠']


os.system('cls')
poker = Poker()

# STRAIGHT FLUSH TEST
print('STRAIGHT FLUSH TEST')
print(poker.replace_to_suits(straight_flush), " :", end='')
print(poker._straight_flush(straight_flush))
print(poker.replace_to_suits(not_straight_flush), " :", end='')
print(poker._straight_flush(not_straight_flush))
print('--------------------------------------------------')

# FOUR OF A KIND TEST
print('FOUR OF A KIND TEST')
print(poker.replace_to_suits(four_of_kind), " :", end='')
print(poker._four_of_kind(four_of_kind))
print(poker.replace_to_suits(not_four_of_kind), " :", end='')
print(poker._four_of_kind(not_four_of_kind))
print('--------------------------------------------------')

# FULL HOUSE TEST
print('FULL HOUSE TEST')
print(poker.replace_to_suits(full_house), " :", end='')
print(poker._full_house(full_house))
print(poker.replace_to_suits(not_full_house), " :", end='')
print(poker._full_house(not_full_house))
print('--------------------------------------------------')

# FLUSH TEST
print('FLUSH TEST')
print(poker.replace_to_suits(flush), " :", end='')
print(poker._flush(flush))
print(poker.replace_to_suits(not_flush), " :", end='')
print(poker._flush(not_flush))
print('--------------------------------------------------')

# STRAIGHT TEST
print('STRAIGHT TEST')
print(poker.replace_to_suits(straight), " :", end='')
print(poker._straight(straight))
print(poker.replace_to_suits(not_straight), " :", end='')
print(poker._straight(not_straight))
print('--------------------------------------------------')

# THREE OF A KIND TEST
print('THREE OF A KIND TEST')
print(poker.replace_to_suits(three_of_kind), " :", end='')
print(poker._three_of_kind(three_of_kind))
print(poker.replace_to_suits(not_three_of_kind), " :", end='')
print(poker._three_of_kind(not_three_of_kind))
print('--------------------------------------------------')

# TWO PAIR TEST
print('TWO PAIR TEST')
print(poker.replace_to_suits(two_pair), " :", end='')
print(poker._two_pair(two_pair))
print(poker.replace_to_suits(not_two_pair), " :", end='')
print(poker._two_pair(not_two_pair))
print('--------------------------------------------------')

# ONE PAIR TEST
print('ONE PAIR TEST')
print(poker.replace_to_suits(one_pair), " :", end='')
print(poker._one_pair(one_pair))
print(poker.replace_to_suits(not_one_pair), " :", end='')
print(poker._one_pair(not_one_pair))
print('--------------------------------------------------')