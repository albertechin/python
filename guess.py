import random

name = input("What is your name: ")

print("Hello " + name + ", I'm thinking of a number between 1 to 20!")
num = random.randint(1,20)

for i in range(6):
    guess = int(input("Take a guess: "))

    if(guess > num):
        print("Your guess was high!")
    elif(guess < num):
        print("Your guess was low!")
    else:
        break

if( guess == num):
    print("Great job " + name +  ",you guessed it right in " + str(i+1) + " guesses")
else:
    print("Nope, the number I was thinking of was "+ str(num))
