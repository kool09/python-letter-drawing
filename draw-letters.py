# This program writes a sequence of letters using turtle
import math
import turtle
turtle.color("red")
turtle.shape('turtle')
turtle.speed(1000000)
turtle.bgcolor('purple')


START_X = -600
START_Y = 200
BOX_WIDTH = 80
BOX_GAP = 10
BOX_DISTANCE = BOX_WIDTH + BOX_GAP
BOX_DIAGONAL=int(BOX_WIDTH*math.sqrt(2))
############ def starts here ################################################
def go_to_box(row, column):
    newX = column * BOX_DISTANCE + START_X
    newY = -row * BOX_DISTANCE + START_Y
    turtle.pu()
    turtle.setposition(newX, newY)

def draw_square(width):
    """
    This function draws a square
    """
    turtle.setheading(0) #heading east
    turtle.pd()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.pu()

###### Main code starts here #######
def draw_letter_A():
    x=turtle.xcor()
    y=turtle.ycor()
    turtle.pd()
    turtle.goto(x+BOX_WIDTH/2,y+BOX_WIDTH)
    turtle.goto(x+BOX_WIDTH,y)
    turtle.goto(x+BOX_WIDTH*3/4,y+BOX_WIDTH/2)
    turtle.goto(x+BOX_WIDTH/4,y+BOX_WIDTH/2)
    turtle.pu()

