from myutils import files

def main():

    print("===== Part 1 =====")
    answer = part1()
    print("answer: {}".format(answer))

    print("===== Part 2 =====")
    answer = part2()
    print("answer: {}".format(answer))

def part1():

    inputs = files.getInputs("../inputs/day6-input.txt")
    groups = getGroupsAsString(inputs)
    sum_counts = 0

    for group in groups:
        stripped_group = removeNonUnique(group)
        sum_counts += len(stripped_group)

    return str(sum_counts)

def part2():

    inputs = files.getInputs("../inputs/day6-input.txt")
    groups = getGroups(inputs)
    sum_counts = 0
    for group in groups:
        common = getCommon(group)
        sum_counts += len(common)
    return str(sum_counts)

def getGroups(inputs):
    groups = []
    groups_index = 0
    for line in inputs:
        if line.isspace():
            groups_index += 1
            continue
        if groups_index >= len(groups):
            groups.append([line.strip()])
        else:
            groups[groups_index].append(line.strip())
    return groups

def getGroupsAsString(inputs):
    groups = []
    groups_index = 0
    for line in inputs:
        if line.isspace():
            groups_index += 1
            continue
        if groups_index >= len(groups):
            groups.append(line.strip())
        else:
            groups[groups_index] = groups[groups_index] + line.strip()
    return groups

def removeNonUnique(s):
    s_array =  sorted("".join(set(s)))
    return "".join(str(x) for x in s_array)

def getCommon(sx):

    common = ""
    for s in sx:
        if common == "":
            common = set(s)
        else:
            common = common.intersection(set(s))

    return "".join(common)

if __name__ == "__main__":
    main()