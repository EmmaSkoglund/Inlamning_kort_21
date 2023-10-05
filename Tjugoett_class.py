import random

class CardDeck:
    def __init__(self):
        # Skapar en kortlek med alla kort i ordningen Hjärter, Ruter, Spader, Klöver
        hearts = chr(9829)
        diamonds = chr(9830)
        spades = chr(9824)
        clubs = chr(9827)

        # Definiera de olika korten som finns i en kortlek
        suits = [hearts, diamonds, spades, clubs]
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        # Skapa en kortlek genom att kombinera alla möjliga valörer och färger
        self.deck = [{'Value': value, 'Suit': suit, 'Points': self.assign_points(value)} for suit in suits for value in
                     values]

    def assign_points(self, card_value):
        # Tilldela poäng till kort baserat på dess värde
        if card_value == 'K': # King
            return 13
        elif card_value == 'Q': # Queen
            return 12
        elif card_value == 'J': # Jack
            return 11
        elif card_value == 'A': # Ace
            return 0
        else:
            return int(card_value)

    def shuffle(self):
        # Blanda kortleken slumpmässigt
        random.shuffle(self.deck)

    def calculate_points(self, hand):
        # Beräkna totala poängen för en hand baserat på kortens värden
        points = 0
        for card in hand:
            points += self.assign_points(card['Value'])
        return points

    def draw_card(self):
        # Dra ett kort från kortleken om det finns kort kvar
        if not self.deck:
            return None
        else:
            return self.deck.pop()


