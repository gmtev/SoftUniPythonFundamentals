def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "You can't divide by zero!"


def multiplication(a, b):
    return a * b


def main():
    print('''Welcome to Python Calculator! 
    Menu:
    Addition - 1
    Subtraction - 2
    Multiplication - 3
    Division - 4
    Quit - 5''')
    while True:
        choice = input("Enter your choice: ")
        if choice == "5":
            print("Goodbye!")
            break
        else:
            a = int(input("Enter the first number:"))
            b = int(input("Enter the second number:"))
            if choice == "1":
                print(addition(a, b))
            elif choice == "2":
                print(subtraction(a, b))
            elif choice == "3":
                print(multiplication(a, b))
            elif choice == "4":
                print(division(a, b))
            else:
                print("Invalid input!")


main()
