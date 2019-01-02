import turtle
t = turtle.Pen()
t.speed(0)


def draw_square(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def draw_triangle(length):
    for i in range(3):
        t.forward(length)
        t.left(120)

def draw_pentagon(length):
    for i in range(5):
        t.forward(length)
        t.left(72)

def draw_hexagon(length):
    for i in range(6):
        t.forward(length)
        t.left(60)

def square_spirals(spacing,angle):
    for i in range(50):
        t.forward(i*spacing)
        t.left(angle)

def colorfil_spirals(spacing,angle):
    colors=['red','green','yellow','blue']
    turtle.bgcolor("black")
    t.pensize(3)
    for i in range(50):
        t.pencolor(colors[i%4])
        t.forward(i*spacing)
        t.left(angle)    

def divmod(n,m):
    quot = n // m
    remainder = n%m
    return(quot,remainder)

def count_matches(lst1,lst2):
    counter=0
    if len(lst1) == len(lst2):
        for i in range(len(lst1)):
            if lst1[i]==lst2[i]:
                print(lst1[i], " in position ", i, " matches.")
                counter=counter+1
    else:
        print("lists don't have the same length.")

def student_scores():
    scores = (79,85,99,83,91)
    for i in range(len(scores)):
        print(scores[i])
