import os
import math 

def main():
    print("===== Part 1 =====")
    tree_count = part1()
    print("Number of trees: {}".format(tree_count))

    print("===== Part 2 =====")
    answer = part2()
    print("Number of trees: {}".format(answer))

def part1():
    coordinates = getInputs()
    tree_count = traverse(coordinates, 3, 1)
    return str(tree_count)

def part2():
    coordinates = getInputs()
    slopes = [(1,1), (3,1), (5,1), (7,1), (1, 2)]
    tree_counts = []
    for slope in slopes:
        tree_count_2 = traverse(coordinates, slope[0], slope[1])
        tree_counts.append(tree_count_2)
    answer = math.prod(tree_counts)
    return str(answer)


def traverse(coordinates, slope_x, slope_y):
    x = 0
    y = 0
    max_y = len(coordinates)
    max_x = len(coordinates[y])
    tree_count = 0

    while(y < max_y):
        isTree = checkTree(coordinates, x, y)
        if isTree:
            tree_count += 1
        x = (x + slope_x) % max_x
        y += slope_y

    return tree_count

def checkTree(coordinates, x , y):
    #print("checking tree at (x,y) ({},{})".format(x,y))
    char = coordinates[y][x]
    if char == "#":
        return True
    if char == ".":
        return False
    raise Exception("unknown char: <{}>".format(char))

def getInputs():
    inputs = []
    path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(path) as file:
        for line in file:
            inputs.append(line.strip())
    return inputs

if __name__ == "__main__":
    main()