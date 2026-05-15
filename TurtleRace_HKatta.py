"""
Turtle Race Betting Game
Author: Hyndavi Katta
Description: Pick a color, then watch 6 turtles race across the screen.
The program announces the winner and tells you if your bet was correct.
"""

import turtle
import random
import time

# Setup screen
screen = turtle.Screen()
screen.setup(800, 600)
screen.title("Turtle Race - Place Your Bet!")
screen.bgcolor("lightgreen")

# Ask user for bet
colors = ["red", "blue", "orange", "purple", "yellow", "pink"]
user_bet = ""
while user_bet not in colors:
    user_bet = screen.textinput(
        "Place your bet",
        f"Which turtle will win? ({', '.join(colors)})"
    ).strip().lower()

# Draw finish line
line_drawer = turtle.Turtle()
line_drawer.hideturtle()
line_drawer.penup()
line_drawer.goto(350, 200)
line_drawer.right(90)
line_drawer.pendown()
line_drawer.pensize(3)
line_drawer.forward(400)

# Create turtles
y_positions = [-150, -90, -30, 30, 90, 150]
all_turtles = []
for i in range(6):
    new_turtle = turtle.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(-380, y_positions[i])
    all_turtles.append(new_turtle)

# Race loop
race_on = True
winner = ""
while race_on:
    for t in all_turtles:
        t.forward(random.randint(1, 8))
        if t.xcor() >= 350:
            winner = t.pencolor()
            race_on = False
            break

# Announce winner
time.sleep(0.5)
screen.clear()
screen.bgcolor("lightgreen")
result_turtle = turtle.Turtle()
result_turtle.hideturtle()
result_turtle.penup()
result_turtle.goto(0, 50)
result_turtle.write(
    f"The winner is the {winner} turtle!",
    align="center",
    font=("Arial", 24, "bold")
)
result_turtle.goto(0, -20)
if user_bet == winner:
    message = f"You bet on {user_bet}. You win!"
else:
    message = f"You bet on {user_bet}. Better luck next time."
result_turtle.write(message, align="center", font=("Arial", 18, "normal"))

# Keep window open until click
screen.exitonclick()