def count_matching_answers(groups_answers):
    overlap = groups_answers.pop()
    for answers in groups_answers:
        overlap = set(answers).intersection(overlap)
    return len(overlap)


result = 0
my_groups_answers = []
with open("puzzle_6.txt", "r") as f:
    for line in f:
        if line == "\n":
            result += count_matching_answers(my_groups_answers)
            my_groups_answers = []
        else:
            my_groups_answers.append([c for c in line.strip()])
result += count_matching_answers(my_groups_answers)
print(result)
