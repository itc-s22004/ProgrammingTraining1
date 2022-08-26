class Dlt:
    def __init__(self, canvas):
        self.canvas = canvas

    def win(self):
        self.canvas.create_text(250, 200, text='win')

    def lose(self):
        self.canvas.create_text(250, 200, text='lose')

    def dlt_text(self):
        self.canvas.delete(self.win)
        self.canvas.delete(self.lose)
