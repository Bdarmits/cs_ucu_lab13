# Implements the Maze ADT using a 2-D array.
from arrays import Array2D
from lliststack import Stack

class Maze :
    # Define constants to represent contents of the maze cells.
    MAZE_WALL = " *"
    PATH_TOKEN = " x"
    TRIED_TOKEN = " o"

    # Creates a maze object with all cells marked as open.
    def __init__( self, num_rows, num_cols ):
        self._mazeCells = Array2D( num_rows, num_cols )
        self._startCell = None
        self._exitCell = None

    # Returns the number of rows in the maze.
    def num_rows( self ):
        return self._mazeCells.num_rows()

    # Returns the number of columns in the maze.
    def num_cols( self ):
        return self._mazeCells.num_cols()

    # Fills the indicated cell with a "wall" marker.
    def setWall( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._mazeCells[row, col] = self.MAZE_WALL

    # Sets the starting cell position.
    def setStart( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._startCell = _CellPosition( row, col )

    # Sets the exit cell position.
    def setExit( self, row, col ):
        assert row >= 0 and row < self.num_rows() and \
               col >= 0 and col < self.num_cols(), "Cell index out of range."
        self._exitCell = _CellPosition( row, col )

    # Attempts to solve the maze by finding a path from the starting cell
    # to the exit. Returns True if a path is found and False otherwise.
    def findPath( self ):
        """
        finds  path in a Maze and Returns True
        if no path it will return None
        """
        maze_stack = Stack()
        maze_stack.push(self._startCell)
        current_cell = self._startCell
        self._markPath(self._startCell.row, self._startCell.col)
        while not maze_stack.isEmpty():
            possible_moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

            current_cell.row = maze_stack.peek().row
            current_cell.col = maze_stack.peek().col

            self._markPath(current_cell.row, current_cell.col)

            moved = False
            for i, j in possible_moves:
                if self._validMove(current_cell.row + i, current_cell.col + j):
                    current_cell.row = current_cell.row + i
                    current_cell.col = current_cell.col + j
                    maze_stack.push(_CellPosition(current_cell.row, current_cell.col))
                    moved = True
                    break
            if moved:
                if self._exitFound(current_cell.row, current_cell.col):
                    self._markPath(current_cell.row, current_cell.col)
                    return True
                continue
            visited_cell = maze_stack.pop()
            self._markTried(visited_cell.row, visited_cell.col)

    # Resets maze by removing
    def reset( self ):
        for row in self.num_rows():
            for col in self.num_cols:
                if self._mazeCells[row, col] == self.PATH_TOKEN or self._mazeCells[row, col] == self.TRIED_TOKEN:
                    self._mazeCells[row, col] = None


    # Print a txt representation of  maze
    def draw( self ):
        for row in range(self.num_rows()):
            for col in range(self.num_cols()):
                if self._mazeCells[row, col] == None:
                    self._mazeCells[row, col] = "  "
                print(self._mazeCells[row, col], end="")
            print("\n")

    # Return True if move is valid
    def _validMove( self, row, col ):
        return row >= 0 and row < self.num_rows() \
               and col >= 0 and col < self.num_cols() \
               and self._mazeCells[row, col] is None

    # Helper method to determine if the exit was found.
    def _exitFound( self, row, col ):
        return row == self._exitCell.row and col == self._exitCell.col

    # Drops a "tried" token at the given cell.
    def _markTried( self, row, col ):
        self._mazeCells[row, col] = self.TRIED_TOKEN

    # Drops a "path" token at the given cell.
    def _markPath( self, row, col ):
        self._mazeCells[row, col] = self.PATH_TOKEN

# Private storage class for holding a cell position.
class _CellPosition( object ):
    def __init__( self, row, col ):
        self.row = row
        self.col = col
