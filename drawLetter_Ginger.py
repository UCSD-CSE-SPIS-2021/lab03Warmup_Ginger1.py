import turtle
#draw my first initial (g) with the turtle!
'''draw a capital g, starting with the line from the center'''

def draw_G(the_turtle):
  #line of the G
  the_turtle.forward(50)
  the_turtle.right(90)
  the_turtle.forward(40)
  #right half of bottom curve
  for x in range(3):
    the_turtle.right(30)
    the_turtle.forward(20)
  #left half of bottom curve
  for x in range(3):
    the_turtle.forward(20)
    the_turtle.right(30)
  the_turtle.forward(90)
  for x in range(3):
    the_turtle.right(30)
    the_turtle.forward(20)
  for x in range(3):
    the_turtle.forward(20)
    the_turtle.right(30)

my_turtle = turtle.Turtle()
draw_G(my_turtle)

second_turtle = turtle.Turtle()
second_turtle.penup()
second_turtle.setpos(150,0)
second_turtle.pendown()
draw_G(second_turtle)

#turtle1.setpos(-50, -50)

