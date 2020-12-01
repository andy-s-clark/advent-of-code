num_list = []
target_sum = 2020
with open("puzzle_1a.txt", "r") as f:
    for line in f:
        num_list.append(int(line.strip()))

for i in num_list:
    for j in num_list:
        if i != j and i+j == target_sum:
            print("%i * %i = %i" % (i, j, i*j))
            exit(0)

print("Failed")
