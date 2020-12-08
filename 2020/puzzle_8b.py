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
    instructions_len = len(instructions)
    instructions_ran = []
    while pc not in instructions_ran and pc < instructions_len:
        instruction = instructions[pc]
        instructions_ran.append(pc)
        if instruction[0] == 'jmp':
            pc += instruction[1]
        else:
            if instruction[0] == 'acc':
                acc += instruction[1]
            pc += 1
    status = pc == instructions_len
    return acc, status


def find_mutable_lines(instructions):
    mi = []
    for i in range(0, len(instructions)):
        if instructions[i][0] == 'nop' and instructions[i][1] != 0:
            mi.append(i)
        elif instructions[i][0] == 'jmp':
            mi.append(i)
    return mi


def mutate_instructions(i, instructions):
    ni = list(instructions)
    instruction = ni[i]
    if instruction[0] == 'nop':
        ni[i] = ('jmp', instruction[1])
    elif instruction[0] == 'jmp':
        ni[i] = ('nop', instruction[1])
    return ni


my_instructions = read_instructions('puzzle_8.txt')
result = play_instructions(my_instructions)
if result[1]:
    print(result[0])
else:
    mutable_lines = find_mutable_lines(my_instructions)
    for line_no in mutable_lines:
        new_instructions = mutate_instructions(line_no, my_instructions)
        result = play_instructions(new_instructions)
        if result[1]:
            print('Line %i modified. Acc = %i' % (line_no, result[0]))
            break
