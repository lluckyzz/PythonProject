import random
userCount=0
compCount=0
roundCount=1
i=0
while i<5:
    print("_______________________________________")
    print("_______________Round ",roundCount,"_______________")
    print()
    print("Rock\nPaper\nScissors")
    player = input("Enter your choice :")
    player1= player.capitalize()

    
    print()
    possible_action=["Rock","Paper","Scissors"]
    computer=random.choice(possible_action)

    if player1 == computer:
        print("-> Tie!")



    elif player1 == "Rock":
        if computer == "Paper":
            compCount+=1
            print("-> Computer's point ,", computer, "covers", player)
        else:
            userCount+=1
            print("-> Your Point , ", player, "smashes", computer)




    elif player1 == "Paper":
        if computer == "Scissors":
            compCount+=1
            print("-> Computer's point , ", computer, "cut", player)
        else:
            userCount+=1
            print("-> Your Point , ", player, "covers", computer)         



    elif player1 == "Scissors":
        if computer == "Rock":
            compCount+=1
            print("-> Computer's point ,", computer, "smashes", player)
        else:
            userCount+=1            
            print("-> Your Point , ", player, "cut", computer)        



    else:
        print("-> That's not a valid play. Check your spelling!\n   and play again")
        roundCount-=1
        i-=1
    i+=1
    roundCount+=1


print(" ______________________________")
print("|         Point Table          |")
print("|______________________________|")
print("|Your point       : ",userCount,"        |")
print("|Computer's point : ",compCount,"        |")
print("|______________________________|")
print()
if(userCount<compCount):
    print("You lose , better luck next time ")
elif(userCount>compCount):
    print("Conguratulation!!!!!!!  You win .")
else:
    print("Tie !!!!")




# Output---------->>>>>>>>>
"""
_______________________________________
_______________Round  1 _______________

Rock
Paper
Scissors
Enter your choice :rock

-> Your Point ,  rock smashes Scissors
_______________________________________
_______________Round  2 _______________

Rock
Paper
Scissors
Enter your choice :paper

-> Computer's point ,  Scissors cut paper
_______________________________________
_______________Round  3 _______________

Rock
Paper
Scissors
Enter your choice :scissors

-> Tie!
_______________________________________
_______________Round  4 _______________

Rock
Paper
Scissors
Enter your choice :rock

-> Tie!
_______________________________________
_______________Round  5 _______________

Rock
Paper
Scissors
Enter your choice :paper

-> Your Point ,  paper covers Rock
 ______________________________
|         Point Table          |
|______________________________|
|Your point       :  2         |
|Computer's point :  1         |
|______________________________|

Conguratulation!!!!!!!  You win ."""


