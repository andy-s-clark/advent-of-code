import logging


def bsp_text_to_position(t):
    row_min = 0
    row_max = 127
    col_min = 0
    col_max = 7

    for c in t:
        if c == 'F':
            row_max = int((row_max-row_min)/2)+row_min
        elif c == 'B':
            row_min = int((row_max-row_min)/2)+row_min+1
        if c == 'L':
            col_max = int((col_max-col_min)/2)+col_min
        elif c == 'R':
            col_min = int((col_max-col_min)/2)+col_min+1
        logging.debug(c, row_min, row_max, col_min, col_max)

    return row_max, col_max


def position_to_seat_id(p):
    return p[0] * 8 + p[1]


max_seat_id = 0
with open("puzzle_5.txt", "r") as f:
    for line in f:
        my_position = bsp_text_to_position(line.strip())
        my_seat_id = position_to_seat_id(my_position)
        if max_seat_id < my_seat_id:
            max_seat_id = my_seat_id
        logging.debug(my_position, my_seat_id)
print(max_seat_id)
