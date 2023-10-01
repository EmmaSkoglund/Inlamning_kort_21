import random

class CardDeck:
    def __init__(self):
        h = chr(9829) # h = hearts
        d = chr(9830) # d = diamonds
        s = chr(9824) # s = spades
        c = chr(9827) # c = clubs

        suits = [h, d, s, c]
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


        self.deck = [{'Value': value, 'Suit': suit, 'Points': self.assign_points(value)} for suit in suits for value in
                     values]

    def assign_points(self, card_value):
        if card_value == 'K': # King
            return 13
        elif card_value == 'Q': # Queen
            return 12
        elif card_value == 'J': # Jack
            return 11
        elif card_value == 'A': # Ace
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


