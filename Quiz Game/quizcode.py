import pgzrun
TITLE = "Quiz Game"
WIDTH = 900
LENGTH = 700
#Defining Boxes
marqueebox = Rect(0,0,900,150)
questionbox = Rect(0,150,650,150)
timerbox = Rect(750,150,150,150)
def draw():
    screen.draw.filled_rect(marqueebox,"Blue")
    screen.draw.filled_rect(questionbox,"Red")
    screen.draw.filled_rect(timerbox,"White")
    
pgzrun.go()
