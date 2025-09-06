import pgzrun
import random
TITLE = "Shoot the alien"
#ScreenSize
WIDTH = 500
HEIGHT = 600
#Creating Actors
Alienthatisgoingtobeshot=Actor("xenos.png") 
message = ""
#DrawFunction
def draw():
    screen.fill("lightgreen")
    Alienthatisgoingtobeshot.draw()
    screen.draw.text("SHOOT HIM",(80,10),fontsize = 100,color = "RED")
    screen.draw.text(message,(80,70),fontsize = 50,color = "RED")

    

#FunctionForRandomMovement
def move():
    Alienthatisgoingtobeshot.x = random.randint(15,485)
    Alienthatisgoingtobeshot.y = random.randint(15,585)
#MouseEvent
def on_mouse_down(pos):
    global message
    if Alienthatisgoingtobeshot.collidepoint(pos):
        message = "YOU KILLED HIM"

        move()
    else:
        message = "HOW DID YOU MISS"
move()

pgzrun.go()
