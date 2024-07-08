from random import randint


def main():
    while True:
        try:
            min = int(input("Minimum: "))
            max = int(input("Maximum: "))
            if min > max:
                print("Invalid minimum! Must be less than the maximum!")
        except ValueError:
            print("Invalid Inputs! Must be an integer!")
        else:
            match loop(min, max):
                case "b":
                    break
                case _:
                    pass


def loop(min, max):
    scale = randint(min, max)
    while True:
        guess = input("Guess: ")
        try:
            guess = int(guess)
            if scale == guess:
                print("Your guess is correct!")
                return "b"; break
            elif scale > guess:
                print("Your guess is less than the number!")
            else:
                print("Your guess is greater than the number!")
        except ValueError:
            print("Error raised! Invalid guess: Must be an integer!")


if __name__ == "__main__":
    main()
