#import random module
import random
#Computer's choice
a=random.randint(0,2)
#include game images
rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_image=[rock,paper,scissors]
#Take user's input
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_image[choice])
print("Computer chose:")
print(game_image[a])
if choice>=3 or choice<0:
    print("You typed an invalid number. You Lose !")
elif choice==0 and a==2:
    print("You win!")
elif a>choice:
    print("You Lose!")
elif a==choice:
    print("It's a draw.")
elif a==0 and choice==2:
    print("You Win !!")
elif choice>a:
    print("You Win !!")
