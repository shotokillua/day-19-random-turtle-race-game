from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Who will win the race?", prompt="Pick a color: ")
#print(user_bet)

colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
num_steps = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_position = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []

for turtle_obj in range(0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_obj])
    new_turtle.goto(x=-240, y=y_position[turtle_obj])
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        turtle.forward(random.choice(num_steps))
        if turtle.xcor() > 230:
            if user_bet == turtle.pencolor():
                print(f"You win! The {turtle.pencolor()} is the winner!")
                race_is_on = False
            else:
                print(f"You lose. The {turtle.pencolor()} turtle won the race.")
                race_is_on = False

# red_tam = Turtle()
# red_tam.shape("turtle")
# red_tam.color("red")
# red_tam.penup()
# red_tam.goto(x=-240, y=-150)
# red_tam.forward(random.choice(num_steps))
#
# orange_tam = Turtle()
# orange_tam.shape("turtle")
# orange_tam.color("orange")
# orange_tam.penup()
# orange_tam.goto(x=-240, y=-100)
# orange_tam.forward(random.choice(num_steps))
#
# yellow_tam = Turtle()
# yellow_tam.shape("turtle")
# yellow_tam.color("yellow")
# yellow_tam.penup()
# yellow_tam.goto(x=-240, y=-50)
# yellow_tam.forward(random.choice(num_steps))
#
# green_tam = Turtle()
# green_tam.shape("turtle")
# green_tam.color("green")
# green_tam.penup()
# green_tam.goto(x=-240, y=0)
# green_tam.forward(random.choice(num_steps))
#
# blue_tam = Turtle()
# blue_tam.shape("turtle")
# blue_tam.color("blue")
# blue_tam.penup()
# blue_tam.goto(x=-240, y=50)
# blue_tam.forward(random.choice(num_steps))
#
# purple_tam = Turtle()
# purple_tam.shape("turtle")
# purple_tam.color("purple")
# purple_tam.penup()
# purple_tam.goto(x=-240, y=100)
# purple_tam.forward(random.choice(num_steps))
#
# pink_tam = Turtle()
# pink_tam.shape("turtle")
# pink_tam.color("pink")
# pink_tam.penup()
# pink_tam.goto(x=-240, y=150)
# pink_tam.forward(random.choice(num_steps))


screen.exitonclick()