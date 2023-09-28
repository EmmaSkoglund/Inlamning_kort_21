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

dealerTurn = False

while True:
    clearScreen()
    print('-' * 30)
    print(f"Player's Hand:")
    for card in playerHand:
        playerPoint = deck.calculate_points(playerHand)
        print(f"{card['Value']} of {card['Suit']}")
    print("Total player score:", playerPoint)
        
    print('-' * 5)
    print(f"Dealer's Hand:")
    for card in dealerHand:
        dealerPoint = deck.calculate_points(dealerHand)
        print(f"{card['Value']} of {card['Suit']}")
    print("Total player score:", dealerPoint)
        
    print("-" * 5)
    newCard = input("Do you want a new card? Y/N\n> ").lower()

    try: 
        if newCard == "n":
            break 
        elif newCard == "y":
            newCard = deck.draw_card()
            playerHand.append(newCard)
    except ValueError:
        print("ERROR:")

    if playerPoint == 21:
        playAgain = input("The player has won!\nDo you want you play agen... > ")
        try:
            if playAgain == "n":
                break
            elif playAgain == "y":
                continue
        except ValueError: 
            print("ERROR:")

    elif playerPoint > 21:
        playAgain = input("you lost and the dealer has won!\nDo you want you play agen... > ")
        try:
            if playAgain == "n":
                break
            elif playAgain == "y":
                continue
        except ValueError: 
            print("ERROR:")

    elif playerPoint < 21:
        if playAgain == "n":
            dealerTurn = True

    if dealerPoint < 17:
            print("Dealern took a new card")
            newCard = deck.draw_card()
            dealerHand.append(newCard)
            if dealerPoint == playerPoint or dealerPoint > playerPoint:
                playAgain = input("The dealer has won!\nDo you want you play agen... > ")
                try:
                    if playAgain == "n":
                        break
                    elif playAgain == "y":
                         continue
                except ValueError: 
                        print("ERROR:")
            elif playerPoint > dealerPoint:
                playAgain = input("The player has won!\nDo you want you play agen... > ")
                try:
                    if playAgain == "n":
                        break
                    elif playAgain == "y":
                         continue
                except ValueError: 
                        print("ERROR:")
            
    elif dealerPoint == 21:
        playAgain = input("The dealer has won!\nDo you want you play agen... > ")
        try:
            if playAgain == "n":
                break
            elif playAgain == "y":
                continue
        except ValueError: 
            print("ERROR:")
        
    elif dealerPoint > 21:
        playAgain = input("The dealer has lost!\nDo you want you play agen... > ")
        try:
            if playAgain == "n":
                break
            elif playAgain == "y":
                continue
        except ValueError: 
            print("ERROR:")



