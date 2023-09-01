#importing libraries
from turtle import Turtle

class Ball(Turtle):

    #creating ball
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(0.5,0.5)
        self.penup()
        self.speed(10)
    
    #moving ball
    def move(self,x_move,y_move):
        new_x = self.xcor() + x_move
        new_y = self.ycor() + y_move        
        self.goto(new_x,new_y)