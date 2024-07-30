import random

def get_random_word():
    words = ["janita", "kotli", "impossible", "programming", "task"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_hangman():
    word = get_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Word Challenge Game!")
    
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Guessed letters: {guessed_letters}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Good guess!")
            if set(word).issubset(guessed_letters):
                print(f"\nCongratulations! You've guessed the word: {word}")
                break
        else:
            incorrect_guesses += 1
            print("Incorrect guess.")

    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nYou've run out of guesses. The word was: {word}. Better luck next time :)")

if __name__ == "__main__":
    play_hangman()
