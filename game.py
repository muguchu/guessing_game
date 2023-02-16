#this program demos a guessing game
#game

#1.gets user name
player= input("Whats your name?")
print("Hello there"+ player +"!")

#generate a random number
from random import randint
number = randint(1,100)


counter= 0

#3.using a while loop
while counter <5:
    usernumber=eval(input("Enter a number:"))
    counter += 1

#Checks if usernumber is equal to nrandomly generated number.
    if usernumber < number:
        print("Your guess is too low.")
    elif usernumber > number:
        print("Your guess is too high.")
    elif usernumber==number:
        break

print("Game over.")

if usernumber == number:
    print("Correct.You win!")
else:
    print("The correct number is")
    print(number)



