from turtle import *


#we want to paint a house

#step 1: draw a square
speed(15)
shape ("arrow")
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120)     #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()
color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#draw a window

left(30)
color("blue")
begin_fill()
forward(60)
left(90)
forward(60)
left(90)
forward(55)
left(90)
forward(60)
penup()
goto(200, 200)
pendown()
forward(60)
left(90)
forward(60)
left(90)
forward(60)
left(90)
forward(60)
end_fill()

exitonclick()