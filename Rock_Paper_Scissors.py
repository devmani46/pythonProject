import random

def game(comp,you):
    if comp==you:
        return None
    elif comp == "scissor":
        if you == "paper":
            return False
        elif you == "rock":
            return True
    elif comp == "paper":
        if you == "rock":
            return False
        elif you == "scissor":
            return True     
    elif comp == "rock":
        if you == "scissor":
            return False
        elif you == "paper":
            return True  

r=random.randint(1,3)
if r==1:
    comp="scissor"
elif r==2:
    comp="paper"
else:
    comp="rock"
you= input("Your turn: Rock Paper or scissor : ")
a = game(comp,you)
print("Computer's turn: Rock Paper or scissor")

print(f"Computer chose : {comp}")
print(f"You chose : {you}")

if a==None:
    print("Draw")
elif a:
    print("You win!")
else:
    print("You Lose!")