import elavator
import random

class People:
    destinationFloor = random.randint(0,100)

class Group(People):
    currentFloor = random.randint(0,100)
    numPeople = random.randint(1,12)
