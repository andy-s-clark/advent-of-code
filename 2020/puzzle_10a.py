def read_adapters(filename):
    adapters = []
    with open(filename, 'r') as f:
        for line in f:
            adapters.append(int(line.strip()))
    return adapters


def find_differences(adapters, outlet_joltage, device_joltage):
    ds = []
    last = outlet_joltage
    for a in set(adapters):
        ds.append(a - last)
        last = a
    ds.append(device_joltage - last)
    return ds


my_adapters = read_adapters('puzzle_10.txt')
my_differences = find_differences(my_adapters, 0, max(my_adapters) + 3)
print(my_differences.count(1) * my_differences.count(3))
