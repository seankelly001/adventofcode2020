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
    invalidNumber = getInvalidNumber(inputs, preamble_range)
    return str(invalidNumber)

def part2():
    inputs = files.getNumInputs("../inputs/day9-input.txt")   
    #inputs = files.getNumInputs("../inputs/test.txt")   
    preamble_range = 25
    #preamble_range = 5
    invalidNumber = getInvalidNumber(inputs, preamble_range)
    contiguous_set = getContiguousSet(inputs, invalidNumber)
    print(contiguous_set)
    print(sorted(contiguous_set))
    contiguous_set = sorted(contiguous_set)
    answer = contiguous_set[0] + contiguous_set[len(contiguous_set)-1]
    return str(answer)

def getInvalidNumber(inputs, preamble_range):
    for i in range(preamble_range, len(inputs)):
        preamble = inputs[i-preamble_range:i]
        if not isValidNumber(inputs[i], preamble):
            return inputs[i]
    return -1

def isValidNumber(num, nums):
    if num in nums:
        return True
    for ix in combinations(nums,2):
        if sum(ix) == num:
            return True
    return False

def getContiguousSet(inputs, num):

    for i in range(len(inputs)):
        print("trying i: {}".format(i))
        contiguous_set = []
        for j in range(i, len(inputs)):   
            contiguous_set.append(inputs[j])
            count = sum(contiguous_set) 
            if count == num:
                return contiguous_set
            elif count > num:
                break
    return []


if __name__ == "__main__":
    main()