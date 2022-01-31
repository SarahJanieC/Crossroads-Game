from turtle import Screen
from cars import Cars
from level import Level
from player import Player
import time
# Crossroads Game written in Python using Turtle module. Cross road without getting hit by objects to level up

screen = Screen()
screen.setup(800,600)
screen.bgcolor("white")
screen.title("Crossroads Game")
screen.tracer(0)


# Create Objects
cars = Cars()
t = Player()
level = Level()


#bind key to functions
screen.listen()
screen.onkey(t.up, "Up")
screen.onkey(t.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
        
    if(t.ycor() > 280):
        t.new_level()
        level.update_level()
    
    #detect if turtle hits car
    for car in cars.all_cars:
        if(car.distance(t) < 20):
            level.game_over()
            game_is_on = False
    cars.create_cars()
    cars.move()
    
screen.exitonclick()