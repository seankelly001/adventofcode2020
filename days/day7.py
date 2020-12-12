from myutils import files

def main():
    print("===== Part 1 =====")
    answer = part1()
    print("answer: {}".format(answer))

    print("===== Part 2 =====")
    answer = part2()
    print("answer: {}".format(answer))

def part1():

    inputs = files.getInputs("../inputs/day7-input.txt", strip=True)
    #inputs = files.getInputs("../inputs/test.txt", strip=True)
    rules = getRules(inputs)

    shiny_gold_bags = []
    for rule in rules:
        if checkBagContainsShinyGold(rules, rule):
            shiny_gold_bags.append(rule)

    #print(shiny_gold_bags)
    return str(len(shiny_gold_bags))

def part2():
    inputs = files.getInputs("../inputs/day7-input.txt", strip=True)
    inputs = files.getInputs("../inputs/test.txt", strip=True)
    rules = getRules(inputs)
    bag_count = getBagCount(rules, "shiny gold")
    return str(bag_count)

def checkBagContainsShinyGold(rules, rule):
    if rules[rule] == []:
        return False
    #for r in rules[rule]:
    for r in list(set(rules[rule])):
        if r == "shiny gold":
            return True
        else:
            if checkBagContainsShinyGold(rules, r):
                return True
    return False

def getBagCount(rules, rule):
    if rules[rule] == []:
        return 1
    bag_counts = []
    for r in list(set(rules[rule])):
        #bag_count = bag_count + (getBagCount(rules, r) * rules[rule].count(r))
        bag_counts.append((getBagCount(rules, r) * rules[rule].count(r)))
    # for r in rules[rule]:
    #     bag_count += (getBagCount(rules, r))
    #print("{} has {}".format(rule, bag_count))
    return bag_counts

def getRules(inputs):
    rules = {}

    for line in inputs:
        line_parts = line.split("contain")
        bags = (line_parts[1])
        bags = bags[:len(bags)-1].strip()
        bags_array = parseBags(bags)

        rx = line_parts[0].split(" ")
        rule_key = rx[0] + " " + rx[1]
        rules[rule_key] = bags_array

    # for rule in rules:
    #     print("{}: {}".format(rule, rules[rule]))

    return rules

def parseBags(bags_string):

    if bags_string == "no other bags":
        return []
    else:
        bags = bags_string.split(", ")
        bags_array = []
        for b in bags:
            b_x = b.split(" ")
            for _ in range(int(b_x[0])):
                bags_array.append("{} {}".format(b_x[1], b_x[2]))
            #bags_array.append("{} {}".format(b_x[1], b_x[2]))
        return bags_array

if __name__ == "__main__":
    main()