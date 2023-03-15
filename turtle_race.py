import turtle
import time

WIDTH, HEIGHT = 500, 500


def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Enter the number of racers (2 - 10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Input is not numeric... Try again!")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Number not in range 2-10. Try Again!")
            continue


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing")


racers = get_number_of_racers()
init_turtle()

racer = turtle.Turtle()
# racer.forward(100)
# racer.left(108)
# racer.forward(138)
# racer.back(18)
# racer.right(97)
# racer.forward(100)

# Make the turtle run in a loop

# Create a spiral through turtle movements
i = 0
while True:
    racer.forward(i)
    racer.left(90)
    i += 1


# time.sleep(5)
