from random import choice


def main():
    print("""
    Welcome to Word Guess!
    ------------------------------
    You need to guess letters one by one to reveal the word!""")
    
    name = input("Your Name: ")
    print(f"Goodluck, {name}!")

    with open("words.txt", 'r') as txtfile:
        words = txtfile.readlines()
    word = choice(words).strip()

    guessed = []
    remaining_attempts = 5
    correct_guess = ["_"] * len(word)

    game_state(word, guessed, remaining_attempts, correct_guess)

    while remaining_attempts > 0 and "_" in correct_guess:
        guessed_letter = input("Letter: ")

        if len(guessed_letter) != 1 or guessed_letter in guessed:
            print("Invalid guess: Please enter a single new letter!")
            continue

        guessed.append(guessed_letter)

        if guessed_letter in word:
            print("Correct Guess!")
            for index, char in enumerate(word):
                if char == guessed_letter:
                    correct_guess[index] = guessed_letter
        else:
            print("Incorrect Guess!")
            remaining_attempts -= 1

        game_state(word, guessed, remaining_attempts, correct_guess)
    
    game_end_conditions(word, name, correct_guess)

    again = input("Play again (y/n): ")
    if again.lower() == "y" or again.lower() == "yes":
        main()
    else:
        print("Thanks for playing!")


def game_state(word, guessed, remaining_attempts, correct_guess):
    print(f"Word has {len(word)} letters.")
    print(" ".join(correct_guess))
    print(f"You have {remaining_attempts} remaining attempts left!")


def game_end_conditions(word, name, correct_guess):
    if "_" not in correct_guess:
        print(f"Congratulations, {name}! You guessed it!")
    else:
        print(f"Uh oh, you ran out of attempts. The word was {word}")


if __name__ == "__main__":
    main()
