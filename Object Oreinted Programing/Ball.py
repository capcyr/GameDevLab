import pgzrun, random
TITLE = "Bouncing Ball Game"
WIDTH = 800
LENGTH = 750
red = random.randint(0,255)
blue = random.randint(0,255)
green = random.randint(0,255)

combined_rgb = red,green,blue

gravity = 2000.0
class ball:
    def __init__(self,initialx,initialy,radius):
        self.initialx = initialx
        self.initialy = initialy
        self.radius = radius

        self.vx = 200
        self.vy = 0
    def draw(self):
        red = random.randint(0,255)
        blue = random.randint(0,255)
        green = random.randint(0,255)

        color = red,blue,green 
        pos = (self.initialx,self.initialy)
        screen.draw.filled_circle(pos,self.radius,color)
#creating objects
baller = ball(100,100,60)
balls = [baller]
def draw():
    for i in balls:
        i.draw()
def update(t):
    global balls
    for i in balls:
        uy = i.vy
        i.vy += gravity*t 
        i.initialy += (uy+i.vy)*0.5*t
        if i.initialy>700 or i.initialy <0:
            i.initialy = 700
            i.vy = - i.vy*0.9
        i.initialx += i.vx*t
        if i.initialx>750 or i.initialx<50:
            i.vx = - i.vx

def on_key_down(key):
    if key == keys.SPACE:
        baller.vy = -350









pgzrun.go()    