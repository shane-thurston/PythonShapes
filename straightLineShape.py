from turtle import *
t = Turtle()
t.speed(0)
#Blue pattern
t.color('blue')
x = 200
y = 10
for i in range(10):
  t.penup()
  t.goto(0,y)
  t.pendown()
  t.goto(x,0)
  x -= 20
  y += 20
