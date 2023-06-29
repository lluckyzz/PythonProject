import random

def rock_paper_scissors_game():
    userCount = 0
    compCount = 0
    roundCount = 1
    i = 0

    while i < 5:
        print("______________________________________________")
        print("___________________Round", roundCount, "___________________")
        print()
        print("Rock\nPaper\nScissors")
        player = input("Enter your choice: ")
        player1 = player.capitalize()

        print()
        possible_action = ["Rock", "Paper", "Scissor"]
        computer = random.choice(possible_action)

        if player1 == computer:
            print("->> Tie!")
        elif player1 == "Rock":
            if computer == "Paper":
                compCount += 1
                print("->> Computer's point, ", computer, "covers", player)
            else:
                userCount += 1
                print("->> Your Point, ", player, "smashes", computer)
        elif player1 == "Paper":
            if computer == "Scissor":
                compCount += 1
                print("->> Computer's point, ", computer, "cut", player)
            else:
                userCount += 1
                print("->> Your Point, ", player, "covers", computer)
        elif player1 == "Scissor":
            if computer == "Rock":
                compCount += 1
                print("->> Computer's point, ", computer, "smashes", player)
            else:
                userCount += 1
                print("->> Your Point, ", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!\n   and play again")
            roundCount -= 1
            i -= 1

        i += 1
        roundCount += 1

    print("_____________________________________________")
    print()
    print(" ______________________________")
    print("|         Point Table          |")
    print("|______________________________|")
    print("|Your point       :", userCount, "         |")
    print("|Computer's point :", compCount, "         |")
    print("|______________________________|")
    print()

    if userCount < compCount:
        print("You lose, better luck next time!")
    elif userCount > compCount:
        print("Congratulations! You win.")
    else:
        print("It's a tie!")

# Call the function to start the game
rock_paper_scissors_game()

j=1

while j==1:
    print()
    n=input("press 1 to play again , else press any key to exit!! :")
    if n!="1":
        j=0
        print()
        print("exitted!!!!!!!")
        print()
    else:
        print()
        rock_paper_scissors_game()

# Output --->>>>
"""
______________________________________________
___________________Round 1 ___________________

Rock
Paper
Scissors
Enter your choice: rock

->> Your Point,  rock smashes Scissor
______________________________________________
___________________Round 2 ___________________

Rock
Paper
Scissors
Enter your choice: paper 

->> Computer's point,  Scissor cut paper
______________________________________________
___________________Round 3 ___________________

Rock
Paper
Scissors
Enter your choice: scissor

->> Tie!
______________________________________________
___________________Round 4 ___________________

Rock
Paper
Scissors
Enter your choice: rock

->> Computer's point,  Paper covers rock
______________________________________________
___________________Round 5 ___________________

Rock
Paper
Scissors
Enter your choice: paper

->> Tie!
_____________________________________________

 ______________________________
|         Point Table          |
|______________________________|
|Your point       : 1          |
|Computer's point : 2          |
|______________________________|

You lose, better luck next time!

press 1 to play again , else press any key to exit!! :1

______________________________________________
___________________Round 1 ___________________

Rock
Paper
Scissors
Enter your choice: rock

->> Computer's point,  Paper covers rock
______________________________________________
___________________Round 2 ___________________

Rock
Paper
Scissors
Enter your choice: paper

->> Computer's point,  Scissor cut paper
______________________________________________
___________________Round 3 ___________________

Rock
Paper
Scissors
Enter your choice: scissor

->> Tie!
______________________________________________
___________________Round 4 ___________________

Rock
Paper
Scissors
Enter your choice: rock

->> Computer's point,  Paper covers rock
______________________________________________
___________________Round 5 ___________________

Rock
Paper
Scissors
Enter your choice: paper

->> Your Point,  paper covers Rock
_____________________________________________

 ______________________________
|         Point Table          |
|______________________________|
|Your point       : 1          |
|Computer's point : 3          |
|______________________________|

You lose, better luck next time!

press 1 to play again , else press any key to exit!! :as

exitted!!!!!!!

"""


