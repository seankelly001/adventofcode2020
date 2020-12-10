import os
import re

def main():
    print("===== Part 1 =====")
    valid_passport_count = part1()
    print("number of valid passports: {}".format(valid_passport_count))

    print("===== Part 2 =====")
    valid_passport_count = part2()
    print("number of valid passports: {}".format(valid_passport_count))

def part1():
    mandatory_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #cid is optional
    passports = getPassports()
    valid_passport_count = 0
    for passport in passports:
        valid = all(field in passport for field in mandatory_keys)
        if valid:
            valid_passport_count += 1
    return str(valid_passport_count)

def part2():
    mandatory_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #cid is optional
    passports = getPassports()
    valid_passport_count = 0
    for passport in passports:
        if (all(field in passport for field in mandatory_keys)) and (validPassport(passport)):
          valid_passport_count += 1
    return str(valid_passport_count)

def getPassports():

    path = os.path.join(os.path.dirname(__file__), 'input.txt')
    passport_index = 0
    passports = []

    with open(path) as file:
        for line in file:
            if line.isspace():
                passport_index += 1
                continue
           
            if passport_index >= len(passports):
                 passports.append({})
            passport_parts = line.split()
            for part in passport_parts:
                k = part.split(":")[0]
                v = part.split(":")[1]
                passports[passport_index][k] = v
    return passports

def validPassport(passport):
    return validBYR(passport["byr"]) & \
           validIYR(passport["iyr"]) & \
           validEYR(passport["eyr"]) & \
           validHGT(passport["hgt"]) & \
           validHCL(passport["hcl"]) & \
           validECL(passport["ecl"]) & \
           validPID(passport["pid"])

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def validBYR(yr):
    return validYear(yr, 1920, 2002)

# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def validIYR(yr):
    return validYear(yr, 2010, 2020)

# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def validEYR(yr):
    return validYear(yr, 2020, 2030)
    
def validYear(yr, min, max):
    if len(yr) != 4:
        return False
    try:
        yr_int = int(yr)
        return (yr_int >= min) & (yr_int <= max)
    except ValueError:
        return False

# hgt (Height) - a number followed by either cm or in:
# If cm, the number must be at least 150 and at most 193.
# If in, the number must be at least 59 and at most 76.
def validHGT(hgt):
    repl_cm = re.compile(r'^\d+cm')
    repl_in = re.compile(r'^\d+in')
    repl_num = re.compile(r'^\d+')

    #check cm
    if re.search(repl_cm, hgt):
        cm_list = re.findall(repl_num, hgt)
        cm = int(cm_list[0])
        return (cm >= 150) & (cm <= 193)
    # check in
    if re.search(repl_in, hgt):
        in_list = re.findall(repl_num, hgt)
        inch = int(in_list[0])
        return (inch >= 59) & (inch <= 76)
    return False

# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def validHCL(hgt):
    repl_hcl = re.compile(r'^#[0-9a-f]{6}$')
    if re.match(repl_hcl, hgt):
        return True
    return False

# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def validECL(ecl):
    valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in valid_ecls

# pid (Passport ID) - a nine-digit number, including leading zeroes.
def validPID(pid):
    repl_pid = re.compile(r'^[0-9]{9}$')
    if re.match(repl_pid, pid):
        return True
    return False

if __name__ == "__main__":
    main()