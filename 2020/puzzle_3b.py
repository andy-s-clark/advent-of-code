def read_tree_map(file_path):
    t = []
    with open(file_path, "r") as f:
        for line in f:
            tml = []
            for c in line:
                if c == '#':
                    tml.append(True)
                elif c == '.':
                    tml.append(False)
            t.append(tml)
    return t


def count_trees_with_forehead(tree_map, x_start=0, y_start=0, x_increment=3, y_increment=1):
    x_max = len(tree_map[0]) - 1
    tree_hit_count = 0
    x_pos = x_start
    for y_pos in range(y_start, len(tree_map), y_increment):
        if tree_map[y_pos][x_pos]:
            tree_hit_count += 1
        x_pos += x_increment
        if x_pos > x_max:
            # Wrap around the map
            x_pos = x_pos - x_max - 1
    return tree_hit_count


my_tree_map = read_tree_map("puzzle_3.txt")
slopes = [(1, 1),
          (3, 1),
          (5, 1),
          (7, 1),
          (1, 2)
          ]
result = 1
for slope in slopes:
    trees_hit = count_trees_with_forehead(my_tree_map, 0, 0, slope[0], slope[1])
    print("%s %i" % (slope, trees_hit))
    result *= trees_hit
print("Final result: %i" % result)
