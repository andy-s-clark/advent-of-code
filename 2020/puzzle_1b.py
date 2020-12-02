num_list = []
target_sum = 2020
with open("puzzle_1.txt", "r") as f:
    for line in f:
        num_list.append(int(line.strip()))

list_len = len(num_list)

for i in range(0, list_len):
    for j in range(1, list_len):
        for k in range(2, list_len):
            if i != j and i != k and j != k and num_list[i]+num_list[j]+num_list[k] == target_sum:
                print("%i * %i * %i = %i"
                      % (num_list[i], num_list[j], num_list[j], num_list[i]*num_list[j]*num_list[k]))
                exit(0)

print("Failed")
