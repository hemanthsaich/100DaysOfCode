# Hirst Painting

'''Part-1 Extract colors from image'''
#import colorgram
# rgb_color = []
# colors = colorgram.extract('download.jpg',20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color =(r,g,b)
#     rgb_color.append(new_color)
# print(rgb_color)

'''Part-2 Drawing dots'''
import turtle as ts
import random
ts.colormode(255)

chin = ts.Turtle()
chin.speed('fastest')
chin.penup()
chin.hide()

colors_list = [(243, 220, 103), (229, 72, 96), (226, 126, 153), (17, 116, 180), (5, 181, 222), (102, 182, 219), (8, 185, 138), (241, 161, 180), (245, 163, 151), (213, 91, 77), (108, 205, 154), (139, 218, 194), (171, 51, 97), (14, 136, 87)]

chin.setheading(225)
chin.forward(300)
chin.setheading(0)

no_of_dots = 100
for dot_count in range(1, no_of_dots + 1):
    chin.dot(20, random.choice(colors_list))
    chin.forward(50)

    if dot_count % 10 == 0:
        chin.setheading(90)
        chin.forward(50)
        chin.setheading(180)
        chin.forward(500)
        chin.setheading(0)


screen = ts.Screen()
screen.exitonclick()
