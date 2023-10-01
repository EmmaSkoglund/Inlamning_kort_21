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
newRound = True

while True:
    while newRound:
        deck.shuffle()
        playerHand = [deck.draw_card()]
        dealerHand = [deck.draw_card()]
        newRound = False
        playerPoint = 0
        dealerPoint = 0

    clearScreen()
    print('-' * 30)
    print(f"Player's Hand:")
    player_rows = ['', '', '', '']
    for card in playerHand:
        value = card['Value']
        suit = card['Suit']
        player_rows[1] += '|{} | '.format(value.ljust(2, '_'))
        player_rows[2] += '| {} | '.format(suit)
        player_rows[3] += '|_{}| '.format(value.rjust(2, '_'))
        print(f"{card['Value']} of {card['Suit']}")
    for row in player_rows:
        print(row)
    playerPoint = deck.calculate_points(playerHand)
    print("Total player score:", playerPoint)
    print('-' * 5)
    print(f"Dealer's Hand:")
    dealer_rows = ['', '', '', '']
    for card in dealerHand:
        value = card['Value']
        suit = card['Suit']
        dealer_rows[1] += '|{} | '.format(value.ljust(2, '_'))
        dealer_rows[2] += '| {} | '.format(suit)
        dealer_rows[3] += '|_{}| '.format(value.rjust(2, '_'))
        print(f"{card['Value']} of {card['Suit']}")
    for row in dealer_rows:
        print(row)
    dealerPoint = deck.calculate_points(dealerHand)
    print("Total dealer score:", dealerPoint)
        
    print("-" * 5)
    if playerTurn:
        newCard = input("Do you want a new card? Y/N\n> ").lower()

        if newCard == "n":
            playerTurn = False
        elif newCard == "y":
            newCard = deck.draw_card()
            playerHand.append(newCard)
            print("You drew:", newCard['Value'], "of", newCard['Suit'])
            value = card['Value']
            suit = card['Suit']
            player_rows[1] += '|{} | '.format(value.ljust(2, '_'))
            player_rows[2] += '| {} | '.format(suit)
            player_rows[3] += '|_{}| '.format(value.rjust(2, '_'))
            print(f"{card['Value']} of {card['Suit']}")
            for row in player_rows:
                print(row)
            playerPoint = deck.calculate_points(playerHand)
            print("Total player score:", playerPoint)
            print("-" * 5)

        if playerPoint == 21:
            playAgain = input("The player has won!\nDo you want to play again? (Y/N) > ").lower()
            if playAgain == "n":
                break
            elif playAgain == "y":
                newRound = True
                continue
            
        elif playerPoint > 21:
            playAgain = input("you lost and the dealer has won!\nDo you want to play again? (Y/N) >").lower()
            if playAgain == "n":
                break
            elif playAgain == "y":
                newRound = True
                continue

    else:
        if dealerPoint < 17:
            print("Dealern took a new card")
            newCard = deck.draw_card()
            dealerHand.append(newCard)

        elif dealerPoint == 21:
            playAgain = input("The dealer has won!\nDo you want to play again? (Y/N) > ").lower()
            if playAgain == "n":
                break
            elif playAgain == "y":
                newRound = True
                continue
           
        elif dealerPoint > 21:
            playAgain = input("The dealer has lost!\nDo you want to play again? (Y/N) > ").lower()
            if playAgain == "n":
                break
            elif playAgain == "y":
                newRound = True
                continue

        elif dealerPoint >= playerPoint:
            playAgain = input("The dealer has won!\nDo you want to play again? (Y/N) > ").lower()
            if playAgain == "n":
                break
            elif playAgain == "y":
                newRound = True
                continue

        elif playerPoint > dealerPoint:
            playAgain = input("The player has won!\nDo you want to play again? (Y/N) > ").lower()
            if playAgain == "n":
                break
            elif playAgain == "y":
                newRound = True
                continue



