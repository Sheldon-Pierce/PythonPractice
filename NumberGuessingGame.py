import random

def play_again():
    play = input("Would you like to play again? ")
    if play == "yes":
        print("\n" * 20)
        guessing_game()
    elif play == "no":
        return
    else:
        print("Please enter either 'yes' or 'no'")
        play_again()

def guessing_game():
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    chosen_number = random.randint(1, 100)
    # print("You chose:", chosen_number)
    user_difficulty = input("Choose a difficulty level: Type 'easy' or 'hard' ").lower()
    if user_difficulty == 'easy':
        number_of_guesses = 10
    elif user_difficulty == 'hard':
        number_of_guesses = 5
    else:
        print("Invalid difficulty level.")
        return

    while number_of_guesses != 0:
        user_choice = int(input("Pick a number: "))
        number_of_guesses -= 1
        if user_choice == chosen_number:
            print("You guessed the number with " + str(number_of_guesses) + " guesses left!")
            play_again()
        else:
            if user_choice > chosen_number:
                print('Your guess is too high.')
            else:
                print('Your guess is too low.')
    print("You lose")
    print(f"The number was {chosen_number}.")
    play_again()

guessing_game()