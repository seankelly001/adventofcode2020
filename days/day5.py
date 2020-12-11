from myutils import files

def main():

    print("===== Part 1 =====")
    highest_seat_id = part1()
    print("highest seat id: {}".format(highest_seat_id))
    
    print("===== Part 2 =====")
    missing_seat_id = part2()
    print("Missing seat id: {}".format(missing_seat_id))

def part1():
    inputs = files.getInputs("../inputs/day5-input.txt", strip=True)
    seat_ids = getSeatIDs(inputs)
    highest_seat_id = seat_ids[len(seat_ids)-1]
    return str(highest_seat_id)

def part2():
    inputs = files.getInputs("../inputs/day5-input.txt", strip=True)
    seat_ids = getSeatIDs(inputs)
    missing_seat_id = getMissingSeatID(seat_ids)
    return str(missing_seat_id)

def getSeatIDs(inputs):
    seat_ids = []
    for input in inputs:
        cnv = toBinaryString(input)
        row = binaryToDec(cnv[:7])
        col = binaryToDec(cnv[7:])
        seat_id = (row * 8) + col
        seat_ids.append(seat_id)
    return sorted(seat_ids)

def toBinaryString(str):
    cnv_str = str.replace("B", "1")
    cnv_str = cnv_str.replace("F", "0")
    cnv_str = cnv_str.replace("R", "1")
    cnv_str = cnv_str.replace("L", "0")
    return cnv_str

def binaryToDec(str):
    return int(str, 2)

def getMissingSeatID(seat_ids):

    for i in range(0, len(seat_ids) - 2):
        current_seat_id = seat_ids[i]
        next_seat_id = seat_ids[i+1]
        if(next_seat_id - current_seat_id == 2):
            return current_seat_id+1
    return -1

if __name__ == "__main__":
    main()