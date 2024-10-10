from turtle import Turtle
#Paddle creation
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape('square')
        self.color('green')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)#requires two parameters(co-ordinates of x and y)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)


    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)


