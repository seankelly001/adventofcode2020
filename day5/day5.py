import os
def main():

    inputs = getInputs()
    print("===== Part 1 =====")
    seat_ids = []
    for input in inputs:
        cnv = toBinaryString(input)
        row = binaryToDec(cnv[:7])
        col = binaryToDec(cnv[7:])
        seat_id = (row * 8) + col
        seat_ids.append(seat_id)

    seat_ids = sorted(seat_ids)
    highest_seat_id = seat_ids[len(seat_ids)-1]
    print("highest seat id: {}".format(highest_seat_id))
    
    print("===== Part 2 =====")
    missing_seat_id = getMissingSeatID(seat_ids)
    print("Missing seat id: {}".format(missing_seat_id))

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
        next_next_seat_id = seat_ids[i+2]
        print("---")
        print(current_seat_id)
        print(next_seat_id)
        print("---")
        if(next_seat_id - current_seat_id == 2):
            return current_seat_id+1
    return -1

def getInputs():
    inputs = []
    path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(path) as file:
        for line in file:
            inputs.append(line.strip())
    return inputs

if __name__ == "__main__":
    main()