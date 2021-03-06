# Used to store and manage information related to an airline ticket agent.
class TicketAgent :
    # Creates a ticket agent object.
    def __init__( self, idNum ):
        self._idNum = idNum
        self._passenger = None
        self._stopTime = -1

    # Gets the ticket agent's id number.
    def idNum( self ):
        return self._idNum

    # Determines if the ticket agent is free to assist a passenger.
    def isFree( self ):
        return self._passenger is None

    # Determines if the ticket agent has finished helping the passenger.
    def isFinished( self, curTime ):
        return self._passenger is not None and self._stopTime == curTime

    # Indicates the ticket agent has begun assisting a passenger.
    def startService( self, passenger, stopTime ):
        self._passenger = passenger
        self._stopTime = stopTime

    # Indicates the ticket agent has finished helping the passenger.
    def stopService( self ):
        thePassenger = self._passenger
        self._passenger = None
        return thePassenger
