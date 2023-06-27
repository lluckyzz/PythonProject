import random
userCount=0
compCount=0
roundCount=1
i=0
while i<5:
    print("______________________________________________")
    print("___________________Round",roundCount,"___________________")
    print()
    print("Rock\nPaper\nScissors")
    player = input("Enter your choice :")
    player1= player.capitalize()

    
    print()
    possible_action=["Rock","Paper","Scissors"]
    computer=random.choice(possible_action)

    if player1 == computer:
        print("->> Tie!")



    elif player1 == "Rock":
        if computer == "Paper":
            compCount+=1
            print("->> Computer's point ,", computer, "covers", player)
        else:
            userCount+=1
            print("->> Your Point , ", player, "smashes", computer)




    elif player1 == "Paper":
        if computer == "Scissors":
            compCount+=1
            print("->> Computer's point , ", computer, "cut", player)
        else:
            userCount+=1
            print("->> Your Point , ", player, "covers", computer)         



    elif player1 == "Scissors":
        if computer == "Rock":
            compCount+=1
            print("->> Computer's point ,", computer, "smashes", player)
        else:
            userCount+=1            
            print("->> Your Point , ", player, "cut", computer)        



    else:
        print("That's not a valid play. Check your spelling!\n   and play again")
        roundCount-=1
        i-=1
    i+=1
    roundCount+=1
print("_____________________________________________")
print()

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
______________________________________________
___________________Round 1 ___________________

Rock
Paper
Scissors
Enter your choice :rock

->> Your Point ,  rock smashes Scissors
______________________________________________
___________________Round 2 ___________________

Rock
Paper
Scissors
Enter your choice :paper

->> Computer's point ,  Scissors cut paper
______________________________________________
___________________Round 3 ___________________

Rock
Paper
Scissors
Enter your choice :scissors

->> Your Point ,  scissors cut Paper
______________________________________________
___________________Round 4 ___________________

Rock
Paper
Scissors
Enter your choice :rock

->> Tie!
______________________________________________
___________________Round 5 ___________________

Rock
Paper
Scissors
Enter your choice :paper

->> Your Point ,  paper covers Rock
_____________________________________________

 ______________________________
|         Point Table          |
|______________________________|
|Your point       :  3         |
|Computer's point :  1         |
|______________________________|

Conguratulation!!!!!!!  You win .

"""


