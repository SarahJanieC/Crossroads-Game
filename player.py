from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        pass
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0,-275)

    def up(self):
        new_y = self.ycor() + 28
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 28
        self.goto(self.xcor(), new_y)

    def new_level(self):
        self.goto(0,-275)
        

