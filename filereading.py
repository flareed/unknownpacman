import os.path
import numpy

# Return a string


def readFile(path):
    """
    1. Check if file exists
    2. Read the file
    """
    if not os.path.exists(path):
        return False

    f = open(path, "r")  # open file in <path> in read mode
    str = f.read()

    return str


def printContent(str):
    # split the string by "\n" delimiter, returned a list of strings
    lines = str.splitlines()

    count = 1
    for line in lines:
        print(f"Line {count}: {line}")
        count += 1


def readALine(str):
    result = []
    temp_list = str.split()  # split by white space

    for i in range(0, len(temp_list)):
        result.append(int(temp_list[i]))

    return result


def processRead(str):
    lines = str.splitlines()  # split the string by "\n" delimiter

    """ First part: row count, column count """
    temp_list = lines[0].split()
    # int() to convert the char to number
    (row, column) = (int(temp_list[0]), int(temp_list[1]))

    """ Second part, the matrix """
    arr = []
    for i in range(1, len(lines) - 1):
        temp = readALine(lines[i])
        arr.append(temp)

    # print(arr)
    # transfer 1D array to 2D array (aka matrix)
    arr = numpy.array(arr).reshape((row, column))

    """ Third part, pacman pos """
    temp_list = lines[len(lines) - 1].split()
    # int() to convert the char to number
    (pos_x, pos_y) = (int(temp_list[0]), int(temp_list[1]))

    return (row, column), arr, (pos_x, pos_y)


path = "input.txt"


def testRead():
    lines = readFile(path)
    if lines == False:
        print("File does not exist")
        return

    print(processRead(lines))


if __name__ == "__main__":
    testRead()
