import turtle as t
import time
import math
t.speed(0)
t.colormode(255)
t.ht()
s = t.Screen()

yes = ["Yes", "yes", "Y", "y"]
cor = [[],[]]
pieces = [[], []]
turn = 2
global fromMenu
fromMenu = True
resignWin = False
global runner
runner = True
global draw
draw = False
global tie
tie = False
global array
array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

text = t.Turtle()
text.pu()
text.ht()

def startAnimation():
    t.pencolor(184,156,64)
    t.bgcolor(184,156,64)
    #NAME
    s.tracer(0)
    text.pencolor("black")
    text.goto(-32, 32)
    text.write("A game by", font = ("Calibri", 10, "normal"))
    text.goto(-65, -0)
    text.write("Joey Zhang", font = ("Calibri", 20, "bold"))
    s.update()
    time.sleep(2)
    text.clear()
    s.update()

    time.sleep(1)

    # NORD VPN
    text.goto(-50, -50)
    t.goto(29, 70)
    s.tracer(0)
    t.fillcolor("white")
    t.seth(-230)
    t.begin_fill()
    t.circle(58)
    t.end_fill()
    t.fillcolor(70, 135, 255)
    t.begin_fill()
    t.seth(240)
    t.fd(50)
    t.rt(120)
    t.fd(20)
    t.lt(160)
    t.fd(20)
    t.seth(240)
    t.fd(20)
    t.rt(120)
    t.fd(40)
    t.lt(160)
    t.fd(15)
    t.seth(240)
    t.fd(5)
    t.seth(-240)
    t.fd(56)
    t.seth(230)
    t.circle(58, 260)
    t.end_fill()
    s.update()

    s.tracer(0)
    text.pencolor("black")
    text.pu()
    text.goto(-50, 95)
    text.write("Sponsored by", font = ("Calibri", 10, "normal"))
    text.goto(-100, -80)
    text.write("South VPN", font = ("Calibri", 30, "bold"))
    s.update()

    time.sleep(2)
    t.clear()
    text.clear()
    s.update()


    time.sleep(1)

    R = 20
    speed = 4
    rotspeed = speed - 0.5

    #LOADING SCREEN
    for i in range(int(525/speed)):
        s.tracer(0)
        t.goto(speed*i-250, -30)

        t.seth(180)
        t.pd()
        t.fillcolor("white")
        t.begin_fill()
        t.fd(i*speed)
        t.lt(90)
        t.fd(2*R)
        t.lt(90)
        t.fd(i*speed)
        t.end_fill()
        t.fd(525-i*speed)
        t.lt(90)
        t.fd(2*R)
        t.lt(90)
        t.fd(525-i*speed)
        t.pu()

        t.goto(speed*i-250, -50)
        t.seth(-4*i*rotspeed)
        t.fd(R)
        t.pd()
        t.lt(90)
        
        t.begin_fill()
        t.circle(R, -360, 360)
        t.end_fill()
        t.fillcolor("black")
        t.begin_fill()
        t.circle(R/2, -180, 180)
        t.circle(-R/2, -180, 180)
        t.circle(-R, 180, 180)
        t.end_fill()

        t.rt(90)
        t.pu()
        t.fd(0.4*R)
        t.pd()
        t.rt(90)
        t.color("white")
        t.begin_fill()
        t.circle(R/10, 360, 360)
        t.end_fill()
        t.lt(90)
        t.pu()
        t.fd(R)
        t.pd()
        t.rt(90)
        t.color("black")
        t.begin_fill()
        t.circle(R/10, 360, 360)
        t.end_fill()
        t.lt(90)
        t.pu()
        t.bk(0.4*R)
        s.update()
        s.tracer(0)
        text.color("black")
        text.goto(-35, -100)
        if i % 9 == 0:
                text.clear()
                text.write("Loading"+((i % 36)//9)*".", font = ("Calibri", 15, "bold"))
                s.update()
        t.clear()
    
    t.pd()
    text.clear()
    for i in range(25):
        t.goto(0, 0)
        s.tracer(0)
        t.color("gray" + str(4*i))
        t.dot(i**math.log(670, 25))
        s.update()
        t.clear()
        time.sleep(0.002)
    s.bgcolor("white")
    time.sleep(0.8)
    t.clearscreen()

def start():
    t.colormode(255)
    t.bgcolor(184,156,64)
    t.fillcolor("#b3b3b3")
    t.ht()
    s.tracer(0)
    t.pu()
    t.goto(-200, 100)
    t.pd()
    for i in range(3):
        t.begin_fill()
        for i in range(2):
            t.fd(400)
            t.rt(90)
            t.fd(60)
            t.rt(90)
        t.end_fill()
        t.pu()
        t.rt(90)
        t.fd(100)
        t.seth(0)
        t.pd()
    t.pu()
    t.goto(-162, 200)
    t.write("GOMOKU", font = ("Times New Roman", 50, "bold"))
    t.goto(-80, 50)
    t.write("Play Game", font = ("Calibri", 25, "bold"))
    t.goto(-88, -50)
    t.write("Instructions", font = ("Calibri", 25, "bold"))
    t.goto(-78, -150)
    t.write("Exit Game", font = ("Calibri", 25, "bold"))
    s.update()

def board():
    s.tracer(0)
    for i in range(19):
        t.goto(-225, -250+i*30)
        t.pd()
        for i in range(19):
            for i in range(4):
                t.fd(30)
                t.rt(90)
            t.fd(30)
        t.pu()
    s.update()

def stallboard():
    t.pu()
    s.tracer(0)
    for i in range(19):
        t.goto(-225, -250+i*30)
        for i in range(19):
            for i in range(4):
                t.fd(30)
                t.rt(90)
            t.fd(30)
    s.update()
    t.pd()

def piece(x, y):
    global turn
    s.onclick(None)
    if -240 < x < 360 and -295 < y < 305:
        if (x + 225) % 30 > 15:
            x += 30 - ((x + 225) % 30)
        else:
            x -= (x + 225) % 30
        if (y + 280) % 30 > 15:
            y += 30 - ((y + 280) % 30)
        else:
            y -= (y + 280) % 30
        y -= 13
        t.goto(x, y)
        t.pd()
        overlap = 0
        for i in range(2):
            for j in range(len(cor[i])):
                if (int((x + 225) / 30), int((y + 293) / 30)) == cor[i][j]:
                    overlap += 1
        if overlap == 0:
            if turn % 2 == 0:
                t.fillcolor("white")
                cor[0].append((int((x + 225) / 30), int((y + 293) / 30)))
                pieces[0].append((x, y))
                array[19-int((y + 293) / 30)][int((x + 225) / 30)] = 1 
            else:
                t.fillcolor("black")
                cor[1].append((int((x + 225) / 30), int((y + 293) / 30)))
                pieces[1].append((x, y))
                array[19-int((y + 293) / 30)][int((x + 225) / 30)] = 2
            t.begin_fill()
            t.circle(13)
            t.end_fill()
            t.pu()
            turn += 1
        return
    else:
        if -250 > x > -300 and 240 < y < 290:
            settings()
        elif -360 < x < -240:
            if-290 < y < -250:
                if t.textinput("Resignation", "Are you sure?") in yes:
                    global resignWin
                    resignWin = True
            elif -230 < y < -190:
                if turn % 2 == 0:
                    drawOffer = ["Black", "white"]
                else:
                    drawOffer = ["White", "black"]
                if t.textinput("Offer Draw", drawOffer[0] + ", do you accept " + drawOffer[1] + "'s draw offer?") in yes:
                    global draw
                    draw = True
    
def winButtons(x, y):
    if -150 < x < 150:
        if 50 > y > -15:
            t.clear()
            reset()
            game()
        elif -75 > y > -130:
            reset()
            full()

def win():
    t.pu()
    t.goto(-200, 200)
    t.pd()
    t.fillcolor("#8f8f8f")
    t.begin_fill()
    for i in range(4):
        t.fd(400)
        t.rt(90)
    t.end_fill()
    t.pu()
    if not draw:
        t.goto(-140, 120)
        if turn % 2 == 0:
            t.write("BLACK WINS!", font = ("Times New Roman", 30, "bold"))
        else:
            t.write("WHITE WINS!", font = ("Times New Roman", 30, "bold"))
        if not resignWin:
            t.goto(-60, 95)
            t.write("From 5 in a row", font = ("Calibri", 13, "normal"))
        else:
            t.goto(-63, 95)
            t.write("From resignation", font = ("Calibri", 13, "normal"))
    else:
        t.goto(-68, 120)
        t.write("DRAW!", font = ("Times New Roman", 30, "bold"))
        if tie:
            t.goto(-33, 95)
            t.write("From tie", font = ("Calibri", 13, "normal"))
        else:
            t.goto(-60, 95)
            t.write("From agreement", font = ("Calibri", 13, "normal"))


    t.goto(-150, 50)
    t.fillcolor("#b3b3b3")
    for i in range(2):
        t.pd()
        t.begin_fill()
        for j in range(2):
            t.fd(300)
            t.rt(90)
            t.fd(65)
            t.rt(90)
        t.end_fill()
        t.pu()
        t.goto(-150, -75)
    t.goto(-78, -2)
    t.write("New Game", font = ("Calibri", 25, "bold"))
    t.goto(-83, -127)
    t.write("Main Menu", font = ("Calibri", 25, "bold"))
    while runner == True:
        s.onclick(winButtons)
        stallboard()
        time.sleep(1)

def drawPieces():
    t.fillcolor("white")
    for color in range(2):
        for i in pieces[color]:
            t.goto(i[0], i[1])
            t.pd()
            t.begin_fill()
            t.circle(13)
            t.end_fill()
            t.pu()
        t.fillcolor("black")

def winCondition():
    if turn == 363:
        draw = True
        return
    
    if turn % 2 == 0:
        thing = 2
    else:
        thing = 1
    
    for row in range(19):
        for col in range(14):
            match = True
            for i in range(5):
                if thing != array[row][col+i]: match = False
            if match: return True

    for row in range(14):
        for col in range(19):
            match = True
            for i in range(5):
                if thing != array[row+i][col]: match = False
            if match: return True

    for row in range(14):
        for col in range(14):
            match = True
            for i in range(5):
                if thing != array[row+i][col+i]: match = False
            if match: return True

    for row in range(14):
        for col in range(14):
            match = True
            for i in range(5):
                if thing != array[row-i][col+i]: match = False
            if match: return True

    return False 
                    

def game():  
    board()
    settingsGear()
    resignFlag()
    drawPieces()
    text.goto(-360, 50)
    while runner == True:
        s.tracer(0)
        s.update()
        s.onclick(piece)
        if turn % 2 == 0:
            text.write("TURN  " + str(turn//2) + "\n    ---\n WHITE", font = ("Calibri", 15, "bold"))
        else:
            text.write("TURN  " + str(turn//2) + "\n    ---\n BLACK", font = ("Calibri", 15, "bold"))
        text.clear()
        if winCondition() or resignWin or draw:
            win()
            reset()
            full()
        time.sleep(0.25)

def reset():
    global cor
    global resignWin
    global turn
    global pieces
    global draw
    global tie
    global array
    array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    cor = [[], []]
    pieces =[[], []]
    turn = 2
    resignWin = False
    draw = False
    tie = False

def instructionPieces(x, y):
    t.pu()
    t.goto(x, y)
    t.pd()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

def returnButton(x, y):
    if 250 > x > 100 and -155 > y > -215:
        t.clear()
        if fromMenu:
            full()
        else:
            game()

        
def instructions():
        s.tracer(0)
        t.pu()
        t.goto(-180, 170)
        t.write("INSTRUCTIONS", font = ("Times New Roman", 30, "bold"))
        t.goto(-350, 50)
        t.write("Gomoku, or Five in a Row, is a two-player turn-based strategy board game. The name explains \nthe premise: whoever gets five in a row first wins. These can be horizontal, vertical, or diagonal. \nTo place a piece, simply left-click a square. The pieces are placed on the line intersections \nand will be snapped in by their hitboxes. Once the first person has placed their first piece, \nthe piece color automatically switches for the second player.", font = ("Calibri", 13, "normal"))
        t.goto(-200, -40)
        t.write("GOOD LUCK!", font = ("Times New Roman", 40, "bold"))

        t.goto(-350, -50)
        t.pd()
        for i in range(4):
            t.fd(250)
            t.rt(90)
        for i in range(2):
            t.fd(25)
            for i in range(5):
                t.rt(90)
                t.fd(250)
                t.bk(250)
                t.lt(90)
                t.fd(50)
            t.pencolor("#b89c4c")
            t.bk(25)
            t.pencolor("black")
            t.rt(90)
        t.fillcolor("black")
        instructionPieces(-275, -155)
        instructionPieces(-225, -205)
        instructionPieces(-175, -155)
        t.fillcolor("white")
        instructionPieces(-225, -155)
        instructionPieces(-225, -105)
        instructionPieces(-175, -205)

        t.pu()
        t.goto(100, -155)
        t.seth(0)
        t.pd()
        t.fillcolor("#b3b3b3")
        t.begin_fill()
        for i in range(2):
            t.fd(150)
            t.rt(90)
            t.fd(60)
            t.rt(90)
        t.end_fill()
        t.pu()
        t.goto(123, -200)
        t.write("Return >>", font = ("Calibri", 20, "bold"))
        s.update()
        while runner == True:
            stallboard()
            s.onclick(returnButton)

def exitGame():
    if t.textinput("Exit Game", "Are you sure?") in yes:
            global runner
            runner = False
            quit()
    else:
        start()

def button(x, y):
    if -200 < x < 200:
        if 40 < y < 100:
            t.clear()
            game()
            return
        elif -60 < y < 0:
            t.clear()
            global fromMenu
            fromMenu = True
            instructions()
        elif -160 < y < -100:
            exitGame()
        else:
            pass
    else:
        pass     

def full():
    t.clear()
    start()
    while runner == True:
        s.tracer(0)
        s.onclick(button)
        s.update()
        time.sleep(1)
    quit()

def settingsGear():
    s.tracer(0)
    t.fillcolor("#8f8f8f")
    t.pu()
    t.goto(-85/4-280, 45/4+280)
    t.pd()
    t.begin_fill()
    for i in range(4):
        t.fd(50)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(-280, 280)
    t.pd()
    t.fillcolor("#b3b3b3")
    t.begin_fill()
    for i in range(8):
        t.lt(90)
        for i in range(3):
            t.fd(6.25)
            t.rt(90)
        t.rt(180)
        t.circle(-6.25, 45)
    t.end_fill()
    t.pu()
    t.goto(13/4-280, -85/4+280)
    t.pd()
    t.fillcolor("#8f8f8f")
    t.begin_fill()
    t.circle(7.5)
    t.end_fill()
    t.pu()
    s.update()

def settingsButton(x, y):
    if -50 < x < 200:
        if 40 < y < 125:
            t.clear()
            game()
        elif -75 < y < 0:
            t.clear()
            global fromMenu
            fromMenu = False
            instructions()
        elif -200 < y < -125:
            if t.textinput("Main Menu", "Are you sure?") in yes:
                reset()
                full()
        else:
            pass
    else:
        pass 

def settings(): 
    s.tracer(0)
    t.pu()
    t.goto(-250, 250)
    t.pd()
    t.fillcolor("#8f8f8f")
    t.begin_fill()
    for i in range(4):
        t.fd(500)
        t.rt(90)
    t.end_fill()
    t.pu()
    t.goto(-200, 125)
    for i in range(3):
        t.pd()
        t.fillcolor("#b3b3b3")
        t.begin_fill()
        for j in range(2):
            t.fd(400)
            t.rt(90)
            t.fd(75)
            t.rt(90)
        t.end_fill()
        t.pu()
        t.rt(90)
        t.fd(125)
        t.seth(0)
    t.goto(-170, 150)
    t.write("SETTINGS", font = ("Times New Roman", 50, "bold"))
    t.goto(-70, 68)
    t.write("Continue", font = ("Calibri", 25, "bold"))
    t.goto(-85, -57)
    t.write("Instructions", font = ("Calibri", 25, "bold"))
    t.goto(-85, -182)
    t.write("Main Menu", font = ("Calibri", 25, "bold"))
    time.sleep(1)
    s.update()

    while runner == True:
        stallboard()
        s.onclick(settingsButton)

def resignFlag():
    s.tracer(0)
    t.pu()
    t.goto(-360, -190)
    for i in range(2):
        t.pd()
        t.fillcolor("#8f8f8f")
        t.begin_fill()
        for i in range(2):
            t.fd(120)
            t.rt(90)
            t.fd(40)
            t.rt(90)
        t.end_fill()
        t.pu()
        t.goto(-360, -250)
    t.pu()
    t.goto(-355, -265)
    t.pd()
    t.fillcolor("black")
    t.begin_fill()
    t.rt(45)
    for i in range(2):
        t.fd(25)
        t.circle(-1, 180)
    t.lt(45)
    t.circle(8, 60)
    t.rt(180)
    t.circle(8, -60)
    t.seth(45)
    t.circle(-1, 90)
    t.fd(10)
    t.circle(-1, 90)
    t.rt(45)
    t.circle(8, 60)
    t.rt(180)
    t.circle(8, -60)
    t.end_fill()
    t.pu()
    t.goto(-325, -285)
    t.write("RESIGN", font = ("Calibri", 17, "bold"))
    t.goto(-353, -213)
    t.write(1, font = ("Calibri", 15, "bold"))
    t.goto(15-353, -15-213)
    t.write(2, font = ("Calibri", 15, "bold"))
    t.goto(-321, -225)
    t.write("DRAW", font = ("Calibri", 17, "bold"))
    t.goto(19-352, 13-212)
    t.seth(230)
    t.pd()
    t.pensize(3)
    t.fd(30)
    t.pensize(1)
    t.seth(0)
    s.update()
    t.pu()

startAnimation()
full()