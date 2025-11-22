import pgzrun
import random

WIDTH = 1000
HEIGHT = 700

#Variables
gameover = False
levels = 6
beginlevel = 1
currentlevel = []
speed = 5
gamecomplete = True
totalitems = ["labtop.png","mirror.png","plasticbag.png","pot.png"]
targetitem = None

def draw():
    screen.fill("white")
    if gameover:
        screen.fill("black")
        screen.draw.text("GAME OVER",center = (500,320), fontsize = 130 , color = "red") 
    elif gamecomplete:
        screen.fill("green")
        screen.draw.text("GAME WON",center = (500,320), fontsize = 130 , color = "Blue")


#function for falling items

def falling(extra):
    global targetitem
    global totalitems
    templist = []
    targetitem = random.choice(totalitems)
    wrongitem = random.choices([i for i  in totalitems if i != targetitem], k=extra)
    combinedlist = [targetitem]+wrongitem
    random.shuffle(combinedlist)
    #placement of items
    horizspacing = WIDTH/(len(combinedlist)+1)
    for u, img in enumerate(combinedlist):
       ACTING = Actor(img)
       ACTING.active = True 
       ACTING.x = (u+1)*horizspacing
       ACTING.y = random.randint(-100,0)
       templist.append(ACTING)
       animate(ACTING,duration = max(1,speed - beginlevel),on_finished = lambda a=ACTING: failure(a),y=HEIGHT)
    return templist
#When actor reaches the bottom
def failure(actor):
    global gameover
    if not actor.active:
        return 
    if actor.image == targetitem:
        gameover = True

def failureagain():
    global gameover
    gameover = True
     








def update():
    pass
    global currentlevel, beginlevel
    if gameover or gamecomplete:
        return
    if len(currentlevel) == 0:
        currentlevel = falling(beginlevel)









pgzrun.go()