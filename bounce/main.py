from tkinter import *
import random
import time
import math

class Ball:
    def __init__(self, calvas, color):
        self.canvas = canvas
        self.id = canvas.create_oval(10, 10 ,25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        self.speed = 3
        starts = [20,25,30,35,40,45,50,55,60]
        direction = [1,-1]
        random.shuffle(starts)
        random.shuffle(direction)
        self.x = starts[0]
        self.x = math.cos(math.radians(starts[0])) * self.speed * direction[0]
        self.y = math.sin(math.radians(starts[0])) * self.speed
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        #tate
        if pos[1] <= 0 or pos[3] >= self.canvas_height: 
            self.y *= -1
        #yoko
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x *= -1

class paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(-200,-100,1000,1000,fill=color) #x,y,xsize,ysize
        self.canvas.move(self.id, 200,350)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<Keypress-Left>', self.turn_left)
        self.canvas.bind_all('<Keypress-Right>', self.turn_right)
        
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0 or pos[2] >= self.canvas_width:
            self.x = 0
        

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.y = 2
        
tk = Tk()
tk.title("Game")
tk.resizable(0,0)
tk.wm_attributes("-topmost",1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

ball = Ball(canvas, 'red')
paddle = paddle(canvas, 'blue')

while True:
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)


