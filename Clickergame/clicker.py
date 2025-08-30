import pgzrun
import random
TITLE = "Shoot the alien"
#ScreenSize
WIDTH = 500
HEIGHT = 600
#Creating Actors
Alienthatisgoingtobeshot=Actor("xenos.png") 
#DrawFunction
def draw():
    screen.fill("lightgreen")
    Alienthatisgoingtobeshot.draw()
    screen.draw.text("SHOOT HIM",(80,10),fontsize = 100,color = "RED")
#FunctionForRandomMovement
def move():
    Alienthatisgoingtobeshot.x = random.randint(15,485)
    Alienthatisgoingtobeshot.y = random.randint(15,585)
move()

pgzrun.go()