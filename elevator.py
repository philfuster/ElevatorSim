import random
import simulation

class Elevator:

    id
    status = { "ready":True, "traveling":False}
    currentFloor = 1
    destinations = []

    #floorAccess

    def __init__(self):
        self.id = None


    def getFloor(self):
        return self.currentFloor

    def setFloor(self, floor):
        self.currentFloor = floor




class Retail_Elevator(Elevator):
    status = "ready"
    #floorAccess
    currentFloor = 1
    destinationFloor = 1

    def __init__(self):
        self.status = "ready"
        self.currentFloor = 1
        self.destinationFloor = 1




class Residential_Elevator(Elevator):

    id
    status = "ready"
    currentFloor = 1
    destinationFloor = 1
    #floorAccess

    def __init__(self):
        self.id
        self.status = "ready"
        self.currentFloor = 1
        self.destinationFloor = 1



class Office_Elevator(Elevator):

    id
    status ="ready"
    currentFloor = 1
    destinationFloor = 1
    #floorAccess


class Mechanical_Elevator(Elevator):

    id
    status="ready"
    currentFloor = 1
    destinationFloor = 1
    #floorAccess

    def __init__(self):
        self.id
        self.status = "ready"
        self.currentFloor = 1
        self.destinationFloor = 1





e1 = Retail_Elevator()

print "Status of retail elevator is", e1.status

e1.setFloor(2)

print e1.getFloor()



