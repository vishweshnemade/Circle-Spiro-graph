import turtle

turtle.Screen()

i = 1
while i>0:
    for j in ["red", "blue", "magenta", "green", "yellow", "white"]:
        turtle.color(j)
        turtle.circle(100)
        turtle.left(10)

turtle.clear()


turtle.mainloop()