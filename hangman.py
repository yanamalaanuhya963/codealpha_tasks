import random

# Predefined list of 5 words
word_list = ["apple", "bread", "chair", "house", "plant"]

# Randomly choose a word from the list
secret_word = random.choice(word_list)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("_ " * len(secret_word))

# Game loop
while incorrect_guesses < max_guesses:
    guess = input("Enter a letter: ").lower()

    # Input validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Incorrect! You have", max_guesses - incorrect_guesses, "guesses left.")

    # Show current progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(display_word.strip())

    # Check for win
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You guessed the word:", secret_word)
        break

# If player didn't win
if incorrect_guesses == max_guesses:
    print("Game Over! The word was:", secret_word)
