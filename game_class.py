from enum import Enum


class Misc(Enum):
    BUFF_VAULE = 0
    BUFF_DURATION = 10000  # milisecond
    FOOD_VALUE = 100


class Color(Enum):
    BLACK = 0x0
    PURPLE = 0x800080
    ROYAL_BLUE = 0x4169E1


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


""" Player section """


class Player:
    def __init__(self):
        self.name = None
        self.x = 0  # row # in the 2D matrix
        self.y = 0  # column # in the 2D matrix
        self.isAlive = True
        self.isShown = True

    def setPos(self, x, y):
        self.x = x
        self.y = y

    # direction: enum
    def isMovable(self, direction):
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

    def move(self, direction):
        """
            1. Check if movable
            2. New pos processing
            3. Change the position in 2D Matrix
            4. Update class pos
        """
        if not self.isMovable(direction):
            # comment this line if needed
            print(f"Can't move {direction.name}")
            return

        """ Change the code here
        new_x = self.x
        new_y = self.y
        end change 
        """

        self.setPos(new_x, new_y)


class Pacman(Player):
    def __init__(self):
        super().__init__()
        isInvincible = False  # invincible: take no damage, can attack monsters


class Monster(Player):
    def __init__(self):
        super().__init__()
        TurnsBeforeRespawn = 0  # incase implementing super buff for pacman


""" Graphic section """


class Object:
    def __init__(self):
        self.isShown = True

    def hide():
        self.isShown = False

    def show():
        self.isShown = True


class Wall(Object):
    def __init__(self):
        super().__init__()
        self.wall_color = None
        self.wall_thickness = 3
        self.isTopOpen = True
        self.isBottomOpen = True
        self.isLeftOpen = True
        self.isRightOpen = True


class Food(Object):
    def __init__(self):
        super().__init__()
        self.score_value = Misc.FOOD_VALUE.value

    def printScoreValue(self):
        print(f"Food score value is: {self.score_value}")


class Buff_Food(Food):
    def __init__(self):
        super().__init__()
        self.score_value = Misc.BUFF_VAULE.value


class Tile():
    def __init__(self):
        # A tile has background. May have wall, food
        # For entity: we just draw the entity on top
        self.background_color = None
        self.wall = Wall()
        self.food = Food()
        
        self.wall.isShown = False
        self.food.isShown = False

    def showWall(self):
        self.wall.show()

    def hideWall(self):
        self.wall.hide()

    def showFood(self):
        self.food.show()
        
    def hideFood(self):
        self.food.hide()
