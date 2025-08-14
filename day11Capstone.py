import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def userturn(userHand, computerHand):
    userSafe = True
    while userSafe:
        print(f"{userHand}, total score: {sum(userHand)}")
        if sum(userHand) == 21:
            print("21, Computer's turn!")
            return
        print(f"Computer's first card: {computerHand[0]}")
        userOption = input("Would you like another card? Y or N ").lower()
        if userOption == 'y':
            userHand.append(random.choice(cards))
            userTotal = sum(userHand)
            while userTotal > 21 and 11 in userHand:
                i = userHand.index(11)
                userHand[i] = 1
                userTotal = sum(userHand)
                print(f"user total: {userTotal}");
            if userTotal > 21:
                print(f"{userHand}, total score: {userTotal}")
                print("Bust! Dealer Wins")
                return
        else:
            return

def computerturn(userHand, computerHand):
    computerTotal = sum(computerHand)
    while computerTotal <= 16:
        computerHand.append(random.choice(cards))
        computerTotal = sum(computerHand)
        while computerTotal > 21 and 11 in computerHand:
            i = computerHand.index(11)
            computerHand[i] = 1
            computerTotal = sum(computerHand)
    print(f"Final user hand: {userHand}, total score: {sum(userHand)}")
    print(f"Final computer hand: {computerHand}, total score: {computerTotal}")
    if computerTotal > 21 or computerTotal < sum(userHand):
        print("User Wins")
        return
    if computerTotal > sum(userHand) and computerTotal <= 21 or computerTotal == 21:
        print("Computer Wins")
        return
    if computerTotal == sum(userHand) and computerTotal != 21:
        print("Game tied!")
        return

def blackjack():
    userHand = [random.choice(cards), random.choice(cards)]
    computerHand = [random.choice(cards), random.choice(cards)]
    userturn(userHand, computerHand)
    if sum(userHand) <= 21:
        computerturn(userHand, computerHand)
    playAgain = input("Would you like to play again? Y or N ").lower()
    if playAgain == 'y':
        print("\n" * 20)
        blackjack()
    else:
        return

blackjack()