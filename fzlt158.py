def find_x(treasure_map):
    m = dict(zip('NSEW', [(-1, 0), (1, 0), (0, 1), (0, -1)]))
    pos = (len(treasure_map) // 2, len(treasure_map[0]) // 2)
    v = set()
    while pos not in v:
        v.add(pos)
        if treasure_map[pos[0]][pos[1]] == "X":
            return pos
        s, mv = treasure_map[pos[0]][pos[1]][0], int(
            treasure_map[pos[0]][pos[1]][1:])
        x, y = (m[s][0] * mv, m[s][1] * mv)
        pos = pos[0] + x, pos[1] + y
        if pos[0] < 0 or pos[0] >= len(treasure_map) or pos[1] < 0 or pos[1] >= len(treasure_map[0]):
            break

# 2nd solution


def moving(y, x, treasure_map):
    if x < 0 or y < 0 or x >= len(treasure_map[0]) or y >= len(treasure_map):
        return
    if treasure_map[y][x] == '':
        return
    if treasure_map[y][x] == 'X':
        return y, x
    direction, distance = treasure_map[y][x][0], int(treasure_map[y][x][1:])
    if direction == 'N':
        treasure_map[y][x] = ''
        return moving(y - distance, x, treasure_map)
    elif direction == 'S':
        treasure_map[y][x] = ''
        return moving(y + distance, x, treasure_map)
    elif direction == 'W':
        treasure_map[y][x] = ''
        return moving(y, x - distance, treasure_map)
    elif direction == 'E':
        treasure_map[y][x] = ''
        return moving(y, x + distance, treasure_map)


def find_x1(treasure_map):
    return moving(len(treasure_map) // 2, len(treasure_map[0]) // 2, treasure_map)
