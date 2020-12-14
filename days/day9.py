from myutils import files
from itertools import combinations

def main():
    print("===== Part 1 =====")
    answer = part1()
    print("answer: {}".format(answer))

    print("===== Part 2 =====")
    answer = part2()
    print("answer: {}".format(answer))

def part1():
    inputs = files.getNumInputs("../inputs/day9-input.txt")   
    #inputs = files.getNumInputs("../inputs/test.txt")   
    preamble_range = 25
    #preamble_range = 5

    for i in range(preamble_range, len(inputs)):
        preamble = inputs[i-preamble_range:i]
        if not isValidNumber(inputs[i], preamble):
            return str(inputs[i])

    return ""

def part2():
    return ""


def isValidNumber(num, nums):
    print("{}, {}".format(num, nums))
    if num in nums:
        return True
    for ix in combinations(nums,2):
        if sum(ix) == num:
            return True
    return False

if __name__ == "__main__":
    main()