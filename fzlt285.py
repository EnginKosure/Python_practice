# It takes 22 minutes for 10 people to paint 10 walls.
# How many minutes does it take 14 people to paint 14 walls?

rate = {
    "people": 10,
    "walls": 10,
    "minutes": 22
}


def time(dct, people, walls):
    r = dct['walls'] / dct['minutes'] / dct['people']

    t = walls / people / r

    return int(t)


print(time(rate, rate['people'], rate['walls']))  # 22