def draw_letter_B():
    turtle.pu()
    turtle.setheading(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.pd()
    turtle.circle(BOX_WIDTH/4,180)
    turtle.setheading(0)
    turtle.circle(BOX_WIDTH/4,180)
    turtle.left(90)
    turtle.forward(BOX_WIDTH)
    turtle.pu()

def draw_letter_C():
    turtle.pu()
    turtle.setheading(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.pd()
    turtle.circle(BOX_WIDTH/2,-180)

def draw_letter_D():
    turtle.pd()
    turtle.setheading(0)
    turtle.circle(BOX_WIDTH/2,180)
    turtle.left(90)
    turtle.forward(BOX_WIDTH)
    turtle.pu()

def draw_letter_E():
    turtle.setheading(90)
    turtle.pd()
    turtle.forward(BOX_WIDTH)
    turtle.seth(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.back(BOX_WIDTH/2)
    turtle.setheading(-90)
    turtle.forward(BOX_WIDTH/2)
    turtle.setheading(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.backward(BOX_WIDTH/2)
    turtle.setheading(-90)
    turtle.forward(BOX_WIDTH/2)
    turtle.setheading(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.pu()

def draw_letter_F():
    turtle.setheading(90)
    turtle.pd()
    turtle.forward(BOX_WIDTH)
    turtle.seth(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.back(BOX_WIDTH/2)
    turtle.setheading(-90)
    turtle.forward(BOX_WIDTH/2)
    turtle.setheading(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.pu()

def draw_letter_G():
    draw_letter_C()
    turtle.circle(BOX_WIDTH/2,270)
    turtle.seth(180)
    turtle.forward(BOX_WIDTH/2)
    turtle.pu()

def draw_letter_H():
    turtle.setheading(90)
    turtle.pd()
    turtle.forward(BOX_WIDTH)
    turtle.back(BOX_WIDTH/2)
    turtle.setheading(0)
    turtle.forward(BOX_WIDTH)
    turtle.setheading(90)
    turtle.forward(BOX_WIDTH/2)
    turtle.back(BOX_WIDTH)
    turtle.pu()

def draw_letter_I():
    draw_letter_T()
    turtle.pd()
    turtle.setheading(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.seth(-90)
    turtle.forward(BOX_WIDTH)
    turtle.seth(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.back(BOX_WIDTH)
    turtle.pu()

def draw_letter_J():
    turtle.pu()
    turtle.forward(BOX_WIDTH/2)
    turtle.seth(90)
    turtle.forward(BOX_WIDTH)
    turtle.seth(0)
    turtle.pd()
    turtle.forward(BOX_WIDTH/2)
    turtle.back(BOX_WIDTH)
    turtle.forward(BOX_WIDTH/2)
    turtle.seth(-90)
    turtle.forward(BOX_WIDTH*3/4)
    turtle.circle(-BOX_WIDTH/4,180)

def draw_letter_K():
        turtle.pd()
        x=turtle.xcor()
        y=turtle.ycor()
        turtle.seth(90)
        turtle.forward(BOX_WIDTH)
        turtle.back(BOX_WIDTH/2)
        turtle.goto(x+BOX_WIDTH/2,y+BOX_WIDTH)
        turtle.goto(x,y+BOX_WIDTH/2)
        turtle.goto(x+BOX_WIDTH/2,y)
        turtle.pu()

def draw_letter_L():
    turtle.pd()
    turtle.seth(90)
    turtle.forward(BOX_WIDTH)
    turtle.forward(-BOX_WIDTH)
    turtle.seth(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.pu()

def draw_letter_M():
    x=turtle.xcor()
    y=turtle.ycor()
    turtle.pd()
    turtle.goto(x, y+BOX_WIDTH)
    turtle.goto(x+BOX_WIDTH/2,y)
    turtle.goto(x+BOX_WIDTH, y+BOX_WIDTH)
    turtle.seth(-90)
    turtle.forward(BOX_WIDTH)

def draw_letter_N():
    turtle.seth(90)
    turtle.pd()
    turtle.forward(BOX_WIDTH)
    turtle.seth(-45)
    turtle.forward(BOX_DIAGONAL)
    turtle.seth(90)
    turtle.forward(BOX_WIDTH)
    turtle.pu()

def draw_letter_O():
    turtle.seth(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.pd()
    turtle.circle(BOX_WIDTH/2)
    turtle.pu()

def draw_letter_P():
    turtle.pu()
    turtle.setheading(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.pd()
    turtle.seth(90)
    turtle.forward(BOX_WIDTH/2)
    turtle.seth(0)
    turtle.circle(BOX_WIDTH/4,180)
    turtle.setheading(0)
    turtle.left(90)
    turtle.forward(-BOX_WIDTH)
    turtle.pu()

def draw_letter_Q():
    draw_letter_O()
    turtle.seth(90)
    turtle.forward(BOX_WIDTH/2)
    turtle.seth(-45)
    turtle.pd()
    turtle.forward(BOX_DIAGONAL/2)
    turtle.pu()

def draw_letter_R():
    draw_letter_P()
    turtle.pd()
    turtle.seth(90)
    turtle.forward(BOX_WIDTH/2)
    turtle.seth(-45)
    turtle.forward(BOX_DIAGONAL/2)
    turtle.pu()

def draw_letter_S():
    turtle.pu()
    turtle.setheading(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.pd()
    turtle.circle(BOX_WIDTH/4,180)
    turtle.setheading(0)
    turtle.circle(BOX_WIDTH/4,-180)

def draw_letter_T():
    turtle.seth(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.seth(90)
    turtle.pd()
    turtle.forward(BOX_WIDTH)
    turtle.seth(0)
    turtle.forward(BOX_WIDTH/2)
    turtle.back(BOX_WIDTH)
    turtle.pu()

def draw_letter_U():
    turtle.pu()
    turtle.seth(90)
    turtle.forward(BOX_WIDTH)
    turtle.pd()
    turtle.back(BOX_WIDTH/2)
    turtle.seth(90)
    turtle.circle(-BOX_WIDTH/2,-180)
    turtle.seth(90)
    turtle.forward(BOX_WIDTH/2)
    turtle.pu()

def draw_letter_V():
    x=turtle.xcor()
    y=turtle.ycor()
    turtle.pu()
    turtle.goto(x,y+BOX_WIDTH)
    turtle.pd()
    turtle.goto(x+BOX_WIDTH/2,y)
    turtle.goto(x+BOX_WIDTH,y+BOX_WIDTH)

def draw_letter_W():
    x=turtle.xcor()
    y=turtle.ycor()
    turtle.pu()
    turtle.goto(x,y+BOX_WIDTH)
    turtle.pd()
    turtle.goto(x+BOX_WIDTH/4,y)
    turtle.goto(x+BOX_WIDTH/2,y+BOX_WIDTH)
    turtle.goto(x+BOX_WIDTH*3/4,y)
    turtle.goto(x+BOX_WIDTH,y+BOX_WIDTH)

def draw_letter_X():
    turtle.seth(45)
    turtle.pd()
    turtle.forward(BOX_DIAGONAL)
    turtle.seth(180)
    turtle.pu()
    turtle.forward(BOX_WIDTH)
    turtle.right(45)
    turtle.pd()
    turtle.forward(-BOX_DIAGONAL)
    turtle.pu()

def draw_letter_Y():
        turtle.seth(45)
        turtle.pd()
        turtle.forward(BOX_DIAGONAL)
        turtle.seth(180)
        turtle.pu()
        turtle.forward(BOX_WIDTH)
        turtle.right(45)
        turtle.pd()
        turtle.forward(-BOX_DIAGONAL/2)

def draw_letter_Z():
    turtle.pu()
    turtle.setheading(90)
    turtle.forward(BOX_WIDTH)
    turtle.pd()
    turtle.setheading(0)
    turtle.forward(BOX_WIDTH)
    turtle.right(-45)
    turtle.back(BOX_DIAGONAL)
    turtle.seth(0)
    turtle.forward(BOX_WIDTH)
    turtle.pu()


def draw_letter_at_box(letter,row,column):
    go_to_box(row,column)
    #draw_square(BOX_WIDTH)
    draw_letter(letter)
    print(row,column)

def draw_letter(letter):
    if (letter == 'A'):
        draw_letter_A()
    if (letter == 'B'):
        draw_letter_B()
    if (letter == 'C'):
        draw_letter_C()
    if (letter == 'D'):
        draw_letter_D()
    if (letter == 'E'):
        draw_letter_E()
    if (letter == 'F'):
        draw_letter_F()
    if (letter == 'G'):
        draw_letter_G()
    if (letter == 'H'):
        draw_letter_H()
    if (letter == 'I'):
        draw_letter_I()
    if (letter == 'J'):
        draw_letter_J()
    if (letter == 'K'):
        draw_letter_K()
    if (letter == 'L'):
        draw_letter_L()
    if (letter == 'M'):
        draw_letter_M()
    if (letter == 'N'):
        draw_letter_N()
    if (letter == 'O'):
        draw_letter_O()
    if (letter == 'P'):
        draw_letter_P()
    if (letter == 'Q'):
        draw_letter_Q()
    if (letter == 'R'):
        draw_letter_R()
    if (letter == 'S'):
        draw_letter_S()
    if (letter == 'T'):
        draw_letter_T()
    if (letter == 'U'):
        draw_letter_U()
    if (letter == 'V'):
        draw_letter_V()
    if (letter == 'W'):
        draw_letter_W()
    if (letter == 'X'):
        draw_letter_X()
    if (letter == 'Y'):
        draw_letter_Y()
    if (letter == 'Z'):
        draw_letter_Z()

def draw_alphabet():
    draw_letter_at_box("A", 0, 0)
    draw_letter_at_box("B", 0, 1)
    draw_letter_at_box("C", 0, 2)
    draw_letter_at_box("D", 0, 3)
    draw_letter_at_box("E", 0, 4)
    draw_letter_at_box("F", 0, 5)
    draw_letter_at_box("G", 0, 6)
    draw_letter_at_box("H", 0, 7)
    draw_letter_at_box("I", 0, 8)
    draw_letter_at_box("J", 0, 9)
    draw_letter_at_box("K", 0, 10)
    draw_letter_at_box("L", 0, 11)
    draw_letter_at_box("M", 0, 12)
    draw_letter_at_box("N", 1, 0)
    draw_letter_at_box("O", 1, 1)
    draw_letter_at_box("P", 1, 2)
    draw_letter_at_box("Q", 1, 3)
    draw_letter_at_box("R", 1, 4)
    draw_letter_at_box("S", 1 ,5)
    draw_letter_at_box("T", 1 ,6)
    draw_letter_at_box("U", 1 ,7)
    draw_letter_at_box("V", 1 ,8)
    draw_letter_at_box("W", 1 ,9)
    draw_letter_at_box("X", 1 ,10)
    draw_letter_at_box("Y", 1 ,11)
    draw_letter_at_box("Z", 1 ,12)

def write_text(text):
    column=0
    row=0
    for letter in text:
        draw_letter_at_box(letter,row, column)
        column=column+1
        if column==12:
            row=row+1
            column=0


def calledWhenOnClicked(x, y):
    text = turtle.textinput('Text Input', "Enter Text(letters and spaces only)")
    turtle.clear()
    write_text(text.upper())
    turtle.pu()
    turtle.home()

################################## entry starts here ###################
turtle.title('Turtle Text Drawing - Click the turtle to draw letters by entering text')

turtle.pensize(5)
turtle.pu()
turtle.home()
turtle.onclick(calledWhenOnClicked)
draw_alphabet()
turtle.home()
turtle.mainloop()
