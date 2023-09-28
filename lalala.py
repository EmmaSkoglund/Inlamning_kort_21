import os
from card_deck import CardDeck

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

card_deck = CardDeck()
shuffleDeck = card_deck.shuffle()

def display_hand(hand):
    for card in hand:
        print(f"{card['Suit']} : {card['Value']}\nPoints: {card['Points']}")

dealerHand = [card_deck.draw_card()]
playerHand = [card_deck.draw_card()]

dealersTurn = False

ui = 30

while True:
    clear_screen()

    print("*" * ui)
    print(".: WELCOME :.".center(ui))
    print("*" * ui)
    print("You're about to play a card\ngame called 21\nDo you want to play?")
    print("-" * ui)
    answer = input("Y/N > ").lower()

    if answer == "y":
        break

    elif answer == "n":
        break

print("Let's start the game ")
print("-" * ui)
input("Press enter to continue...")

print("-" * ui)
print("The goal is to come as close to \n21 as you can. If you get more, \nyou lose.")
print("-" * ui)
print("Rules:\nThe dealer starts by giving the \nplayer two cards")
print("The player can decide to either\nbe dealt another card or to stop")
print("When the player decides to stop, \nit is the dealer's turn to play, \nwith open cards.")
print("The dealer plays by the same \nrules as the player.")
print("But... if the score is tied, \nthe dealer wins.")
print("-" * ui)

while True:
    clear_screen()

    print("Player's hand:")
    display_hand(playerHand)

    print("-" * 5)
    print("Dealer's hand:")
    display_hand(dealerHand)

    playerPoints = card_deck.calculate_points(playerHand)

    if playerPoints == 21:
        print("Player wins!")
        break

    elif playerPoints < 21:
        print("-" * 5)
        print("Do you want to add a new card? Y/N")
        addCard = input("> ").lower()
        if addCard == "y":
            newCard = card_deck.draw_card()
            if newCard is not None:
                playerHand.append(newCard)
                print("\nNew card for player:")
                display_hand([newCard])
        elif addCard == "n":
            dealersTurn = True
        else:
            print("No more cards in the deck.")
            break

    elif playerPoints > 21:
        print("-" * 5)
        print("You lost and the dealer wins!")

    else:
        dealersTurn = True

    dealerPoints = card_deck.calculate_points(dealerHand)

    while dealersTurn:
        clear_screen()

        print("Player's hand:")
        display_hand(playerHand)

        print("-" * 5)
        print("Dealer's hand:")
        display_hand(dealerHand)

        dealerPoints = card_deck.calculate_points(dealerHand)

        if dealerPoints == 21:
            print("Dealer wins!")
            break

        elif dealerPoints < 17:
            print("-" * 5)
            print("Dealer draws another card.")
            newCard = card_deck.draw_card()
            if newCard is not None:
                dealerHand.append(newCard)
                print("\nNew card for dealer:")
                display_hand([newCard])
        else:
            print("Dealer stops.")
            if dealerPoints > 21 or (playerPoints <= 21 and playerPoints > dealerPoints):
                print("Player wins!")
            elif dealerPoints > playerPoints:
                print("Dealer wins!")
            else:
                print("It's a tie!")
            dealersTurn = False

    playAgain = input("Do you want to play again? Y/N: ")
    if playAgain == "y":
        input("Press enter to play again...")
        card_deck = CardDeck()
        shuffleDeck = card_deck.shuffle()
        dealerHand = [card_deck.draw_card()]
        playerHand = [card_deck.draw_card()]
        dealersTurn = False
    else:
        break
