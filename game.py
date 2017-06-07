#Space invaders using Turtle
import turtle
import os

#setting up the screen
window = turtle.Screen()
window.title("Space Invaders")
window.bgcolor("Black")

#draw the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("White")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)

border_pen.hideturtle()

#creating the player
player = turtle.Turtle()
player.color("Orange")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

delay = input("Press enter to finish")