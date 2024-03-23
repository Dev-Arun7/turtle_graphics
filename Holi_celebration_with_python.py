# # Import the turtle graphics library
# import turtle
# import random

# # Create a drawing screen
# screen = turtle.Screen()
# screen.title("Holi Celebration with Turtle")
# # Set the background color of the screen
# screen.bgcolor("white")

# # Create a turtle named 'holi'
# holi = turtle.Turtle()
# holi.speed(0)  # This sets the drawing speed to the fastest

# # Define a list of colors to represent the Holi colors
# colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink']

# # Define a function to draw a circle using random colors
# def draw_circle():
#     holi.color(random.choice(colors))  # Choose a random color
#     holi.begin_fill()  # Begin to fill color in a circle
#     holi.circle(random.randint(10, 50))  # Draw a circle with a random radius between 10 and 50
#     holi.end_fill()  # End filling the circle with color

# # Move the turtle to a random position on the screen
# def move_turtle():
#     holi.penup()  # Don't draw when moving to a new position
#     holi.goto(random.randint(-300, 300), random.randint(-300, 300))  # Move to a random position
#     holi.pendown()  # Start drawing again

# # Main loop to draw 50 colored circles
# for _ in range(50):
#     draw_circle()
#     move_turtle()

# # Hide the turtle after drawing
# holi.hideturtle()

# # Keeps the window open until it is manually closed
# turtle.done()








# # Import the turtle graphics library
# import turtle
# import random

# # Setup the drawing screen
# screen = turtle.Screen()
# screen.title("Holi Celebration with Turtle - More Attractive!")
# screen.bgcolor("black")  # Change background to black for contrast

# # Create a turtle named 'holi'
# holi = turtle.Turtle()
# holi.speed(0)

# # Define a list of bright colors
# colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'magenta']

# # Function to draw spirals of varying sizes and colors
# def draw_spiral():
#     for i in range(36):  # Draw a circle made of 36 squares
#         holi.color(random.choice(colors))
#         holi.circle(100, steps=4)  # Draw a square as part of the circle
#         holi.right(10)  # Turn a bit for the spiral effect

# # Function to draw flowers
# def draw_flower():
#     for i in range(36):
#         holi.color(random.choice(colors))
#         holi.circle(100, steps=6)  # Draw a hexagon as part of the flower
#         holi.right(10)

# # Function to draw stars
# def draw_star():
#     for i in range(50):
#         holi.color(random.choice(colors))
#         holi.penup()
#         holi.goto(random.randint(-300, 300), random.randint(-200, 200))
#         holi.pendown()
#         for i in range(5):
#             holi.forward(50)
#             holi.right(144)  # Star angle

# # Draw the patterns
# draw_spiral()
# holi.penup()
# holi.goto(-100, -100)  # Move the turtle to a new location
# holi.pendown()
# draw_flower()
# draw_star()

# # Hide the turtle after drawing
# holi.hideturtle()

# # Keeps the window open until it is manually closed
# turtle.done()








# # Import the turtle graphics library
# import turtle
# import random

# # Create a drawing screen
# screen = turtle.Screen()
# screen.title("Holi Celebration with Turtle")
# # Set the background color of the screen
# screen.bgcolor("black")  # Changed to black for more vibrant colors

# # Create a turtle named 'holi'
# holi = turtle.Turtle()
# holi.speed(0)  # This sets the drawing speed to the fastest

# # Define a list of colors to represent the Holi colors
# colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'magenta']

# # Function to draw spirals of circles
# def draw_spiral():
#     for i in range(10):
#         holi.color(random.choice(colors))
#         holi.circle(i * 2)
#         holi._rotate(360 / 10)  # Use the private method _rotate for simplicity; normally, we should avoid using private methods

# # Define a function to draw a splash with random circles
# def draw_splash():
#     holi.penup()
#     x, y = random.randint(-300, 300), random.randint(-300, 300)
#     holi.goto(x, y)
#     holi.pendown()
#     for _ in range(random.randint(6, 10)):  # Draw 6 to 10 circles to form a splash
#         splash_size = random.randint(5, 20)
#         holi.color(random.choice(colors))
#         holi.begin_fill()
#         holi.circle(splash_size)
#         holi.end_fill()
#         # Move a bit for the next circle
#         holi.penup()
#         holi.goto(x + random.randint(-20, 20), y + random.randint(-20, 20))
#         holi.pendown()

# # Draw spirals and splashes
# for _ in range(10):  # Draw 10 spirals
#     draw_spiral()
#     holi.penup()
#     holi.goto(random.randint(-300, 300), random.randint(-300, 300))
#     holi.pendown()

# for _ in range(15):  # Draw 15 splashes
#     draw_splash()

# # Hide the turtle after drawing
# holi.hideturtle()

# # Keeps the window open until it is manually closed
# turtle.done()









# Import the turtle graphics library
import turtle
import random

# Set up the drawing screen
screen = turtle.Screen()
screen.title("Holi Celebration with Turtle - Amazing Version!")
screen.bgcolor("black")  # Changing the background to black for colors to pop

# Create a turtle named 'holi'
holi = turtle.Turtle()
holi.speed(0)  # Fastest drawing speed

# Enhance the list of colors for more variety
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'cyan', 'magenta', 'gold']

# Function to draw a circle with a more dynamic, sparkly effect
def draw_sparkly_circle():
    for _ in range(36):  # Create a loop to make the circle more complex
        holi.color(random.choice(colors))  # Choose a random color
        holi.circle(random.randint(20, 100))  # Random radius for bigger, bolder circles
        holi.right(10)  # Slight turn to create a sparkling effect

# Function to move the turtle to a random position and leave a trail of stars
def move_turtle_with_trail():
    for _ in range(10):  # Draw 10 stars leading to the next circle
        star_position_x = random.randint(-300, 300)
        star_position_y = random.randint(-300, 300)
        holi.penup()
        holi.goto(star_position_x, star_position_y)
        holi.pendown()
        draw_star(random.choice(colors), random.randint(5, 20))

# Function to draw a star for the trail effect
def draw_star(color, size):
    angle = 120  # Angle for the star points
    holi.fillcolor(color)
    holi.begin_fill()

    for side in range(5):
        holi.forward(size)
        holi.right(angle)
        holi.forward(size)
        holi.right(72 - angle)
    holi.end_fill()

# Main loop to draw 10 sparkly circles with star trails
holi.penup()
for _ in range(10):
    holi.goto(random.randint(-300, 300), random.randint(-300, 300))
    holi.pendown()
    draw_sparkly_circle()
    move_turtle_with_trail()

# Hide the turtle after drawing and show the result
holi.hideturtle()

# Keeps the window open until it is manually closed
turtle.done()











