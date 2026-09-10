import random

# 5 predefined words
words = ["python", "computer", "programming", "developer", "algorithm"]

# Random word select
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

print("=" * 40)
print("       🎮 HANGMAN GAME")
print("=" * 40)
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses.")

# Main game loop
while wrong_guesses < max_wrong_guesses:

    # Display current word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)

    # Check win
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 Congratulations! You guessed the word!")
        print("The word was:", word)
        break

    # Take user input
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one alphabet letter.")
        continue

    # Check repeated guess
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in word:
        print("✅ Correct guess!")
    else:
        wrong_guesses += 1
        print("❌ Wrong guess!")

else:
    print("\n💀 Game Over!")
    print("The correct word was:", word)

print("\nThanks for playing! 🎮")