import random

def hangman_game():
    # 5 predefined words
    words = ["anmol", "code", "anurag", "anu", "a"]

    # Random word choose
    secret_word = random.choice(words)

    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("===================================")
    print("        Welcome to Hangman Game")
    print("===================================")
    print("Guess the word one letter at a time.")
    print("You have only 6 incorrect guesses.\n")

    while wrong_guesses < max_wrong_guesses:
        display_word = ""

        for letter in secret_word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print("Word:", display_word)
        print("Wrong guesses left:", max_wrong_guesses - wrong_guesses)
        print("Guessed letters:", guessed_letters)

        # Win condition
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word correctly.")
            print("The word was:", secret_word)
            break

        guess = input("\nEnter a letter: ").lower().strip()

        # Input validation
        if len(guess) != 1:
            print("Please enter only one letter.\n")
            continue

        if not guess.isalpha():
            print("Please enter only alphabet letters.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!\n")
        else:
            wrong_guesses += 1
            print("Wrong guess!\n")

    else:
        print("\nGame Over!")
        print("You used all 6 incorrect guesses.")
        print("The correct word was:", secret_word)


hangman_game()