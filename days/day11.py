from myutils import files

def main():
    print("===== Part 1 =====")
    answer = part1()
    print("answer: {}".format(answer))

    print("===== Part 2 =====")
    answer = part2()
    print("answer: {}".format(answer))

def part1():
    floor = files.getInputs("../inputs/day11-input.txt", strip=True)
    floor = createFloor(floor)
    while True:
        floor_2 = fillSeats(floor)
        if floor == floor_2:
            break
        floor = floor_2
    filled_seat_count = countFilledSeats(floor)
    return str(filled_seat_count)

def part2():
    floor = files.getInputs("../inputs/day11-input.txt", strip=True)
    floor = createFloor(floor)
    while True:
        floor_2 = fillSeats2(floor)
        if floor == floor_2:
            break
        floor = floor_2
    filled_seat_count = countFilledSeats(floor)
    return str(filled_seat_count)

def createFloor(floor):
    new_floor = []
    for row in floor:
        new_floor.append(list(row))
    return new_floor

def printFloor(floor):
    for l in floor:
        print(l)

def countFilledSeats(floor):
    filled_seat_count = 0
    for row in floor:
        filled_seat_count += row.count("#")
    return filled_seat_count

def fillSeats(floor):
    new_floor = []
    for i in range(len(floor)):
        row = floor[i]
        new_row = []
        for j in range(len(row)):
            if row[j] == "L" and getNumAdjacentSeats(floor, i, j) == 0:
                new_row.append("#")
            elif row[j] == "#" and getNumAdjacentSeats(floor, i, j) >= 4:
                new_row.append("L")
            else:
                new_row.append(row[j])
        new_floor.append(new_row)
    return new_floor
            
def getNumAdjacentSeats(floor, i, j):
    # ---
    # -X-
    # ---
    num_adjacent = 0
    for x in range(i-1,i+2):
        for y in range(j-1,j+2):
            if checkSeatType(floor, "#", x, y):
                num_adjacent += 1
    if checkSeatType(floor, "#", i, j):
        num_adjacent -= 1
    return num_adjacent

def checkSeatType(floor, seat_type, x, y):
    if x < 0 or y < 0 or x >= len(floor) or y >= len(floor[0]):
        return False
    seat = floor[x][y]
    if seat == seat_type:
        return True
    else:
        return False

def fillSeats2(floor):
    new_floor = []
    for i in range(len(floor)):
        row = floor[i]
        new_row = []
        for j in range(len(row)):
            if row[j] == "L" and getNumVisibleSeats(floor, i, j) == 0:
                new_row.append("#")
            elif row[j] == "#" and getNumVisibleSeats(floor, i, j) >= 5:
                new_row.append("L")
            else:
                new_row.append(row[j])
        new_floor.append(new_row)
    return new_floor

def getNumVisibleSeats(floor, i, j):

    #\^/
    #<X>
    #/v\
    num_visible = 0
    for x_slope in range(-1,2):
        for y_slope in range(-1,2):
            if x_slope == 0 and y_slope == 0:
                continue
            a,b = i,j
            while a >= 0 and a <= len(floor) and b >= 0 and b <= len(floor[0]):            
                if a == i and b == j:
                    a += x_slope
                    b += y_slope
                    continue
                if checkSeatType(floor, "#", a, b):
                    #print("visible for (i,j) ({},{}), (a,b) ({},{}), (x,y) ({},{})".format(i,j,a,b,x_slope,y_slope))
                    num_visible += 1
                    break
                if checkSeatType(floor, "L", a, b):
                    #print("visible for (i,j) ({},{}), (a,b) ({},{}), (x,y) ({},{})".format(i,j,a,b,x_slope,y_slope))
                    break
                a += x_slope
                b += y_slope
    return num_visible
        
if __name__ == "__main__":
    main()
