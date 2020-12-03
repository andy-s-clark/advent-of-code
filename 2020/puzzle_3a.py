x_increment = 3
x_start_pos = 0
y_start_pos = 0

tree_map = []
with open("puzzle_3.txt", "r") as f:
    for line in f:
        tree_map_line = []
        for c in line:
            if c == '#':
                tree_map_line.append(True)
            elif c == '.':
                tree_map_line.append(False)
        tree_map.append(tree_map_line)

x_max = len(tree_map[0]) - 1
tree_hit_count = 0
x_pos = x_start_pos
for y_pos in range(y_start_pos, len(tree_map)):
    if tree_map[y_pos][x_pos]:
        tree_hit_count += 1
    x_pos += x_increment
    if x_pos > x_max:
        # Wrap around the map
        x_pos = x_pos - x_max - 1
print(tree_hit_count)
