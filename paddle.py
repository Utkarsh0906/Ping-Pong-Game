#importing libraries
from turtle import Turtle,Screen

class Paddle(Turtle):
    
    #creating paddle
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1,5)
        self.goto(pos,0)
        self.setheading(90)
    
    #moving paddle
    def move_upward(self):
        self.forward(20)
    def move_downward(self):
        self.backward(20)