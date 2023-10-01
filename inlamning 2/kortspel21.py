import os
from cardDeck import CardDeck


def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


deck = CardDeck()
deck.shuffle()
playerHand = [deck.draw_card()]
dealerHand = [deck.draw_card()]

playerPoint = 0
dealerPoint = 0

playerTurn = True

while True:
    clearScreen()
    print('-' * 30)
    print(f"Player's Hand:")
    for card in playerHand:
        print(f"{card['Value']} of {card['Suit']}")
    playerPoint = deck.calculate_points(playerHand)
    print("Total player score:", playerPoint)
    print('-' * 5)
    print(f"Dealer's Hand:")
    for card in dealerHand:
        print(f"{card['Value']} of {card['Suit']}")
    dealerPoint = deck.calculate_points(dealerHand)
    print("Total player score:", dealerPoint)
        
    print("-" * 5)
    if playerTurn:
        newCard = input("Do you want a new card? Y/N\n> ").lower()

        if newCard == "n":
            playerTurn = False
        elif newCard == "y":
            newCard = deck.draw_card()
            playerHand.append(newCard)
            playerPoint = deck.calculate_points(playerHand)

        if playerPoint == 21:
            playAgain = input("The player has won!\nDo you want you play agen... > ")
            if playAgain == "n":
                break
            elif playAgain == "y":
                dealerPoint, playerPoint = 0, 0
                continue

        elif playerPoint > 21:
            playAgain = input("you lost and the dealer has won!\nDo you want you play agen... > ")
            if playAgain == "n":
                break
            elif playAgain == "y":
                dealerPoint, playerPoint = 0, 0
                continue
    else:
        if dealerPoint < 17:
            print("Dealern took a new card")
            newCard = deck.draw_card()
            dealerHand.append(newCard)
            dealerPoint = deck.calculate_points(dealerHand)

        elif dealerPoint == 21:
            playAgain = input("The dealer has won!\nDo you want you play agen... > ")
            if playAgain == "n":
                break
            elif playAgain == "y":
                dealerPoint, playerPoint = 0, 0
                continue
        
        elif dealerPoint > 21:
            playAgain = input("The dealer has lost!\nDo you want you play agen... > ")
            if playAgain == "n":
                break
            elif playAgain == "y":
                dealerPoint, playerPoint = 0, 0
                continue

        elif dealerPoint >= playerPoint:
            playAgain = input("The dealer has won!\nDo you want to play again? (Y/N) > ")
            if playAgain == "n":
                break
            elif playAgain == "y":
                dealerPoint, playerPoint = 0, 0
                continue

        elif playerPoint > dealerPoint:
            playAgain = input("The player has won!\nDo you want to play again? (Y/N) > ")
            if playAgain == "n":
                break
            elif playAgain == "y":
                dealerPoint, playerPoint = 0, 0
                continue

deck = CardDeck()
deck.shuffle()
playerHand = [deck.draw_card()]
dealerHand = [deck.draw_card()]
playerPoint = 0
dealerPoint = 0
playerTurn = True

