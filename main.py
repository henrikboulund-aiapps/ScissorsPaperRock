import random

result: int = ""

# Present the rules for the game!
print("Winning rules of the game SCISSORS PAPER ROCK are:\n"
      + "Rock vs Paper -> Paper wins\n"
      + "Rock vs Scissor -> Rock wins\n"
      + "Paper vs scissor -> Scissors wins\n")

while True:

    # Present the choices to the users
    print("Enter your choice: \n1 - Rock\n2 - Paper\n3 - Scissors \n")

    # Make the use choose
    choice = int(input("Enter your choice:"))

    # Check if choice is valid
    while choice > 3 or choice < 1:
        choice = int(input("Enter a valid choice please:"))

    # Translate the choice into a name
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = "Paper"
    else:
        choice_name = "Scissors"

    # Present the user choice and let the computer make its choice
    print("User choice is: ", choice_name, "\n\n")
    print("Now it is computer's turn...\n\n")

    comp_choice = random.randint(1, 3)

    # Translate the computer choice to a name!
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"

    print("Computer choice is:", comp_choice_name, "\n\n")
    print(choice_name, " vs. ", comp_choice_name)

    # Decide who is the winner!
    if choice == comp_choice:
        result = "DRAW"
    elif (choice == 1 and comp_choice == 2) or (comp_choice == 1 and choice == 2):
        result = "Paper"
    elif (choice == 1 and comp_choice == 3) or (comp_choice == 1 and choice == 2):
        result = "Rock"
    elif (choice == 2 and comp_choice == 3) or (comp_choice == 2 and choice == 3):
        result = "Scissors"

    # Present the result to the user.
    if result == "DRAW":
        print("<== It's a tie ==>")
    elif result == choice_name:
        print("<== User wins ==>")
    else:
        print("<== Computer wins ==>")

    # Ask if the user would like to play it again
    print("\nWould you like to play again? (n=no, y=yes, default=yes)")
    ans = input().lower()

    if ans == 'n':
        break
    if ans != 'n' or ans != 'y':
        print("Not an valid option!")

print("Thank you for playing SCISSORS PAPER ROCKER!")