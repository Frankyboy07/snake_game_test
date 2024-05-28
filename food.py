from turtle import Turtle
import random
COLORS = ['red', 'green', 'blue', 'purple', 'cyan', 'gold']

class Food(Turtle):

    def __init__(self, color):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.color(color)
        self.speed('fastest')
        self.refresh()

    def refresh(self):
        self.color(random.choice(COLORS))
        random_x = random.randint(-260, 260)
        random_y = random.randint(-260, 260)
        self.goto(random_x, random_y)
