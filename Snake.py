import turtle
import time
import random

delay = 0.1

# Ustawienia ekranu
screen = turtle.Screen()
screen.title("Gra Wąż")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

# Głowa węża
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Jedzenie
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("yellow")
food.penup()
food.goto(0, 100)

segments = []

# Funkcje sterujące
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# Klawisze
screen.listen()
screen.onkeypress(go_up, "w")
screen.onkeypress(go_down, "s")
screen.onkeypress(go_left, "a")
screen.onkeypress(go_right, "d")

# Funkcja do aktualizacji pozycji jedzenia
def update_food_position():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    food.goto(x // 20 * 20, y // 20 * 20)

# Główna pętla gry
while True:
    screen.update()

    # Sprawdzenie kolizji z granicami
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Ukryj segmenty
        for segment in segments:
            segment.goto(1000, 1000)
        
        # Wyczyść listę segmentów
        segments.clear()

    # Sprawdzenie kolizji z jedzeniem
    if head.distance(food) < 20:
        update_food_position()

        # Dodaj nowy segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.penup()
        segments.append(new_segment)

    # Przesuń segmenty węża
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()    

    # Sprawdzenie kolizji z ciałem węża
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            
            # Ukryj segmenty
            for segment in segments:
                segment.goto(1000, 1000)
            
            segments.clear()

    time.sleep(delay)

screen.mainloop()
