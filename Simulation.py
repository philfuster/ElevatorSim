from Elevator import Elevator, Retail_Elevator,  Residential_Elevator_Lower, Residential_Elevator_Luxury, Office_Elevator_Lower, Office_Elevator_Luxury, Mechanical_Elevator, Observatory_Elevator
#from people import People, Group
#import queue

class Simulation:

	#elevators = []
	#elevators.append( Retail_Elevator )
	#elevators.append( Residential_Elevator_Lower )
	#elevators.append( Residential_Elevator_Luxury )
	#elevators.append( Office_Elevator_Lower )
	#elevators.append( Office_Elevator_Luxury )
	#elevators.append( Mechanical_Elevator )
	#elevators.append( Observatory_Elevator )
	#elevators.append( Key_Card_Elevator )

	AllWaitingList = [ [], [], [], [], [], [], [], [] ]
	AllWaitingPickUp = [ [], [], [], [], [], [], [], [] ]
	AllElevators = [ [], [], [], [], [], [], [], [] ]

	# Check from 7:00 to 9:00
	for moment in range( 0, 2400 ):

		#str_test = raw_input()

		#current, destination, people, request = str_test.split()

		request = 5

		WaitingList = AllWaitingList[ request ]
		WaitingPickup = AllWaitingPickUp[ request ]		# curent, destination, people
		Elevators = AllElevators[ request ]

		# DONT FORGET TO ADD IN
		#waitingGroup = ( current, destination, people )
		#WaitingList.append( waitingGroup )

		# Check all of the elevators
		for typeElevator in range( 0, 7 ):

			WaitingList = AllWaitingList[ typeElevator ]
			WaitingPickup = AllWaitingPickUp[ typeElevator ]
			Elevators = AllElevators[ typeElevator ]

			elevatorsLen = len( Elevators )

			# Have people get off at this floor
			for idx in range( 0, elevatorsLen ):

				particularElevator = Elevators[ idx ]

				# Avoid checking elevators that are empty				
				if particularElevator.holding == 0:

					# Update elevators that are empty, but have already been assigned somebody to pick up
					if len( WaitingPickup[ idx ] ) != 0:

						increment = WaitingPickup[ idx ][ 0 ] - WaitingPickup[ idx ][ 0 ]
						particularElevator.currentFloor -= abs( increment ) / increment

					continue

				# Update current floor
				if particularElevator.currentFloor < particularElevator.destinations[ 0 ][ 0 ]:

					particularElevator.currentFloor = particularElevator.currentFloor - 1
				else:

					particularElevator.currentFloor = particularElevator.currentFloor + 1

				# Simulate people getting off at this floor
				for group in range( len( particularElevator.destinations ) ):

					if particularElevator.destinations[ group ][ 0 ] == particularElevator.currentFloor:
						particularElevator.holding = particularElevator.holding - particularElevator.destinations[ group ][ 1 ]

						particularElevator.remove( ( particularElevator.destinations[ group ] ) )

			# Have people get on at this floor
			for idx in range( 0, elevatorsLen ):

				

			# Check if there are currently people waiting to be picked up that have not yet been assigned an elevator
			# This also takes care of empty elevators
			if len( WaitingList ) != 0:

				# Make empty elevators head move towards people that have been waiting the longest (i.e. first element of WaitingList)
				for idx in range( 0, elevatorsLen ):

					particularElevator = Elevators[ idx ]
					particularWaitingPickup = WaitingPickup[ idx ]

					# Avoid considering elevators that are already occupied, or headed towards somebody
					if len( particularElevator.destinations ) != 0 or len( WaitingPickup ) != 0:

						continue

					particularWaitingPickup.append( WaitingPickup[ 0 ] )

					increment = WaitingPickup[ 0 ][ 0 ] - WaitingPickup[ 0 ][ 1 ]
					particularElevator.currentFloor -= abs( increment ) / increment

					WaitingPickup.remove( WaitingPickup[ 0 ] )







	print "PROJECT COMPILED!"


