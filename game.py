from enum import Enum

class Direction(Enum):
    UP: 1
    DOWN: 2
    LEFT: 3
    RIGHT: 4

def updateMatrixPos(matrix, old_x, old_y, new_x, new_y):
    matrix[new_x][new_y] = matrix[old_x][old_y]
    # matrix[old_x][old_y] = <empty>

class Player:
    def __init__(self):
        self.name = None
        self.x = 0 # row # in the 2D matrix
        self.y = 0 # column # in the 2D matrix
        self.isAlive = True
        self.isShown = True
    
    def setPos(x, y):
        self.x = x
        sefl.y = y
    
    # direction: enum
    def isMovable(direction):
        result = True

        # if row/column out of bound, set to false
        if direction == Direction.UP.value:
            # things to do here
            pass
        elif direction == Direction.DOWN.value:
            # things to do here
            pass
        elif direction == Direction.LEFT.value:
            # things to do here
            pass
        elif direction == Direction.RIGHT.value:
            # things to do here
            pass
        else:
            result = False

        return result

    def move(direction):
        """
            1. Check if movable
            2. New pos processing
            3. Change the position in 2D Matrix
            4. Update class pos
        """
        if not self.isMovable(direction):
            print(f"Can't move {direction.name}")
            return
        
        # Change the code here
        new_x = self.x
        new_y = self.y
        # end change

        updateMatrixPos(matrix, self.x, self.y, new_x, new_y)
        self.setPos(new_x, new_y)

class Pacman(Player):
    pass

class Monster(Player):
    pass



