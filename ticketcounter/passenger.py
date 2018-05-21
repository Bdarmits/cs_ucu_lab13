# Used to store and manage information related to an airline passenger.
class Passenger :
    # Creates a passenger object.
    def __init__( self, idNum, arrivalTime ):
        self._idNum = idNum
        self._arrivalTime = arrivalTime

    # Gets the passenger's id numberself.
    def idNum( self ) :
        return self._idNum

    # Gets the passenger's arrival time.
    def timeArrived( self ) :
        return self._arrivalTime

