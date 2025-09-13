import pgzrun
import random
WIDTH = 750
HEIGHT = 500
bee = Actor("bee.png")
flower = Actor("flower.png")
score_1 = 0
gameover = False
def GAMEOVER():
    global gameover
    gameover = True 
def teleport():
    flower.x = random.randint(80,700)
    flower.y = random.randint(80,420)



def draw():
    screen.blit("land.jpg",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text(str(score_1),(650,10),fontsize = 100,color = "RED")
    if gameover:
        screen.fill("red")
        screen.draw.text("GAME OVER",(170,220),fontsize = 100,color = "BLACK")
        screen.draw.text(("Your score was"+str(score_1)),(140,300),fontsize = 100,color = "BLACK")
def update():
    global score_1
    if keyboard.left:
        bee.x=bee.x - 5
    if keyboard.right:
        bee.x=bee.x + 5
    if keyboard.up:
        bee.y=bee.y-5
    if keyboard.down:
        bee.y=bee.y+5
    if bee.colliderect(flower):
        teleport()
        score_1+=1
    
clock.schedule(GAMEOVER,60)
teleport()
pgzrun.go()