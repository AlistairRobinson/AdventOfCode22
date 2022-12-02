from utils import Input
from enum import Enum

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def from_char(c):
        return \
            Move.ROCK if c in ("A", "X") else \
            Move.PAPER if c in ("B", "Y") else \
            Move.SCISSORS if c in ("C", "Z") else None

    def __gt__(self, other) -> bool:
        return self.value == other.value % 3 + 1
    
    def score(self, opponent) -> int:
        result = 6 if self > opponent else 3 if self == opponent else 0
        return result + self.value

    def match_intent(self, intent):
        return Move((self.value + intent.value) % 3 + 1)

class Intent(Enum):
    LOSE = 1
    DRAW = 2
    WIN = 3

    def from_char(c):
        return \
            Intent.LOSE if c in ("X") else \
            Intent.DRAW if c in ("Y") else \
            Intent.WIN if c in ("Z") else None

i = Input("input/day2.txt").words()

def part1() -> int:
    return sum([
        Move.from_char(moves[1]).score(Move.from_char(moves[0])) for moves in i
    ])

def part2() -> int:
    return sum([
        Move.from_char(moves[0])
            .match_intent(Intent.from_char(moves[1]))
            .score(Move.from_char(moves[0]))
        for moves in i
    ])