from time import time
from turtle import Turtle
import random

STARTING_MOVE_DISTANCE = 10
COLORS = ["red","yellow","blue","orange","purple","green"]

class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()

    def create_cars(self):
        random_chance = random.randint(1,6)
        if(random_chance == 1):
            new_car = Turtle("square")
            new_car.shapesize(1,2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-280,280)
            new_car.goto(400,random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)


