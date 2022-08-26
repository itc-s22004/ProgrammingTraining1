class Text:
    def __init__(self, canvas):
        self.canvas = canvas
        self.num = 0
        self.id = self.canvas.create_text(320, 400, text="score " + str(self.num))
                

    def plus(self):
        self.num += 1

    def draw(self):
        self.num
        
