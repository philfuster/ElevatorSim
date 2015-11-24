from Elevator import Elevator, Retail_Elevator,  Residential_Elevator_Lower, Residential_Elevator_Luxury, Office_Elevator_Lower, Office_Elevator_Luxury, Mechanical_Elevator, Observatory_Elevator, Key_Card_Elevator
#from people import People, Group
#import queue

class Simulation:

	AllWaitingList = [ [], [], [], [], [], [], [], [] ]
	AllWaitingPickUp = [ [], [], [], [], [], [], [], [] ]
	AllElevators = [ [], [], [], [], [], [], [], [] ]

	cntTime = [ 0, 0, 0, 0, 0, 0, 0, 0]
	cntTrips = [ 0, 0, 0, 0, 0, 0, 0, 0]
	maxTime = [ 0, 0, 0, 0, 0, 0, 0, 0]

	print "Simulation begins here"

	for it in range( 0, 11 ):
		AllElevators[ 0 ].append( Key_Card_Elevator )
		AllWaitingPickUp[ 0 ].append( [] )

	for it in range( 0, 4 ):
		AllElevators[ 1 ].append( Retail_Elevator )
		AllWaitingPickUp[ 1 ].append( [] )

	for it in range( 0, 7 ):
		AllElevators[ 2 ].append( Office_Elevator_Lower )
		AllWaitingPickUp[ 2 ].append( [] )

	for it in range( 0, 3 ):
		AllElevators[ 3 ].append( Residential_Elevator_Lower )
		AllWaitingPickUp[ 3 ].append( [] )

	for it in range( 0, 7 ):
		AllElevators[ 4 ].append( Office_Elevator_Luxury )
		AllWaitingPickUp[ 4 ].append( [] )

	for it in range( 0, 2 ):
		AllElevators[ 5 ].append( Residential_Elevator_Luxury )
		AllWaitingPickUp[ 5 ].append( [] )

	for it in range( 0, 2 ):
		AllElevators[ 6 ].append( Observatory_Elevator )
		AllWaitingPickUp[ 6 ].append( [] )

	for it in range( 0, 4 ):
		AllElevators[ 7 ].append( Mechanical_Elevator )
		AllWaitingPickUp[ 7 ].append( [] )

	print len( AllWaitingPickUp[ 7 ] )

	flag = False
	# Check from 7:00 to 10:00
	for moment in range( 0, 1080 ):

		if flag == False:

			print "banter"
			#str_test = raw_input()

			#tim, current, destination, people, request = str_test.split()

		else:

			flag = False

		#if tim != moment:

			#flag = True
			#continue

		request = 5



		WaitingList = AllWaitingList[ request ]
		WaitingPickup = AllWaitingPickUp[ request ]		# curent, destination, people
		Elevators = AllElevators[ request ]

		# DONT FORGET TO ADD IN
		#waitingGroup = ( tim, current, destination, people )
		#WaitingList.append( waitingGroup )

		# Check all of the elevators
		for typeElevator in range( 0, 8 ):

			print "Checking Elevator "  + `typeElevator`
			WaitingList = AllWaitingList[ typeElevator ]
			WaitingPickup = AllWaitingPickUp[ typeElevator ]
			Elevators = AllElevators[ typeElevator ]

			elevatorsLen = len( Elevators )

			# Have people get off at this floor
			for idx in range( 0, elevatorsLen ):

				particularElevator = Elevators[ idx ]
				particularWaitingPickup = WaitingPickup[ idx ]

				# Avoid checking elevators that are empty				
				if particularElevator.holding == 0:

					# Update elevators that are empty, but have already been assigned somebody to pick up
					if len( WaitingPickup[ idx ] ) > 0:

						increment = particularWaitingPickup[ 0 ] - particularWaitingPickup[ 1 ]
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

						particularElevator.doorsOpen = True

			# Have people get on at this floor
			for idx in range( 0, elevatorsLen ):

				particularElevator = Elevators[ idx ]
				particularWaitingPickup = WaitingPickup[ idx ]

				# Check if the elevator can still carry more people, and if the elevator open
				if particularElevator.holding == 12 or particularElevator.doorsOpen == False:

					continue

				# Check if the open elevator will pickup anybody on this floor
				for group in range( 0, len( WaitingList ) ):

					particularGroup = WaitingList[ group ]

					# Check if elevator is currently on a floor with people waiting to be picked up
					if particularElevator.currentFloor != particularGroup[ 0 ]:

						continue

					if len( particularElevator.destinations ) != 0:

						dir1 = particularElevator.currentFloor - particularElevator.destinations[ 0 ][ 0 ]
						dir2 = particularGroup[ 0 ] - particularGroup[ 1 ]

						if dir1 != dir2:

							continue

					willGetOn = min( particularGroup[ 2 ], 12 - particularElevator.holding )
					stillWaiting = particularGroup[ 2 ] - willGetOn

					particularElevator.holding += willGetOn
					particularElevator.destinations.append( ( particularGroup[ 1 ], willGetOn ) )

					addTime = 10 * ( moment - particularGroup[ 0 ] + abs( particularGroup[ 1 ] - particularGroup[ 2 ] ) )

					cntTime[ idx ] += addTime
					cntTrips[ idx ] += 1
					maxTime[ idx ] = max( maxTime[ idx ], addTime )

					if stillWaiting == 0:

						WaitingList[ idx ].remove( particularGroup )

					else:

						particularGroup[ 2 ] = stillWaiting

					if particularElevator.holding == 12:

						break

			# Check if there are currently people waiting to be picked up that have not yet been assigned an elevator
			# This also takes care of empty elevators
			if len( WaitingList ) != 0:

				# Make empty elevators head move towards people that have been waiting the longest (i.e. first element of WaitingList)
				for idx in range( 0, elevatorsLen ):

					particularElevator = Elevators[ idx ]
					particularWaitingPickup = WaitingPickup[ idx ]

					# Avoid considering elevators that are already occupied, or headed towards somebody
					if len( particularElevator.destinations ) != 0 or len( particularWaitingPickup ) != 0:

						continue

					nextPickUp = -1

					# Check to see if there are people waiting to be picked up, that have not yet been assigned an elevator
					for PickUpIdx in range( 0, WaitingList ):

						takenCareOf = False

						for takenCareOfIdx in range( 0, len( Elevators ) ):

							if WaitingPickup[ takenCareOfIdx ][ 0 ] == WaitingList[ PickUpIdx ]:

								takenCareOf = True
								break

						if takenCareOf == True:

							continue

						nextPickUp = PickUpIdx
						break

					# If there are no people waiting to be picked up, or all of them have already been assigned an elevator
					if nextPickUp == -1:

						break

					particularWaitingPickup.append( WaitingList[ nextPickUp ] )

					increment = WaitingPickup[ 0 ][ 0 ] - WaitingPickup[ 0 ][ 1 ]
					particularElevator.currentFloor -= abs( increment ) / increment

					doorsOpen = False

	print cntTime
	print cntTrips
	print maxTime





	print "PROJECT COMPILED!"


