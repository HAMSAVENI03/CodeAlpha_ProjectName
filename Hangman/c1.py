import random
def hangman():
    words = ["apple", "tiger", "chair", "plant", "bread"]
    word = random.choice(words)
    guessed_letters = []
    attempts = 6
    display_word = ["_"] * len(word)
    print(" Welcome to Hangman Game!")
    while attempts > 0 and "_" in display_word:
        print("\nWord:", " ".join(display_word))
        print("Attempts left:", attempts)
        guess = input("Enter a letter: ").lower()
        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue
        guessed_letters.append(guess)
        if guess in word:
            print("Correct guess!")
            for i in range(len(word)):
                if word[i] == guess:
                    display_word[i] = guess
        else:
            print("Wrong guess!")
            attempts -= 1
    if "_" not in display_word:
        print("\n You won! The word was:", word)
    else:
        print("\n You lost! The word was:", word)
hangman()