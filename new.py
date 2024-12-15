
from turtle import Turtle,Screen
screen = Screen()
import random

is_race_on = False
user_choice = screen.textinput(title="Make your bet",prompt="Which turtle win the race? Enter the color")

colors = ["red","orange","green","blue","yellow","purple",]
all_turtle = []
y_position = [-120,-80,-40,0,40,80]

screen.setup(width=500,height=400)
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtle.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_choice:
                print(f"You've win! the {winner} turtle is winner")
            else:
                print(f"You've lost! the {winner} turtle is winner")
        random_dis = random.randint(0,10)
        turtle.forward(random_dis)
screen.exitonclick()