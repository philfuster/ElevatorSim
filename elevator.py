import random

class Elevator:

    id
    status = { "ready":True, "traveling":False}
    currentFloor = 1
    destinations = []
    floorAccess

    def __init__(self):
        self.id = None


    def getFloor(self):
        return self.currentFloor

    def setFloor(self, floor):
        self.currentFloor = floor




class Retail_Elevator(Elevator):
    status = "ready"
    floorAccess = range( 1, 6 )
    currentFloor = 1
    destinationFloor = 1

    def __init__(self):
        self.status = "ready"
        self.currentFloor = 1
        self.destinationFloor = 1




class Residential_Elevator_Lower(Elevator):

    id
    status = "ready"
    currentFloor = 1
    destinationFloor = 1
    floorAccess = range( 23, 40 )

    def __init__(self):
        self.id
        self.status = "ready"
        self.currentFloor = 1
        self.destinationFloor = 1

class Residential_Elevator_Luxury(Elevator):

    id
    status = "ready"
    currentFloor = 1
    destinationFloor = 1
    floorAccess = range( 63,80 )

    def __init__(self):
        self.id
        self.status = "ready"
        self.currentFloor = 1
        self.destinationFloor = 1


class Office_Elevator_Lower(Elevator):

    id
    status ="ready"
    currentFloor = 1
    destinationFloor = 1
    floorAccess
    
class Office_Elevator_Luxury(Elevator):

    id
    status ="ready"
    currentFloor = 1
    destinationFloor = 1
    floorAccess


class Mechanical_Elevator(Elevator):

    id
    status="ready"
    currentFloor = 1
    destinationFloor = 1
    floorAccess = range( 1, 81 )

    def __init__(self):
        self.id
        self.status = "ready"
        self.currentFloor = 1
        self.destinationFloor = 1

class Observatory_Elevator(Elevator):

    id
    status="ready"
    currentFloor = 1
    destinationFloor = 1
    floorAccess = range( 1, 81 )

    def __init__(self):
        self.id
        self.status = "ready"
        self.currentFloor = 1
        self.destinationFloor = 1
        
e1 = Retail_Elevator()

print "Status of retail elevator is", e1.status

e1.setFloor(2)

print e1.getFloor()



