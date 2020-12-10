def read_adapters(filename):
    adapters = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                adapters.append(int(line.strip()))
            except ValueError:
                continue
    return adapters


def is_valid_adapter(input_joltage, adapter):
    return input_joltage < adapter <= input_joltage + 3


def get_valid_combinations(adapters, start, end):
    combinations = []
    for this_adapter in filter(lambda a: is_valid_adapter(start, a), adapters):
        if is_valid_adapter(this_adapter, end):
            combinations.append([this_adapter])
        else:
            remaining = list(filter(lambda a: a > this_adapter, adapters))
            sub_combinations = list(get_valid_combinations(remaining, this_adapter, end))
            for sc in sub_combinations:
                combinations.append([this_adapter] + sc)
    return combinations


total_combinations = 1
for i in range(1, 7):
    my_adapters = read_adapters("puzzle_10_data/%i.txt" % i)
    my_start = 0
    my_end = max(my_adapters) + 3
    my_combinations = get_valid_combinations(sorted(my_adapters), my_start, my_end)
    print(i, len(my_combinations))
    total_combinations = total_combinations * len(my_combinations)
print(total_combinations)
