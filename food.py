from turtle import Turtle
import random

#inheriting from Turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("#ffde57")
        self.speed("fastest")
        x = random.randint(-250,250)
        y= random.randint(-250,250)
        self.goto(x,y)

    def refresh(self):
        random_x = random.randint(-250, 250)
        random_y = random.randint(-250, 250)
        self.goto(random_x, random_y)

