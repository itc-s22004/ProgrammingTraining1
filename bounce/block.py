import random

class Block:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.n = random.randint(0,300)
        self.m = random.randint(0,170)
        self.id = self.canvas.create_rectangle(self.n, self.m, self.n + 100, self.m + 40, fill=color)

    
    def crash(self):
        self.canvas.delete(self.id)
    
    def clone(self, color):
        self.n = random.randint(0, 300)
        self.m = random.randint(0, 170)
        self.id = self.canvas.create_rectangle(self.n, self.m, self.n + 100, self.m + 40, fill=color)
    
