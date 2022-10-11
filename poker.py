# https://en.wikipedia.org/wiki/List_of_poker_hands#:~:text=A%20full%20house%2C%20also%20known,or%20%22threes%20full%22).
from collections import defaultdict
import itertools
import random


class Poker():
    def _straight_flush(self, hand: list) -> bool:
        """
        Takes in a hand of cards as a list
        Checks if the hand contains a straight flush
        Returns Bool
        """
        # A straight flush is a hand that contains five cards of sequential rank
        if self._flush(hand) and self._straight(hand):
            return True
        return False


    def _four_of_kind(self, hand: list ) -> bool:
        """
        Takes in a hand of cards as a list
        Checks if the hand contains four of a kind
        Returns Bool
        """
        # Four of a kind, also known as quads, is a hand that contains 
        # four cards of one rank and one card of another rank 
        card_numbers = sorted([int(i[:-1]) for i in hand])
        count = defaultdict(lambda:0)
        for n in card_numbers:
            count[n]+=1
        
        if sorted(count.values()) == [1,4]:
            return True
        return False


    def _full_house(self, hand) -> bool:
        """
        Takes in a hand of cards as a list
        Checks if the hand contains a full house
        Returns Bool
        """
        # A full house, also known as a full boat or a tight or a boat 
        # (and originally called a full hand), is a hand that contains 
        # three cards of one rank and two cards of another rank
        card_numbers = sorted([int(i[:-1]) for i in hand])
        count = defaultdict(lambda:0)
        for n in card_numbers:
            count[n]+=1
        
        if sorted(count.values()) == [2,3]:
            return True
        return False


    def _flush(self, hand: list) -> bool:
        """
        Takes in a hand of cards as a list
        Checks if the hand contains a flush
        Returns Bool
        """
        # A flush is a hand that contains five cards all of the same suit
        card_suits = [i[-1] for i in hand]
        j = itertools.groupby(card_suits)
        for k in j: break
        for k in j: return False
        return True


    def _straight(self, hand: list) -> bool:
        """
        Takes in a hand of cards as a list
        Checks if the hand contains a straight
        Returns Bool
        """
        # A straight is a hand that contains five cards of sequential rank
        card_numbers = sorted([int(i[:-1]) for i in hand])
        if len(set(card_numbers)) != 5:
            return False
        elif card_numbers[0] + 4 == card_numbers[4]:
            return True
        return False


    def _three_of_kind(self, hand) -> bool:
        """
        Takes in a hand of cards as a list
        Checks if the hand contains three of a kind
        Returns Bool
        """
        # Three of a kind, also known as trips or a set, is a hand that 
        # contains three cards of one rank and two cards of two other ranks
        card_numbers = sorted([int(i[:-1]) for i in hand])
        count = defaultdict(lambda:0)
        for n in card_numbers:
            count[n]+=1
        
        if sorted(count.values()) == [1,1,3]:
            return True
        return False


    def _two_pair(self, hand) -> bool:
        """
        Takes in a hand of cards as a list
        Checks if the hand contains two pairs
        Returns Bool
        """
        # Two pair is a hand that contains two cards of one rank, 
        # two cards of another rank and one card of a third rank 
        card_numbers = sorted([int(i[:-1]) for i in hand])
        count = defaultdict(lambda:0)
        for n in card_numbers:
            count[n]+=1
        
        if sorted(count.values()) == [1,2,2]:
            return True
        return False


    def _one_pair(self, hand) -> bool:
        """
        Takes in a hand of cards as a list
        Checks if the hand contains at least one pair
        Returns Bool
        """
        # One pair, or simply a pair, is a hand that contains two 
        # cards of one rank and three cards of three other ranks
        card_numbers = sorted([int(i[:-1]) for i in hand])
        count = defaultdict(lambda:0)
        for n in card_numbers:
            count[n]+=1
        if 2 in count.values():
            return True
        return False


    def calculate_hand(self, hand: list) -> str:
        """
        Takes in your hand as a list of cards
        Evaluates the Poker hand
        Returns a string of what you have in hand
        """
        if self._straight_flush(hand):
            return 'Straight Flush'
        elif self._four_of_kind(hand):
            return 'Four of a Kind'
        elif self._full_house(hand):
            return 'Full House'
        elif self._flush(hand):
            return 'Flush'
        elif self._straight(hand):
            return 'Straight'
        elif self._three_of_kind(hand):
            return 'Three of a Kind'
        elif self._two_pair(hand):
            return 'Two Pair'
        elif self._one_pair(hand):
            return 'One Pair'
        else:
            return 'High Card'


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
        

    def deal_cards(self, cards: list, num_players: int = 1) -> list:
        """
        Accepts a list of all cards in a 52 deck, and amount of players
        Selects a random hands from the 52 card deck for the amount of players
        Max players is 7, if players is more than 1 will return a matrix of lists
        Else just Returns your hand as a list
        """
        # Make a copy of the list of cards that get passed to this function
        # Shuffle the copy of the cards 
        # Picks a random card and removes it from the deck and then choose another card
        # from the remainder of the deck to ensure no duplicates are picked
        cards_copy = cards.copy()
        if num_players == 1:
            self.hand = []
            for _ in range(5):
                self.selection = random.choice(cards_copy)
                cards_copy.pop(cards_copy.index(self.selection))
                self.hand.append(self.selection)
            return self.hand
        elif num_players < 6:
            self.all_players = []
            for _ in range(num_players):
                self.hand = []
                for _ in range(5):
                    self.selection = random.choice(cards_copy)
                    cards_copy.pop(cards_copy.index(self.selection))
                    self.hand.append(self.selection)
                self.all_players.append(self.hand)

            return self.all_players