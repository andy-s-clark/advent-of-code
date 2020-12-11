import logging


def load_input(filename):
    sm = []
    with open(filename, 'r') as f:
        for line in f:
            row = []
            for c in line.strip():
                row.append(c)
            sm.append(row)
    return sm


def format_seat_map(seat_map):
    fsm = ''
    for row in seat_map:
        fsm += ''.join(row) + "\n"
    return "\n" + fsm


def get_adjacent_seat_status_counts(seat_map, column_index, row_index):
    counts = {
        'L': 0,
        '#': 0
    }
    width = len(seat_map[0])
    height = len(seat_map)
    for ri in range(row_index - 1 if row_index > 0 else 0,
                    row_index + 2 if row_index < (height - 1) else height):
        for ci in range(column_index - 1 if column_index > 0 else 0,
                        column_index + 2 if column_index < (width - 1) else width):
            if ri != row_index or ci != column_index:
                if seat_map[ri][ci] == 'L':
                    counts['L'] += 1
                elif seat_map[ri][ci] == '#':
                    counts['#'] += 1
    return counts


def get_iteration(seat_map):
    nsm = []
    width = len(seat_map[0])
    height = len(seat_map)
    for ri in range(0, height):
        nsm.append(['?'] * width)
        for ci in range(0, width):
            cs = seat_map[ri][ci]
            if cs in 'L#':
                cnts = get_adjacent_seat_status_counts(seat_map, ci, ri)
                if cs == 'L' and cnts['#'] == 0:
                    nsm[ri][ci] = '#'
                elif cs == '#' and cnts['#'] >= 4:
                    nsm[ri][ci] = 'L'
                else:
                    nsm[ri][ci] = cs
            else:
                nsm[ri][ci] = cs
    return nsm


def count_seat_statuses(seat_map, status):
    count = 0
    for row in seat_map:
        count += row.count(status)
    return count


logging.basicConfig(level=logging.INFO)
my_last_occupied_count = -1
my_seat_map = load_input('puzzle_11.txt')
my_occupied_count = count_seat_statuses(my_seat_map, '#')
logging.debug(format_seat_map(my_seat_map))
while my_last_occupied_count != my_occupied_count:
    my_seat_map = get_iteration(my_seat_map)
    logging.debug(format_seat_map(my_seat_map))
    my_last_occupied_count = my_occupied_count
    my_occupied_count = count_seat_statuses(my_seat_map, '#')
    logging.debug('Last %i, Current: %i' % (my_last_occupied_count, my_occupied_count))

print(my_occupied_count)
