import tkinter as tk
from PIL import Image, ImageTk

class Enemy:
    def __init__(self, ball):
        self.ball = ball
        app = tk.Tk()
        img = Image.open('enemy.jpg')
