from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("red")
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.goto(-290,265)
        self.write(f"Level: {self.level}", False, align=ALIGNMENT, font=FONT)   
        self.level += 1
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)   
