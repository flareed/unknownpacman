import os.path

path = "input.txt"

# Return a string
def readFile(path):
    """
    1. Check if file exists
    2. Read the file
    """
    if not os.path.exists(path):
        return False

    f = open(path, "r") # open file in <path> in read mode
    str = f.read()

    return str

def printContent(str):
    lines = str.splitlines() # split the string by "\n" delimiter

    count = 1
    for line in lines:
        print(f"Line {count}: {line}")
        count += 1

def processRead(str):
    lines = str.splitlines() # split the string by "\n" delimiter
    (row, column) = lines[0].split()

    # From line 2 to the line before last
    for i in range(1, len(lines) - 1):
        # things to do here
        pass

    (pos_x, pos_y) = lines[len(lines) - 1].split()
    
def testRead():
    lines = readFile(path)
    if lines == False:
        print("File does not exist")
        return
    printContent(lines)

#line = "0, 6"
#(row, column) = line.split()
#print(row, column)