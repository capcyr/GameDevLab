import pgzrun
TITLE = "Quiz Game"
WIDTH = 900
HEIGHT = 700
#Defining Boxes
marqueebox = Rect(0,0,900,150)
questionbox = Rect(0,150,750,150)
timerbox = Rect(750,150,150,150)
option1 = Rect(0,300,350,180)
option2 = Rect(370,300,350,180)
option3 = Rect(0,500,350,180)
option4 = Rect(370,500,350,180)
skip = Rect(750,300,200,750)
def draw():
    screen.draw.filled_rect(marqueebox,"Blue")
    screen.draw.filled_rect(questionbox,"Red")
    screen.draw.filled_rect(timerbox,"White")
    screen.draw.filled_rect(option1,"Green")
    screen.draw.filled_rect(option2,"Green")
    screen.draw.filled_rect(option3,"Green")
    screen.draw.filled_rect(option4,"Green")
    screen.draw.filled_rect(skip,"Yellow")
def update():
    pass
pgzrun.go()
