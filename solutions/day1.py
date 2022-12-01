from utils import Input

i = list(map(sum, Input("input/day1.txt").paragraphs(type=int)))

def part1():
    return max(i)

def part2(top=3):
    best = set(i[:top])
    for elf in i[top:]:
        if elf > (lowest := min(best)):
            best.remove(lowest)
            best.add(elf)
    return sum(best)