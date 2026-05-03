import turtle
turtle.Screen().bgcolor("blue")
turtle.Screen().setup(600,600)
polygon = turtle.Turtle()

num_sides = 4
side_length = 200
angle = 360.0 / num_sides

for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)

turtle.done()
