from cardDeck import CardDeck

deck = CardDeck()
deck.shuffle()

playerHand = deck.draw_card()
dealerHand = deck.draw_card()

print("Player's hand:")
for card in playerHand:
    print(f"{card['Suit']} {card['Value']} : {card['Points']} points")

