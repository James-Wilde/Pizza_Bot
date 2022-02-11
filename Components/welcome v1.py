# Pizza bot program
import random
from random import randint

#List of random names
names = ["James", "Mark", "John", "Pheobe", "Sally", "Michael", "Denise", "Ellen", "Bob", "Joe"]

num = randint(0,9)

name = (names[num])

print("*** Welcome to Dream Pizza ***")
print("*** My name is",name,"***")
print("*** I will be here to help you order your delicious Dream Pizza ***")