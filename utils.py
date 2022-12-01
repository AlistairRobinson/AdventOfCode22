class Input:
    def __init__(self, filepath):
        with open(filepath) as f:
            self.raw = f.read()
    
    def lines(self, type=str):
        return list(map(type, self.raw.split("\n")))

    def paragraphs(self, type=str):
        return [list(map(type, group.split("\n"))) for group in self.raw.split("\n\n")]