# Importerar os för att rensa terminalen
# Hämter klassen CardDeck från filen Tjugoett_class
import os
from Tjugoett_class import CardDeck


# Funktion för att rensa skärmen beroende på operativsystem
def clearScreen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Skapar en funktion som visar kortens utseende
def displayHand(hand):
    rows = ['', '', '', '']
    for card in hand:
        value = card['Value']
        suit = card['Suit']
        if value == '14':
            value = 'A'  # Konvertera "14" till "A" om det är ett ess
        # Skapa rader för varje kort
        rows[0] += ' ___'.format()
        rows[1] += '|{} | '.format(value.ljust(2))
        rows[2] += '| {} | '.format(suit)
        rows[3] += '|_{}| '.format(value.rjust(2, '_'))
        # Skriv ut varje rad
    for row in rows:
        print(row)


def welcomeDisplay():
    # Välkomstmeddelande
    print("-" * 40)
    print(".: Welcome :.".center(40))
    play = input("You will now get to play the card game 21!\nDo you want to play? Y/N > ").lower()
    try:
        if play == "n":
            return False
        elif play == "j":
            return True
    except ValueError:
        input("ERROR: Wrong choice! Please select Y/N\nPress enter to continue...")


def rules():
    # Visar regler och hur man spelar
    print("-" * 40)
    print("This is how the game works. You play against a dealer,")
    print("The game starts off by being dealt one card each, the player and the dealer.")
    print("Each round you have a choice to either be dealt another card or stop.")
    print("The goal is to reach 21 points.")
    print("If your score surpasses \"21\" you lose, the same rules apply to the dealer, ")
    print("The one closest to 21 at the end of game, win")
    print("If it's a tie, the dealer win.")
    print("The player is the first to play, then the dealer.")
    input("Press enter to continue...")


 # Huvudfunktionen här alla regler finns för hur spelet ska gå till
def playRound(deck):
    deck.shuffle()
    playerHand = [deck.draw_card()]
    dealerHand = [deck.draw_card()]
    playerTurn = True
    playerPoint = 0
    dealerPoint = 0

    while True:
        clearScreen() # Rensa skärmen för att skapa en känsla av omgången

        # Visa spelarens hand
        print('-' * 30)
        print("Player's Hand:")
        displayHand(playerHand)
        playerPoint = deck.calculate_points(playerHand,)
        print("Total player score:", playerPoint)
        print('-' * 5)

        # Visa dealerns hand
        print("Dealer's Hand:")
        displayHand(dealerHand)
        dealerPoint = deck.calculate_points(dealerHand,)
        print("Total dealer score:", dealerPoint)
        print("-" * 5)

        if playerTurn:
            newCard = input("Do you want a new card? Y/N\n> ").lower()

            if newCard == "n":
                # Om spelaren inte vill ha fler kort och det finns ett ess i handen,
                # låt spelaren välja om esset ska vara värt 1 eller 14 poäng
                if any(card['Value'] == 'A' for card in playerHand):
                    valueChoice = int(input("Should ace resemble \"1\" or \"14\": "))
                    for card in playerHand:
                        if card['Value'] == 'A':
                            if valueChoice == 14:
                                card['Value'] = '14' # Sätt essets värde till 14 om spelaren väljer det
                            else:
                                card['Value'] = '1' # Annars sätt essets värde till 1
                playerTurn = False # Sätter dealerns tur att spela om spelaren valt att inte ta fler kort


            elif newCard == "y":
                newCard = deck.draw_card()
                playerHand.append(newCard) # Lägger till nytt kort om speleren väljer att ta ett nytt kort

                clearScreen()
                print('-' * 30)
                print("Player's Hand:")
                print(f"You drew: {newCard['Value']} of {newCard['Suit']}")
                displayHand(playerHand)
                playerPoint = deck.calculate_points(playerHand)
                print("Total player score:", playerPoint)
                print("-" * 5)

                # Visa dealerns hand efter att spelaren har dragit ett kort
                print("Dealer's Hand:")
                displayHand(dealerHand)
                dealerPoint = deck.calculate_points(dealerHand,)
                print("Total dealer score:", dealerPoint)
                print("-" * 5)
            else:
                # Ger ett felmeddelande om verken j/n angivits
                input("ERROR: Wrong choice! Please select Y/N\nPress enter to continue...")

            if playerPoint == 21:
                print("The player has won!")
                break
            elif playerPoint > 21:
                print("You lost, and the dealer has won!")
                break

        else:
            if dealerPoint < 17:
                print("Dealer takes a new card")
                newCard = deck.draw_card()
                dealerHand.append(newCard) # dealern välger att ta ett nytt kort om poängsumman är under 17

                # Justera essvärdet beroende på dealerns poäng
                for card in dealerHand:
                    if card['Value'] == 'A' and dealerPoint < 10:
                        card['Value'] = '14'
                    elif card['Value'] == 'A':
                        card['Value'] = '1'

                clearScreen()
                print('-' * 30)
                print("Player's Hand:")
                displayHand(playerHand)
                playerPoint = deck.calculate_points(playerHand)
                print("Total player score:", playerPoint)
                print("-" * 5)

                # Visa dealerns hand efter att dealern har dragit ett kort
                print("Dealer's Hand:")
                print(f"The dealer drew: {newCard['Value']} of {newCard['Suit']}")
                displayHand(dealerHand)
                dealerPoint = deck.calculate_points(dealerHand)
                print("Total dealer score:", dealerPoint)
                print("-" * 5)
                input("Press Enter to continue...")

            elif dealerPoint == 21:
                print("The dealer has won!")
                break
            elif dealerPoint > 21:
                print("The dealer has lost!")
                break
            elif dealerPoint >= playerPoint:
                print("The dealer has won!")
                break
            elif playerPoint > dealerPoint:
                print("The player has won!")
                break
        

# Funktion för att fråga om användaren vill spela igen
# Istället för att använda denna del vid varje vilkor av poängsättning
def playAgain():
    while True:
        play_again = input("Do you want to play again? (Y/N) > ").lower()
        if play_again == "n":
            return False
        elif play_again == "y":
            return True
        else:
            input("ERROR: Wrong choice! Please select Y/N\nPress enter to continue...")


# Huvudfunktion som initierar spelet
def main():
    welcomeDisplay()
    rules()

    while True:
        # Skapa en ny kortlek för varje spel
        # Anropar huvudfunktionen
        deck = CardDeck()
        playRound(deck)
        if not playAgain(): # Bryter spelet om användaren inte vill spela mer
            break


        
if __name__ == "__main__":
    main() # Kör main-funktionen
