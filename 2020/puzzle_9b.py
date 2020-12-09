def load_data(filename):
    d = []
    with open(filename, 'r') as f:
        for line in f:
            d.append(int(line.strip()))
    return d


def find_first_outlier(data, preamble_length):
    ps = []
    for i in range(0, len(data) - 1):
        if i >= preamble_length:
            if not is_valid_number(data[i], ps):
                return data[i]
            ps.pop(0)
        ps.append(data[i])
    return None


def is_valid_number(num, predecessors):
    ps = set(predecessors)
    for i in ps:
        for j in ps:
            if i+j == num:
                return True
    return False


def find_weakness(data, outlier):
    for i in range(0, len(data) - 2):
        for j in range(1, len(data)):
            if sum(list(data[i:j])) == outlier:
                return min(data[i:j]) + max(data[i:j])
    return None


my_data = load_data('puzzle_9.txt')
my_outlier = find_first_outlier(my_data, 25)
my_weakness = find_weakness(my_data, my_outlier)
print(my_weakness)
