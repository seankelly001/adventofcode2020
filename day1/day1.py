import os

def main():
    inputs = getNumInputs()

    print("===== Part 1 =====")
    numA, numB = get2Nums(inputs)
    print("a: {}, b: {}".format(numA, numB))
    answer1 = numA * numB
    print("answer is: {}".format(answer1))

    print("===== Part 2 =====")
    numA, numB, numC = get3Nums(inputs)
    print("a: {}, b: {}, c: {}".format(numA, numB, numC))
    answer2 = numA * numB * numC
    print("answer is: {}".format(answer2))


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
