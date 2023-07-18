'''We are going to wrte a program that generats 
a random number and asks the user to guess it.
IF the player guesses the hgher than the actual number,
the program displays "lower number please". 
Similarly if the user guess is too low, thr program 
disaplays "higher number please"
When the user guess the correct number, the program displays
the nuber of guesses the player used to arrive at the number '''

import random
ranNum = random.randint(1,100)
print(ranNum)
user = None
guesses = 0
while(user != ranNum):
    user = int(input("Enter your guess: "))
    guesses +=1
    if(user == ranNum):
        print("You guessed it Right")
    else:
        if(user>ranNum):
            print("You guessed it wrong! Enter a smaller Number")
        else:
            print("You guessed it wrong! Enter a larger Number")

print(f"You guessed the number in {guesses} guesses")
with open("highscore.txt","r") as f:
    highscore = int(f.read())

if(guesses<highscore):
    print("You have broken the highscore")
with open("highscore.txt","w") as f:
    f.write(str(guesses))
