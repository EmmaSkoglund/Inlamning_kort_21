import os
from card_deck import CardDeck

card_deck = CardDeck()
shuffleDeck = card_deck.shuffle()


def display_hand(hand):
    for card in hand:
        print(f"{card['Suit']} : {card['Value']}\nPoints: {card['Points']}")


dealerHand = [card_deck.draw_card()]
playerHand = [card_deck.draw_card()]

dealersTurn = False

ui = 30


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
"""""

while True:
    
    print("*" * ui)
    print(".: WELCOME :.".center(ui))
    print("*" * ui)
    print("Your're about to play a card\ngame called 21\nDo you want to play?")
    print("-" * ui)
    answer = input("Y/N > ").lower()

    if answer == "y":
        break

    elif answer == "n":
        break

print("Lets start the game ")
print("-" * ui)
input("Press enter to continue...")
"""
print("-" * ui)
print("The goal is to come as close to \n21 as you can. If you get more, \nyou lose.")
print("-" * ui)
print("Rules:\nThe dealer starts to give the \nplayer two cards")
print("The player can decide to either\nbe dealt another card or to stop")
print("When the player decide to stop, \nit is the dealers turn to play, \nwith open cards.")
print("The dealer play by the same \nrules as the player.") 
print("But... if the score is even \nthe dealer wins.")
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
        print("You won")
        break

    elif playerPoints < 21:
        print("-" * 5)
        print("Do you want too add a new card? Y/N")
        addCard = input("> ").lower()
        if addCard == "y":
            newCard = card_deck.draw_card()
            if newCard is not None:
                playerHand.append(newCard)
        elif addCard == "n":
            dealersTurn = True
        else:
            print("No more cards in the deck.")
            break

    elif playerPoints > 21:
        print("-" * 5)
        playAgen = input("You lost and the dealer wins!\nDo you want too play agen? Y/N > ").lower()
        if playAgen == "y":
            input("Press enter to play agen...")
        else:
            break

    else:
        dealersTurn = True

    dealerPoints = card_deck.calculate_points(dealerHand)

    if dealerPoints >= 17:
        print("Dealer stops.")
        if dealerPoints < 21 and dealerPoints > playerPoints:
            print("The dealer wins!")
        elif playerPoints < 21 and playerPoints > dealerPoints:
            print("The player wins")
            break

    elif dealerPoints > 21:
        print("The dealer have lost and the player wins")
        playAgen = input("Do you thant to play agen? Y/N" )
        if playAgen == "y":
            input("Press enter to play agen...")
        elif playAgen == "n":
            break

    elif dealerPoints == 21:
        print("Dealer wins!")
        playAgen = input("Do you thant to play agen? Y/N")
        if playAgen == "y":
            input("Press enter to play agen...")
        elif playAgen == "n":
            break

    elif dealerPoints == playerPoints:
        print("The dealer wins!")
        playAgen = input("Do you thant to play agen? Y/N")
        if playAgen == "y":
            input("Press enter to play agen...")
        elif playAgen == "n":
            break


