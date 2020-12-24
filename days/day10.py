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
    #adapters = files.getNumInputs("../inputs/day10-input.txt")   
    adapters = files.getNumInputs("../inputs/test.txt") 
    adapters.sort()
    adapters.insert(0, 0)
    adapters.append(adapters[-1]+3)

    print(adapters)
    diff1 = 0
    diff3 = 0
    for i in range(len(adapters)-1):
        first = adapters[i]
        second = adapters[i+1]
        diff = second - first
        if diff == 1:
            diff1 += 1
        elif diff == 3:
            diff3 +=1
        else:
            raise("Unknown joltage difference: {}".format(diff))
    
    return str(diff1 * diff3)

def part2():
    #adapters = files.getNumInputs("../inputs/day10-input.txt")   
    adapters = files.getNumInputs("../inputs/test.txt") 
    adapters.sort()
    adapters.insert(0, 0)
    adapters.append(adapters[-1]+3)

    visited_adapters = []
    for i in range(len(adapters)):
        
    return ""


if __name__ == "__main__":
    main()