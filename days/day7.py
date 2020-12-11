from myutils import files

def main():
    print("===== Part 1 =====")
    answer = part1()
    print("answer: {}".format(answer))

def part1():

    inputs = files.getInputs("../inputs/day7-input.txt", strip=True)
    #inputs = files.getInputs("../inputs/test.txt", strip=True)
    rules = {}

    for line in inputs:
        line_parts = line.split("contain")
        bags = (line_parts[1])
        bags = bags[:len(bags)-1].strip()
        bags_array = parseBags(bags)

        rx = line_parts[0].split(" ")
        rule_key = rx[0] + " " + rx[1]
        rules[rule_key] = bags_array

    #print(rules)
    # print("len: {}".format(len(rules)))
    # print(rules["posh black"])
    for rule in rules:
        print("{}: {}".format(rule, rules[rule]))


    shiny_gold_count = 0
    for rule in rules:
        print("check: {}".format(rule))
        contains_shiny_gold = checkBagContainsShinyGold(rules, rule)
        if contains_shiny_gold:
            shiny_gold_count += 1
    return str(shiny_gold_count)

def checkBagContainsShinyGold(rules, rule):
    if rules[rule] == []:
        print("no")
        return False
    for r in rules[rule]:
        if r == "shiny gold":
            print("gold!")
            return True
        else:
            print("check 2: {}".format(r))
            return checkBagContainsShinyGold(rules, r)

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
            # bags_array.append("{} {}".format(b_x[1], b_x[2]))
        return bags_array

if __name__ == "__main__":
    main()