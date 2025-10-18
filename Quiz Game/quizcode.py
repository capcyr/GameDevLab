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
    screen.draw.textbox(question[0].strip(),questionbox,color = "black")
    q = 1
    for i in options:
        screen.draw.textbox(question[q].strip(),i, color = "black") 
        q +=1
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
#Reading the file
def reading():
    global totalquestioncount
    global indexing
    global listing 
    openfile = open("question.txt","r")
    for question in openfile:
        listing.append(question)
        totalquestioncount +=1
    openfile.close()

#Reading next question
def adding():
    global indexing
    indexing +=1
    return listing.pop(0).split(",")
    
def gammeover():
    global question, timee, gameeover
    gameeover = True
    timee = 0
    message = f"The quiz is over {score_1}"
    question = [message,"-","-","-","-",5]

def correctanswer():
    global timee, question,score_1,listing
    score_1+=1
    if listing:
        question = adding()
        timee = 30
    else:
        gammeover()

def on_mouse_down(pos):
    if listing and not gameeover:
        counter =1
        for box in options:
            if box.collidepoint(pos):

                if counter == int(question[5]):
                    correctanswer()
                else:
                    gammeover()
            counter+=1 
    
reading()
question = adding()
clock.schedule_interval(countdown,1)
pgzrun.go()


