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
#variables
score_1 = 0
timee = 30
gameeover = False
listing = []
indexing = 0
totalquestioncount = 0
questionquestion = "question.txt"
options = [option1,option2,option3,option4]




def draw():
    global timee
    screen.draw.filled_rect(marqueebox,"Blue")
    screen.draw.filled_rect(questionbox,"Red")
    screen.draw.filled_rect(timerbox,"White")
    screen.draw.filled_rect(option1,"Green")
    screen.draw.filled_rect(option2,"Green")
    screen.draw.filled_rect(option3,"Green")
    screen.draw.filled_rect(option4,"Green")
    screen.draw.filled_rect(skip,"Yellow")
    #Textboxes
    message = "welcome to the quiz app"
    screen.draw.textbox(message,marqueebox,color = "black")
    screen.draw.textbox(str(timee),timerbox,color = "black")
#Function for marquee box
def moving():
    marqueebox.x-=5
    if marqueebox.right < 0:
        marqueebox.left = 900

def countdown():
    global timee
    if timee>0:
        timee-=1

def update():
    pass
    moving()
clock.schedule_interval(countdown,1)
pgzrun.go()
