import turtle
import time
import random

WIDTH, HEIGHT = 700, 600
COLORS = [
    "red",
    "green",
    "blue",
    "orange",
    "yellow",
    "black",
    "purple",
    "pink",
    "brown",
    "cyan",
]


class TurtleRacer:
    def __init__(self, color, position):
        self.turtle = turtle.Turtle()
        self.turtle.color(color)
        self.turtle.shape("turtle")
        self.turtle.left(90)
        self.turtle.penup()
        self.turtle.setpos(position)
        self.turtle.pendown()

    def move(self):
        distance = random.randrange(1, 20)
        self.turtle.forward(distance)

    def get_position(self):
        return self.turtle.pos()


def get_number_of_racers():
    while True:
        try:
            racers = int(input("Enter the number of racers (2 - 10): "))
            if 2 <= racers <= 10:
                return racers
            else:
                print("Number not in range 2-10. Try Again!")
        except ValueError:
            print("Input is not numeric... Try Again!")


def race(colors):
    racers = [
        TurtleRacer(
            color,
            (-WIDTH // 2 + (i + 1) * (WIDTH // (len(colors) + 1)), -HEIGHT // 2 + 20),
        )
        for i, color in enumerate(colors)
    ]
    while True:
        for racer in racers:
            racer.move()
            x, y = racer.get_position()
            if y >= HEIGHT // 2 - 10:
                return colors[racers.index(racer)]


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")


racers = get_number_of_racers()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:racers]

winner = race(colors)
print("The winner is the turtle with color:", winner)
time.sleep(5)
