#importing libraries
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

#required variables
x_move = 10
y_move = 10
sleep = 0.1
game_on = True

#creating screen
screen = Screen()
screen.setup(800,600)
screen.bgcolor("Black")
screen.title("Ping Pong Game")
screen.tracer(0)

#creating paddles
r_paddle = Paddle(380)
l_paddle = Paddle(-380)

#creating ball
ball = Ball()

#creating scoreboard
l_score = ScoreBoard(-100)
r_score = ScoreBoard(100)

#moving ball on keypress
screen.update()
screen.listen()
screen.onkey(r_paddle.move_upward,"Up")
screen.onkey(r_paddle.move_downward,"Down")
screen.onkey(l_paddle.move_upward,"w")
screen.onkey(l_paddle.move_downward,"s")

while(game_on):
    time.sleep(sleep)
    
    #collision with paddles
    if((ball.distance(r_paddle)<50 and ball.xcor()>350)
       or (ball.distance(l_paddle)<50 and ball.xcor()<-350)):
        x_move *= -1
        sleep *= 0.9
    ball.move(x_move,y_move)
    screen.update()
    
    #if paddle try to go out of bounds
    if(r_paddle.ycor()>280 or r_paddle.ycor()<-280):
        r_paddle.goto(r_paddle.xcor(),r_paddle.ycor()*-0.9)
    if(l_paddle.ycor()>280 or l_paddle.ycor()<-280):
        l_paddle.goto(l_paddle.xcor(),l_paddle.ycor()*-0.9)
    
    #collision with top or bottom wall
    if(ball.ycor()>=280 or ball.ycor()<=-280):
        y_move *= -1
        sleep = 0.1
    
    #right misses the ball
    if(ball.xcor()>380):
        ball.goto(0,0)
        x_move *= -1
        l_score.new_score()
    
    #left misses the ball
    elif(ball.xcor()<-380):
        ball.goto(0,0)
        x_move *= -1
        r_score.new_score()
    
    #checking for winner
    if(l_score.return_score()==5):
        l_score.game_over("Left")
        game_on = False
    if(r_score.return_score()==5):
        r_score.game_over("Right")
        game_on = False

screen.exitonclick()
