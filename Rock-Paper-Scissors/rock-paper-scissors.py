import random


def determine(user, machine):
    if user == machine:
        return 2
    elif (user == 'Rock' and machine == 'Paper') or \
        (user == 'Paper' and machine == 'Scissors') or \
        (user == 'Scissors' and machine == 'Rock'):
        return 0
    else:
        return 1
    

def compare(user_score, machine_score):
    if user_score == machine_score:
        return "It's a TIE!"
    elif user_score > machine_score:
        return "User WINS!"
    else:
        return "Machine WINS!"


def main():
    user_score = 0
    machine_score = 0
    choices = ['Rock', 'Paper', 'Scissors', 'q']
    while True:
        user = input("Rock, Paper, Scissors! Press q to exit! Choose: ")
        machine = random.choice(choices)

        if user not in choices:
            print("Invalid Input!")
        elif user == 'q':
            print(f"""{compare(user_score, machine_score)}
-------------------------
Final Scoreboard:
User: {user_score}
Machine: {machine_score}""")
            break
        else:
            match determine(user, machine):
                case 0:
                    machine_score += 1
                case 1:
                    user_score += 1
                case 2:
                    machine_score += 1
                    user_score += 1
            print(f"User: {user_score} | Machine: {machine_score}")
                

if __name__ == "__main__":
    main()
        