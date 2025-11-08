import pgzrun
import random
import itertools


WIDTH = 840   
HEIGHT = 825

block = Actor("block.png")
rocket = Actor("tinyrocket.webp")

block.pos = (130,130)
rocket.pos = (350,350)
blockposition = [(750,130),(750,750),(130,750),(130,130)]
repetition = itertools.cycle(blockposition)



def draw():
    screen.clear()
    block.draw()
    rocket.draw()
def animateblock():
    animate(block,"bounce_end",duration=1,pos = next(repetition))
animateblock()
clock.schedule_interval(animateblock,2) 
#Rocket Ship animation
def animaterocket():
    xpos = random.randint(150,640)
    ypos= random.randint(150,625)
    rocket.target = xpos,ypos
    target_angle = rocket.angle_to(rocket.target)
    target_angle+= 360*((rocket.angle-target_angle+180)//360)
    animate(rocket,angle = target_angle,duration =0.1,on_finished = rocketanimation,)
    
def rocketanimation():
    anim = animate(rocket,tween='accel_decel',pos=rocket.target,duration=rocket.distance_to(rocket.target)/800,on_finished=animaterocket,)
animaterocket()

pgzrun.go()
