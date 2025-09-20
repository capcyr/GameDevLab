import pgzrun
import random
import time

WIDTH = 800
HEIGHT = 500
#Gaming Variables
satellites = []
connections = []
timing = 0 
totaltimer = 0
satcount = 0
totalsatcount = 8
def teleport():
    global timing
    for i in range(totalsatcount):
        satellite = Actor("satellite.png")
        satellite.x = random.randint(80,720)
        satellite.y = random.randint(60,440)
        satellites.append(satellite)
    timing = time.time()

teleport()

def on_mouse_down(pos):
    


def draw():
    global totaltimer
    screen.blit("space.jpg",(0,0))
    count = 1
    for i in satellites:
        i.draw()
        screen.draw.text(str(count),(i.pos[0],i.pos[1]-40))
        count+=1 
    if satcount < totalsatcount:
        totaltimer = time.time() - timing
        totaltimer = round(totaltimer,1)
        screen.draw.text(str(totaltimer),(50,75))
def update():
    pass

pgzrun.go()