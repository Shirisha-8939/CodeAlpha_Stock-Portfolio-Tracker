import random

# Predefined list of words
word_list = ["python", "coding", "hangman", "simple", "logic"]

# Select a random word
secret_word = random.choice(word_list)

# Convert word into hidden format
display_word = ["_"] * len(secret_word)

# Track guessed letters and wrong attempts
guessed_letters = []
wrong_attempts = 0
max_attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print("You have 6 incorrect attempts.\n")

# Game loop
while wrong_attempts < max_attempts and "_" in display_word:
    print("Word:", " ".join(display_word))
    print(f"Wrong attempts left: {max_attempts - wrong_attempts}")
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠ Please enter only one alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check guess
    if guess in secret_word:
        print("✅ Correct guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        wrong_attempts += 1
        print("❌ Wrong guess!\n")

# Result
if "_" not in display_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)