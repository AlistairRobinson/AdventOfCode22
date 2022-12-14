class Input:
    def __init__(self, filepath):
        with open(filepath) as f:
            self.raw = f.read()
    
    def lines(self, type=str):
        return list(map(type, self.raw.split("\n")))

    def paragraphs(self, type=str):
        return [list(map(type, group.split("\n"))) for group in self.raw.split("\n\n")]

    def words(self, type=str):
        return [list(map(type, line.split())) for line in self.lines()]

def chunks(list, chunk_size):
    return [list[i:i+chunk_size] for i in range(0, len(list), chunk_size)]