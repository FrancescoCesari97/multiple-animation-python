
from tkinter import *
from ball import *
import time

window = Tk()

WIDTH = 500
HEIGHT = 500


canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1, 2, "white")

tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, "yellow")

while True:
    volley_ball.move()
    tennis_ball.move()

    window.update()
    time.sleep(0.01)

window.mainloop()