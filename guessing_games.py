import random


def rps():
    options = ["rock", "paper", "scissors"]

    w = 0
    l = 0
    tie = 0

    while True:
        user_input = input(
            "choose your options... Rock|Paper|Scissors or press Q to exit: ").lower()
        if user_input == "q":
            break
        if user_input not in options:
            print("please enter a valid option")
            continue
        computer_input = random.randint(0, 2)
        computer_input = options[computer_input]
        print("Computer choice: " + computer_input)
        if user_input == "rock" and computer_input == "scissors":
            w += 1
            print("You won!")
        elif user_input == "paper" and computer_input == "rock":
            w += 1
            print("You won!")
        elif user_input == "scissors" and computer_input == "paper":
            w += 1
            print("You won!")
        elif user_input == computer_input:
            tie += 1
            print("Tie!")
        else:
            l += 1
            print("You loose :C")

    print("Wins: " + str(w))
    print("Loses: " + str(l))
    print("Tie: " + str(tie))
    main()


def main():
    print("Choose your game: ")
    print("1. Rock, Paper, Scissors")
    print("2. quit")
    user_input = input("Enter your choice: ")
    if user_input == str(1):
        rps()
    elif user_input == str(2):
        print("Cya! Until next time")


main()
