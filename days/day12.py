from myutils import files
import re
import math

#           N(270)
#           ^
#           |
# W(180) <- X -> E(0)
#           |
#           v
#           S(90)
bearings = {0: "E", 90: "S", 180: "W", 270: "N"}

def main():
    print("===== Part 1 =====")
    answer = part1()
    print("answer: {}".format(answer))

    print("===== Part 2 =====")
    answer = part2()
    print("answer: {}".format(answer))

def part1():
    actions = files.getInputs("../inputs/day12-input.txt", strip=True)
    #actions = files.getInputs("../inputs/test.txt", strip=True)
    east_pos, north_pos = getPosition(actions)
    print("east: {}, north: {}".format(east_pos, north_pos))
    manhatten_distance = calculateManhattanDistance(east_pos, north_pos)
    return str(manhatten_distance)

def part2():
    actions = files.getInputs("../inputs/day12-input.txt", strip=True)
    #actions = files.getInputs("../inputs/test.txt", strip=True)
    east_pos, north_pos = getPosition2(actions)
    print("east: {}, north: {}".format(east_pos, north_pos))
    manhatten_distance = calculateManhattanDistance(east_pos, north_pos)
    return str(manhatten_distance)



def getPosition2(actions):
    east, north = 0, 0
    waypoint_east, waypoint_north = 10, 1

    for action in actions:
        acc, num = parseAction(action)
        if acc == "F":
            east, north = goForwardWaypoint(east, north, waypoint_east, waypoint_north, num)
        elif acc == "N":
            waypoint_north += num
        elif acc == "S":
            waypoint_north += (num * -1)
        elif acc == "E":
            waypoint_east += num
        elif acc == "W":
            waypoint_east += (num * -1)
        elif acc in ["R", "L"]:
            waypoint_east, waypoint_north = rotateWaypoint(waypoint_east, waypoint_north, acc, num)
    return east, north


def calculateManhattanDistance(east, north):
    return abs(east) + abs(north)

def getPosition(actions):
    bearing, east, north = 0, 0, 0
    
    for action in actions:
        acc, num = parseAction(action)
        if acc == "F":
            go_east, go_north = forward(bearing, num)
            east += go_east
            north += go_north
        elif acc == "R":
            bearing = rotate(bearing, num)
        elif acc == "L":
            bearing = rotate(bearing, num * -1)
        elif acc in ["E","S","N","W"]:
            go_bearing = list(bearings.keys())[list(bearings.values()).index(acc)]
            go_east, go_north = forward(go_bearing, num)
            east += go_east
            north += go_north
    return east, north

def forward(bearing, amount):
    go_east = 0
    go_north = 0
    direction = bearings[bearing]
    if direction == "E":
        go_east += amount
    elif direction == "W":
        go_east -= amount
    elif direction == "N":
        go_north += amount
    elif direction == "S":
        go_north -= amount
    return go_east, go_north

def rotate(bearing, amount):
    bearing = (bearing + amount) % 360
    return bearing

def goForwardWaypoint(east, north, waypoint_east, waypoint_north, times):
    east = east + (waypoint_east * times)
    north = north + (waypoint_north * times)
    return east, north

def rotateWaypoint(waypoint_east, waypoint_north, direction, amount):
    rotations = math.floor(abs(amount / 90))
    for _ in range(rotations):
        # e = x
        # n = y
        # clockwise (x,y) = (y,-x)
        # counterclockwise (x,y) = (-y, x)
        e = waypoint_east
        n = waypoint_north
        if direction == "R":
            waypoint_east = n
            waypoint_north = e * -1
        elif direction == "L":
            waypoint_east = n * -1
            waypoint_north = e
        else:
            raise Exception("unknown direction")
    return waypoint_east, waypoint_north

def parseAction(action):
    acc = action[0]
    num = re.findall(r'\d+', action)[0]
    return acc, int(num)

if __name__ == "__main__":
    main()