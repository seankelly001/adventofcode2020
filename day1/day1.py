

import os

def main():
    
    print("===== Part 1 =====")
    answer1 = part1()
    print("answer is: {}".format(answer1))

    print("===== Part 2 =====")
    answer2 = part2()
    print("answer is: {}".format(answer2))

def part1():
    inputs = getNumInputs()
    numA, numB = get2Nums(inputs)
    answer = numA * numB
    return str(answer)

def part2():
    inputs = getNumInputs()
    numA, numB, numC = get3Nums(inputs)
    answer = numA * numB * numC
    return str(answer)

def getNumInputs():
    inputs = []
    path = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(path) as file:
        for line in file:
            inputs.append(int(line))
    return inputs

def get2Nums(inputs):

    for input_a in inputs:
        if input_a > 2020:
            continue
        for input_b in inputs:
            if input_b > 2020:
                continue
            if input_a + input_b == 2020:
                return input_a, input_b
    raise Exception("No numbers match 2020")

def get3Nums(inputs):

    for input_a in inputs:
        if input_a > 2020:
            continue
        for input_b in inputs:
            if input_b > 2020:
                continue
            for input_c in inputs:
                if input_c > 2020:
                    continue

                if input_a + input_b + input_c == 2020:
                    return input_a, input_b, input_c
    raise Exception("No numbers match 2020")


if __name__ == "__main__":
    main()
