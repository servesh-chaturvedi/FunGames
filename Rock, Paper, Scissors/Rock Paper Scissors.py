import random
import time
options={1:"rock", 2:"paper", 3: "scissors"}    #build list
try:
    again="y"
    while(again == "y"):
        player=int(input("Enter:\n 1 for Rock\n 2 for Paper\n 3 for Scissors\n"))   #take player input
        print("You entered:", options[player])
        
        comp=random.randint (1, 3)                                                  #take computer input
        print("Computer picked:", options[comp])
        
        score=player-comp
        
        if score in (-2,1):
            print("You win! :)")
        elif score in (-1,2):
            print("Computer wins :(")
        else:
            print("Tie")
            
        again=input("Do you want to play again?? \n Press y to continue \n Any other key to exit \n")
        if again != "y":
            print("Thanks for playing!!!")
            time.sleep(1)
        
except:                                         #input validation
    print("Input invalid, program will exit")
    time.sleep(1)
