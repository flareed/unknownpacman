import algorithm
import game_class
import graphic
import filereading

"""
    1. Read from file: DONE
    1.5 Store matrix in memory: DONE
    2. Open graphic UI
    3. Loop by turn:
        3.1 Monster/pacman turn to move
        3.2 Update the 2D matrix each turn
        3.3 Update graphic UI
        3.4 Check if game over or winning to exit loop
    4. 
"""


def main():
    a = game_class.Pacman()
    x1 = game_class.Monster()
    x2 = game_class.Monster()
    x3 = game_class.Monster()

    actor_list = []
    actor_list.append(a)
    actor_list.append(x1)
    actor_list.append(x2)
    actor_list.append(x3)

    print(actor_list)


main()
