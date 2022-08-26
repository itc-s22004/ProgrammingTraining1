import tkinter as tk

class Text(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)

        
        self.label = tk.Label(self.master,text="score"
                    ,font=('',20),bg='sky blue')

        
        self.num = 0

        self.label.pack()
        self.label.place(x=320, y=400)
        
        if __name__ == "__main__":
            root = tk.Tk()
            app = Text(master = root)
            app.mainloop()

    def plus(self):
        self.num += 10

    
    def draw(self):
        self.label2 = tk.Label(self.master, text=self.num,
                            font=('',20))
        self.label2.pack()
        self.label2.place(x=400, y=400)
    
    ''' 
    def lose(self):
        self.lose = tk.Label(text='lose', font=('', 40), tag='l_tag')
        self.lose.pack()
        self.lose.place(x=200, y=250)

    def win(self):
        self.win = tk.Label(text='win', font=('', 40), tag='w_tag')
        self.win.pack()
        self.win.place(x=200, y=250)
    '''    

