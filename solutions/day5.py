from utils import Input

class Stacks:
    ids = []
    stacks = {}

    def __init__(self, start, multi_pickup=False):
        self.multi_pickup = multi_pickup
        self.ids = start[-1].split()
        self.stacks = {
            s: [
                start[r][(int(s) - 1) * 4 + 1] 
                for r in range(len(start) - 1) 
                if start[r][(int(s) - 1) * 4 + 1] != " "
            ] for s in self.ids
        }
    
    def execute(self, i):
        self.stacks[i["dest"]] = self.stacks[i["orig"]][:i["#"]][::-1 if not self.multi_pickup else 1] + self.stacks[i["dest"]]
        self.stacks[i["orig"]] = self.stacks[i["orig"]][i["#"]:]
        return self

    def run(self, instructions):
        return self.execute(instructions[0]).run(instructions[1:]) if len(instructions) > 0 else self

    def tops(self):
        return "".join([self.stacks[c][0] for c in self.ids])

i = Input("input/day5.txt").paragraphs()
instructions = [{
    "#": int(r[1]),
    "orig": r[3],
    "dest": r[5],
} for r in map(lambda l: l.split(), i[1])]

def part1() -> str:
    return Stacks(i[0], multi_pickup=False).run(instructions).tops()

def part2() -> int:
    return Stacks(i[0], multi_pickup=True).run(instructions).tops()

