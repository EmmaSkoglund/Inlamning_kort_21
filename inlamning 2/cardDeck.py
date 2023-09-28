import random

import random

class CardDeck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

        # Skapa en kortlek med 52 kort med integer-värden
        self.deck = [{'Value': value, 'Suit': suit, 'Points': self.assign_points(value)} for suit in suits for value in
                     values]

    def assign_points(self, card_value):
        if card_value == 'King':
            return 13
        elif card_value == 'Queen':
            return 12
        elif card_value == 'Jack':
            return 11
        elif card_value == 'Ace':
            return 1
        else:
            return int(card_value)

    def shuffle(self):
        random.shuffle(self.deck)

    def calculate_points(self, hand):
        points = 0
        for card in hand:
            points += self.assign_points(card['Value'])
        return points

    def draw_card(self):
        if not self.deck:
            return None
        else:
            return self.deck.pop()

    def suitsCard(self):
        HEARTS = chr(9829)
        DIAMONDS = chr(9830)
        SPADES = chr(9824)
        CLUBS = chr(9827)
        BACKSIDE = 'backside'
