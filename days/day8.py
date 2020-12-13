from myutils import files

def main():
    print("===== Part 1 =====")
    answer = part1()
    print("answer: {}".format(answer))

    print("===== Part 2 =====")
    answer = part2()
    print("answer: {}".format(answer))

def part1():
    instructions = files.getInputs("../inputs/day8-input.txt", strip=True)   
    accumulator, loop_detected = execute_instruction_set(instructions)
    if loop_detected:
        return str(accumulator)
    else:
        return "error, no loop detected"

def part2():
    instructions = files.getInputs("../inputs/day8-input.txt", strip=True)
    for i in range(len(instructions) - 1):
        #print("--------")
        instructions_copy = instructions.copy()
        instructions_copy[i] = fix_instruction(instructions_copy[i])
        accumulator, loop_detected = execute_instruction_set(instructions_copy)
        if not loop_detected:
            return str(accumulator)
    return "No fix found"

def execute_instruction_set(instructions):
    accumulator = 0
    inst_index = 0
    executed = []
    loop_detected = False
    while(True):
        #we have reached end of program succesfully
        if inst_index >= len(instructions):
            break

        if inst_index in executed:
            loop_detected = True
            break
        else:
            executed.append(inst_index)
        inst_index, accumulator = execute_instruction(instructions, inst_index, accumulator)

    return str(accumulator), loop_detected

def execute_instruction(instructions, inst_index, accumulator):
    instruction = instructions[inst_index]
    parts = instruction.split()

    if parts[0] == "nop":
        inst_index += 1
    if parts[0] == "acc":
        accumulator += int(parts[1])
        inst_index += 1
    if parts[0] == "jmp":
        inst_index += int(parts[1])

    return inst_index, accumulator

def fix_instruction(instruction):
    parts = instruction.split()
    fixed_instruction = instruction
    print("instruction to fix: {}".format(instruction))
    if parts[0] == "nop":
        fixed_instruction = "jmp {}".format(parts[1])
    if parts[0] == "jmp":
        fixed_instruction = "nop {}".format(parts[1])
    print("fixed: {}".format(fixed_instruction))
    return fixed_instruction

if __name__ == "__main__":
    main()