import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    Yuma=turtle.Turtle()
    Yuma.shape("turtle")
    Yuma.color("blue")

    shape=simpledialog.askstring(title="Shape?", prompt="What shape would you like me, Yuma the blue turtle, to draw? (enter 'square', 'circle', or 'triangle' in the box down below)")

    if shape == "square":

        Yuma.forward(100)
        Yuma.right(90)
        Yuma.forward(100)
        Yuma.right(90)
        Yuma.forward(100)
        Yuma.right(90)
        Yuma.forward(100)

    if shape == "circle":

        Yuma.circle(radius=88)

    if shape == "triangle":

        Yuma.forward(100)
        Yuma.right(120)
        Yuma.forward(100)
        Yuma.right(120)
        Yuma.forward(100)
    # Make a new turtle
    
    # Ask the user what shape they want to draw and store it in a variable
    
    # Draw the shape requested by the user using if-elif-else statements
    
    # Call the turtle .done() method
    turtle.done()