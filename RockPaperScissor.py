import random
i=True
while i==True:
    print()
    print("Rock\nPaper\nScissors \nexit")
    player = input("Enter your choice :")
    player1= player.capitalize()
    
    print()
    possible_action=["Rock","Paper","Scissors"]
    computer=random.choice(possible_action)

    if player1 == computer:
        print("____________________________________________")
        print("Tie!")
        print("____________________________________________")
        print()



    elif player1 == "Rock":
        if computer == "Paper":
            print("____________________________________________")
            print("You lose!", computer, "covers", player)
            print("____________________________________________")
            print()
        else:
            print("____________________________________________")
            print("You win!", player, "smashes", computer)
            print("____________________________________________")
            print()



    elif player1 == "Paper":
        if computer == "Scissors":
            print("____________________________________________")
            print("You lose!", computer, "cut", player)
            print("____________________________________________")
            print()
        else:
            print("____________________________________________")
            print("You win!", player, "covers", computer)
            print("____________________________________________")
            print()



    elif player1 == "Scissors":
        if computer == "Rock":
            print("____________________________________________")
            print("You lose...", computer, "smashes", player)
            print("____________________________________________")
            print()
        else:
            print("You win!", player, "cut", computer)
            print()
            


    elif  player1=="Exit":
        print("code exitted !!!!")
        i=False


    else:
        print("That's not a valid play. Check your spelling!")
        print()




# Output---------->>>>>>>>>
"""
Rock
Paper
Scissors 
exit
Enter your choice :rock

____________________________________________
You win! rock smashes Scissors
____________________________________________


Rock
Paper
Scissors 
exit
Enter your choice :paper

____________________________________________
You lose! Scissors cut paper
____________________________________________


Rock
Paper
Scissors 
exit
Enter your choice :scissor

That's not a valid play. Check your spelling!


Rock
Paper
Scissors 
exit
Enter your choice :scissors

____________________________________________
You lose... Rock smashes scissors
____________________________________________


Rock
Paper
Scissors 
exit
Enter your choice :exit

code exitted !!!!"""


