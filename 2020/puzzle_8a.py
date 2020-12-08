
def read_instructions(filename):
    instructions = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(' ')
            instructions.append((parts[0], int(parts[1])))
    return instructions


def play_instructions(instructions):
    acc = 0
    pc = 0
    instructions_ran = []
    while pc not in instructions_ran:
        instruction = instructions[pc]
        instructions_ran.append(pc)
        if instruction[0] == 'jmp':
            pc += instruction[1]
        else:
            if instruction[0] == 'acc':
                acc += instruction[1]
            pc += 1
    return acc


my_instructions = read_instructions('puzzle_8.txt')
result = play_instructions(my_instructions)
print(result)
