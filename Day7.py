from random import choice

random_words = [
    "nebula", "whisker", "quantum", "frost", "echo", "glyph", "ember",
    "raven", "throttle", "lumen", "crimson", "orbit", "drizzle",
    "cipher", "wisp", "nimbus", "zenith", "flux", "hollow", "blizzard"
]

hangman_stages = [
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    ========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    ========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    ========""",
    """
     +---+
     |   |
         |
         |
         |
         |
    ========"""
]

chosen_word = choice(random_words)
placeholder = ""
won_game = False
for letter in chosen_word:
    placeholder += "_"
print(chosen_word)
print(placeholder)
total_correct_guesses = []
lives = 6

while won_game is False:
    user_guess = input("Guess a letter: ").lower()
    display = ''
    for letter in chosen_word:
        if letter == user_guess:
            display += letter
            total_correct_guesses.append(letter)
        elif letter in total_correct_guesses:
            display += letter
        else:
            display += "_"
    if user_guess not in chosen_word:
        lives -= 1
        print(hangman_stages[lives])
        if lives == 0:
            print("You LOSE!")
            won_game = True
            break
    if display == chosen_word:
        print("You WIN!")
        won_game = True
    print(display)


