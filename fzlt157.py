tm = [
    ["X", "W3", "E2", "S3", "S4"],
    ["S1", "E1", "N1", "S2", "W1"],
    ["S2", "E1", "N2", "S1", "N3"],
    ["N1", "X", "S2", "E1", "W4"],
    ["X", "E3", "X", "N2", "W4"]
]


def find_x(tm):
    mid = len(tm)//2
    rp = mid
    cp = mid
    pos = tm[rp][cp]
    # for i in tm:
    #     for j in i:
    #         if j[0] == 'N':

    def go_to(r, c):
        pos = tm[r][c]
        return pos

    def check_pos(r, c):
        if r > mid*2 or r < 0:
            return False
        elif c > mid*2 or c < 0:
            return False
        return True

    def check_found(p, r, c):
        if p == 'X':
            return (r, c)
        else:
            pos = go_to(rp, cp)

    if pos[0] == 'N':
        rp -= int(pos[1])
        if check_pos(rp, cp) == True:
            pos = go_to(rp, cp)
        else:
            return None
        print(pos)
    elif pos[0] == 'S':
        rp += int(pos[1])
        pos = go_to(rp, cp)
    elif pos[0] == 'E':
        cp += int(pos[1])
        pos = go_to(rp, cp)
    elif pos[0] == 'w':
        cp -= int(pos[1])
        pos = go_to(rp, cp)
    print(pos)


find_x(tm)
