num_list = []
target_sum = 2020
with open("puzzle_1.txt", "r") as f:
    for line in f:
        num_list.append(int(line.strip()))

for i in num_list:
    for j in num_list:
        for k in num_list:
            if i != j and i != k and j != k and i+j+k == target_sum:
                print("%i * %i * %i = %i" % (i, j, k, i*j*k))
                exit(0)

print("Failed")
