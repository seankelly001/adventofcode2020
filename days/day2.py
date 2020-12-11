import re
from myutils import files

def main():
    print("===== Part 1 =====")
    valid_count = part1()
    print("Numer of valid passwords: {}".format(valid_count))

    print("===== Part 2 =====")
    valid_count = part2()
    print("Numer of valid passwords: {}".format(valid_count))

def part1():
    inputs = files.getInputs("../inputs/day2-input.txt")
    valid_count = 0
    for input in inputs:
        isValidPassword = checkValidPassword1(input)
        if isValidPassword:
            valid_count+=1
    return str(valid_count)

def part2():
    inputs = files.getInputs("../inputs/day2-input.txt")
    valid_count = 0
    for input in inputs:
        isValidPassword = checkValidPassword2(input)
        if isValidPassword:
            valid_count+=1
    return str(valid_count)

def checkValidPassword1(input):
    #<int>-<int> <char>: password
    parts = input.split()
    minRange, maxRange = getNums(parts[0])
    password_char = parts[1].replace(":", "")
    password = parts[2]
    password_char_count = password.count(password_char)
    return (password_char_count >= minRange) & (password_char_count <= maxRange)

def checkValidPassword2(input):
    #<int>-<int> <char>: password
    parts = input.split()
    pos1, pos2 = getNums(parts[0])
    password_char = parts[1].replace(":", "")
    password = parts[2]

    #XOR
    return (password[pos1-1] == password_char) != (password[pos2-1] == password_char)

def getNums(part):
    ranges = part.split("-")
    return int(ranges[0]), int(ranges[1])

if __name__ == "__main__":
    main()