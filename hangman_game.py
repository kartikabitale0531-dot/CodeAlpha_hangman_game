import random

# Predefined words
words = ["python", "java", "computer", "coding", "program"]

# Select a random word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum wrong guesses allowed
wrong_guesses = 0
max_wrong_guesses = 6

print("================================")
print("       HANGMAN GAME")
print("================================")
print("Guess the hidden word!")
print("You have 6 wrong guesses allowed.")

while wrong_guesses < max_wrong_guesses:

    # Display guessed and hidden letters
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses)
    print("Guesses left:", max_wrong_guesses - wrong_guesses)

    # Check whether the player has won
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You won!")
        print("The word was:", word)
        break

    # Take input from player
    guess = input("Enter one letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed this letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

# If the player uses all wrong guesses
if wrong_guesses == max_wrong_guesses:
    print("\nGame Over!")
    print("The correct word was:", word)