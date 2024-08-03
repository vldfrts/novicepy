from tabulate import tabulate
import os
import csv


class Calculator:
    @staticmethod
    def add(x, y):
        return "{:,}".format(float(x) + float(y))

    @staticmethod
    def sub(x, y):
        return "{:,}".format(float(x) - float(y))

    @staticmethod
    def mul(x, y):
        return "{:,}".format(float(x) * float(y))

    @staticmethod
    def div(x, y):
        try:
            result = float(x) / float(y)
            return "{:,}".format(result)
        except ZeroDivisionError:
            return "Division by zero error!"

    @staticmethod
    def exp(x, y):
        try:
            expo = float(x) ** float(y)
            return "{:,}".format(expo)
        except OverflowError:
            return "Result too large!"
    
    @staticmethod
    def fct(x):
        try:
            fctrl = 1
            for i in range(1, int(float(x)) + 1):
                fctrl *= i
            return "{:,}".format(fctrl)
        except ValueError:
            return "Invalid input for factorial"


def main():
    print(commands())
    while True:
        try:
            o = input("Operation: ")
            match(o)
        except SyntaxError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(commands())
        except ValueError:
            print("Invalid Operation or Inputs!")
        except KeyboardInterrupt:
             break    
        

def match(o):
    if o not in ["add", "sub", "mul", "div", "exp", "fct", "clr", "abt", "ext"]:
        raise ValueError
    match o:
        case "clr":
            raise SyntaxError
        case "ext":
            raise KeyboardInterrupt
        case "abt":
            with open("about.txt") as f:
                print(f.read())
        case _:
            x = input("x: ")
            y = input("y: ")
            if len(x) > 50 or len(y) > 50:
                print("x or y 50 Digit Limit is Reached!")
            else:
                print(perform_calculation(o, x, y))


def commands():
    print("SimpleCalc | SimpleCalc Version 1.0")
    with open("commands.csv") as csvfile:
        return tabulate(csv.DictReader(csvfile), headers="keys", tablefmt="rounded_outline")


def perform_calculation(o, x, y):
    match o:
        case "add":
            return f"Sum: {Calculator.add(x, y)}"
        case "sub": 
            return f"Difference: {Calculator.sub(x, y)}"
        case "mul":
            return f"Product: {Calculator.mul(x, y)}"
        case "div":
            return f"Quotient: {Calculator.div(x, y)}"
        case "exp":
            if float(y) > 1000 or float(x) > 10000:
                return "Exponential Limit Reached!"
            else:
                return f"Exponential: {Calculator.exp(x, y)}"
        case "fct":
            if float(x) > 1000:
                return "Factorial Limit Reached"
            return f"Factorial: {Calculator.fct(x)}"
        case _:
            return "Error"


if __name__ == "__main__":
    main()