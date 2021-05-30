import random
from turtle import Turtle, Screen
from random import randint

m = Turtle()
m.shape("turtle")
m.pensize(1)
m.speed("fastest")

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    # Using a tuple
    m.color(R, G, B)

for _ in range(120):
    change_color()
    m.circle(100)
    m.left(3)




















# # random walk
# m.forward(60)
# m.left(90)
# m.right(90)
# def change_color():
#     R = random.random()
#     G = random.random()
#     B = random.random()
#     # Using a tuple
#     m.color(R, G, B)
#
#
# for i in range(0, 300):
#     change_color()
#     choice = random.randint(1, 4)
#     if choice == 1:
#         m.right(90)
#     elif choice == 2:
#         m.left(90)
#     elif choice == 3:
#         m.forward(60)
#     elif choice == 4:
#         m.back(60)
#     print(choice)




# Project drawing the figures using functions
#
# def change_color():
#     R = random.random()
#     G = random.random()
#     B = random.random()
#     manu.color(R, G, B)
#
# def draw_shape(number_of_sides):
#     angle = 360/number_of_sides
#     for _ in range(number_of_sides):
#         manu.forward(100)
#         manu.right(angle)
#
#
#
# for i in range(3,11):
#     draw_shape(i)
#     change_color()



# Project drawing the figures using functions easy
# for _ in range(3):
#     manu.pencolor("chocolate")
#     manu.forward(100)
#     manu.right(90)
#
# for _ in range(4):
#     manu.pencolor("red")
#     manu.forward(100)
#     manu.right(90)
#
# for _ in range(5):
#     manu.pencolor("yellow")
#     manu.forward(100)
#     manu.right(72)
#
# for _ in range(6):
#     manu.color("green3")
#     manu.forward(100)
#     manu.right(60)
#
# for _ in range(7):
#     manu.color("blue")
#     manu.forward(100)
#     manu.right(51.43)
#
# for _ in range(8):
#     manu.color("black")
#     manu.forward(100)
#     manu.right(45)
#
# for _ in range(9):
#     manu.color("aquamarine")
#     manu.forward(100)
#     manu.right(40)
#
# for _ in range(10):
#     manu.color("azure")
#     manu.forward(100)
#     manu.right(36)


# for _ in range(20):
#     manu.pendown()
#     manu.forward(10)
#     manu.penup()
#     manu.forward(10)


screen = Screen()
screen.exitonclick()