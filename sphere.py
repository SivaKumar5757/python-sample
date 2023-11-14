from turtle import Turtle,Screen
dark=Turtle()
screen=Screen()
dark.hideturtle()
dark.speed(0)
dark.color("blue")
for i in range(360):
   dark.circle(100)
   current_heading=dark.heading()
   dark.setheading(current_heading+1)
   current_heading=int(current_heading)
screen.exitonclick()