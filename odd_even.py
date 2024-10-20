# odd or even game

import random
computer = random.randint(1,6)
def game():
        player = int(input("enter the number between 1 and 10:"))
        if player < 1 or player > 10:
                print("invalide number \n please try again ")
        else:
                print(f"you choose {player} and computer choose {computer} ")
                total = player + computer
        if total%2 == 0 :
                print(f"you win {total}")
        
        else:
                print("you loss")
                play=int(input("Do you want to try again Yes - 1, if No - 0: "))
                if play == 1:
                        game()
                else:
                        print("second chance")
try:
        game()   

except ZeroDivisionError:
    print(' cannot zero')