import logging


def read_adapters(filename):
    adapters = []
    with open(filename, 'r') as f:
        for line in f:
            adapters.append(int(line.strip()))
    return adapters


def get_differences(adapters, start):
    ds = []
    last = start
    for a in set(adapters):
        ds.append((a, a - last))
        last = a
    return ds


def get_unique_adapter_sets(adapters, start):
    uass = []
    uas = []
    last_diff = 0
    diffs = get_differences(adapters + [start], start)
    logging.debug('Diffs %s:' % diffs)
    for ds in diffs:
        if ds[1] < 3:
            uas.append(ds[0])
        elif last_diff < 3:
            uas.append(ds[0])
            uass.append(uas)
            uas = [ds[0]]
        else:
            logging.debug('Dropped consecutive 3: %i' % ds[0])
        last_diff = ds[1]
    uass.append(uas)
    return uass


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


logging.basicConfig(level=logging.DEBUG)
my_adapters = read_adapters('puzzle_10_sample_b.txt')
logging.debug('Adapters: %s' % sorted(my_adapters))
logging.debug('Answer using recursion for the lot: %s' % len(get_valid_combinations(my_adapters, 0, max(my_adapters))))
my_adapter_sets = get_unique_adapter_sets(my_adapters, 0)
logging.debug('Adapter Sets: %s' % my_adapter_sets)
total_combos = 1
for my_as in my_adapter_sets:
    if len(my_as) > 3:
        my_start = my_as.pop(0)
        my_end = my_as.pop()
        combo_count = len(get_valid_combinations(my_as, my_start, my_end))
        total_combos = total_combos * (combo_count if combo_count > 1 else 1)
        logging.debug('Combo Count: %i, Start: %i, Adapter Set: %s, End: %i' % (combo_count, my_start, my_as, my_end))
print(total_combos)
