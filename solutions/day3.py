from utils import Input, chunks
from string import ascii_letters

i = Input("input/day3.txt").lines()

def to_priority(c: str) -> int:
    return ascii_letters.index(c) + 1

def part1() -> int:
    return sum(map(lambda r: to_priority(set(r[:len(r)//2]).intersection(set(r[len(r)//2:])).pop()), i))

def part2(group_size=3) -> int:
    return sum(map(lambda g: to_priority(set(g[0]).intersection(set(g[1])).intersection(set(g[2])).pop()), chunks(i, group_size)))

