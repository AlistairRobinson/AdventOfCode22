from utils import Input

i = Input("input/day6.txt").raw

def part1(window_size=4) -> int:
    return next((n for n in range(window_size, len(i)) if len(set(i[n-window_size:n])) == window_size))

def part2() -> int:
    return part1(window_size=14)