result = 0
group_answers = []
with open("puzzle_6.txt", "r") as f:
    for line in f:
        if line == "\n":
            result += len(set(group_answers))
            group_answers = []
        else:
            for c in line.strip():
                group_answers.append(c)
result += len(set(group_answers))
print(result)
