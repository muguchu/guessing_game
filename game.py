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
    usernumber=eval(input("Pick a number of your choice between 1 and 100!"))

#4.checks if users input is equal to random no