from turtle import Turtle, Screen, colormode
import random

# import colorgram

colormode(255)  # change the color mode. for more details read the turtle documentation

timmy = Turtle()
timmy.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    # return r, g, b
    random_generated_color = (r, g, b)
    return random_generated_color


# # drawing dashed line
# for i in range(10):
#     timmy.forward(10)
#     if i % 2 == 0:
#         timmy.penup()
#     else:
#         timmy.pendown()

# drawing shapes
# colors = ["DeepSkyBlue2", "firebrick", "LightPink3", "MediumPurple3", "LightSteelBlue4", "wheat3", "yellow2"]
#
# for i in range(3, 11):
#     a = 0
#     timmy.color(random.choice(colors))
#     while a != i:
#         timmy.right(360 / i)
#         timmy.forward(100)
#         a += 1

# drawing random walk
# direction = [0, 90, 180, 270]
# colors = ["DeepSkyBlue2", "firebrick", "LightPink3", "MediumPurple3", "LightSteelBlue4", "wheat3", "yellow2", "olive",
#           "pink", "purple"]
# timmy.pensize(10)
# timmy.speed("fast")
# timmy.hideturtle()
# # timmy.shape("classic")
# # timmy.shapesize(2, 2)
#
# for i in range(251):
#     timmy.color(random.choice(colors))
#     timmy.forward(20)
#     # timmy.right(random.choice(direction))
#     timmy.setheading(random.choice(direction))

# drawing spirograph
# def draw_spirograph(size_of_gap):
#     timmy.speed("fastest")
#     timmy.shape("classic")
#     for i in range(360 // size_of_gap):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + size_of_gap)
#
#
# draw_spirograph(5)


# colors = colorgram.extract('hirst_painting.jpg', 10)
# # logic of extract color in RGB tuple format from the colorgram
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_rgb_color = (r, g, b)
#     rgb_colors.append(new_rgb_color)
# print(rgb_colors)

rgb_colors = [(223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159),
              (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93)]

timmy.penup()
timmy.hideturtle()
timmy.speed("fastest")
x = -225
y = -225

for i in range(1, 101):
    timmy.goto(x, y)
    timmy.color(random.choice(rgb_colors))
    timmy.dot(20)
    x += 50

    if i % 10 == 0:
        x = -225
        y += 50

screen = Screen()
screen.exitonclick()
