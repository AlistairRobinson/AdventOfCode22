from utils import Input

i = list(map(
    lambda l: list(map(
        lambda r: (int(r.split("-")[0]), int(r.split("-")[1])),
        l.split(",")
    )), Input("input/day4.txt").lines()
))

def contained(a, b, c, d):
    return \
        (min(a, b) >= min(c, d) and max(a, b) <= max(c, d)) or \
        (min(a, b) <= min(c, d) and max(a, b) >= max(c, d))

def overlap(a, b, c, d):
    return \
        (max(a, b) >= min(c, d) and min(a, b) <= max(c, d)) or \
        (min(a, b) <= min(c, d) and min(a, b) >= max(c, d))

def part1() -> int:
    return len(list(filter(lambda l: contained(l[0][0], l[0][1], l[1][0], l[1][1]), i)))

def part2() -> int:
    return len(list(filter(lambda l: overlap(l[0][0], l[0][1], l[1][0], l[1][1]), i)))

