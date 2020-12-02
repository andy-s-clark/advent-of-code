num_list = []
target_sum = 2020
with open("puzzle_1.txt", "r") as f:
    for line in f:
        num_list.append(int(line.strip()))

list_len = len(num_list)

for i in range(0, list_len):
    for j in range(1, list_len):
        if i != j and num_list[i]+num_list[j] == target_sum:
            print("%i * %i = %i"
                  % (num_list[i], num_list[j], num_list[i]*num_list[j]))
            exit(0)

print("Failed")
