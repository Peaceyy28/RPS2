import sys
import random
from enum import Enum


def play_rps():
  class RPS(Enum):
    ROCK = 1
    PAPER =2
    SCISSORS =3


playagain = True

while playagain:
     print("")
     playerchoice = input(
        "Enter...\n1 for rock,\n2 for Paper, or \n3 for scissors:\n\n")

     if playerchoice not in ["1","2", "3"]
        print("you must enter 1,2,or 3")
        return play_rps()
    
     player = int(playerchoice)

     if player < 1 or player > 3:
          sys.exit("you must eneter 1, 2, or 3.")
   
     computerchoice = random.choice("123")
   
     computer = int(computerchoice)
   
print("\nYou chose " + playerchoice + ".")
print("Python chose " + computerchoice + ".\n")

if player == 1 and computer == 3: 
  print("🎉You win!")
elif player == 2 and computer == 1:
    print("🎉you win!")
elif player ==3 and computer == 2:
    print("🎉you win!")
elif player == computer:
    print("😑tie game1")
else: 
    print("😒Python wins!") 
    
    print("\nplay again?")
    
    while True:
            playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n")
            if playagain.lower() not in ["y", "q"]:
               "continue"
            else:
                break
            
    if playagain.lower("") == "y":
       return play_rps()
    else:
         print("\n🎉🎉🎉🎉")
         print("Thank you for playing!\n")
         playagain = False
         
sys.exit("Bye 👋🏾")