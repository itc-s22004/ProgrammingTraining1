import random
import math
import time

class Ball:
    def __init__(self, canvas, color,paddle, block, text):
        self.canvas = canvas
        self.paddle = paddle
        self.text = text
        self.block = block
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.init_x = self.canvas_width / 2 - 7.5
        self.init_y = self.canvas_height / 2 - 7.5
        self.speed = 0
        self.x = 0
        self.y = 0

    def start(self, evt):
        if self.speed != 0:
            return a
        self.canvas.moveto(self.id, self.init_x, self.init_y)#, self.block_id)
        self.speed = 4
        angle = math.radians(random.choice(list(range(20, 65, 5))))
        direction = random.choice([1, -1])
        self.x = math.cos(angle) * self.speed * direction
        self.y = math.sin(angle) * self.speed
        self.canvas.delete('lose')
        self.canvas.delete('win')
        self.canvas.delete('score')
        #self.text.dlt()
        
        
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        
        
        if pos[0] <= 0:
            self.fix(pos[0] - 0, 0)
            
        if pos[1] <= 0:
            self.fix(0, pos[1])
            
        if pos[2] >= self.canvas_width:
            self.fix(pos[2] - self.canvas_width, 0)
            
        if pos[3] >= self.canvas_height:
            self.fix(0, pos[3] - self.canvas_height)
            self.failed()
            
            

        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]\
           and paddle_pos[1] <= pos[3] <= paddle_pos[3]:
            self.fix(0, pos[3] - paddle_pos[1])
        
#------------block---------------
        block_pos = self.canvas.coords(self.block.id)
        #plus = self.text.draw()
        

        '''
        if pos[0] <= block_pos[2] and pos[2] >= block_pos[0] and \
           pos[1] >= block_pos[3] and pos[3] <= block_pos[1]:
            if pos[0] <= block_pos[2]:
                self.x = -self.x
            if pos[2] >= block_pos[0]:
                self.x = -self.x
            if pos[1] <= block_pos[3]:
                self.y = -self.y
            if pos[3] >= block_pos[1]:
                self.y = -self.y
        '''
        if pos[0] <= block_pos[2] and pos[2] >= block_pos[0]\
             and pos[1] <= block_pos[3] and pos[3] >= block_pos[1]:
            self.text.plus()
            self.block.crash()
            self.block.clone("green")
            self.y_win()
            if pos[0] <= block_pos[2] and pos[0] >= block_pos[0]:
                self.x = -self.x
                #self.text.plus()
                
            if pos[1] <= block_pos[3] and pos[1] >= block_pos[1]:
                self.y = -self.y
                #self.text.plus()
            
            if pos[2] >= block_pos[0] and pos[2] <= block_pos[2]:
                self.x = -self.x
                #self.text.plus()
            
            if pos[3] >= block_pos[1] and pos[3] <= block_pos[3]:
                self.y = -self.y
                #self.text.plus()
                      
            
#------------------------------------         
            

            
    def fix(self, diff_x, diff_y):
        self.canvas.move(self.id, -(diff_x * 2), -(diff_y * 2))
        #self.canvas.move(self.block_id, -(diff_x * 2), -(diff_y * 2))
        
        if diff_x != 0:
            self.x = -self.x
        if diff_y != 0:
            self.y = -self.y

        

    def failed(self):
        self.x = 0
        self.y = 0
        self.speed = 0
        self.canvas.create_text(250, 200, text='lose', font=('', 30), tag='lose')
        #self.text.lose()

    def y_win(self):
        if self.text.num >= 40:
            #self.text.win()
            self.canvas.create_text(250, 200, text='win', font=('', 30), tag='win')
            self.x = 0
            self.y = 0
            self.speed = 0
    '''
    def draw(self):
        self.canvas.create_text(400, 400, text=self.text.num, font=('', 20), tag='score')
    '''
    
