import pgzrun, random


WIDTH = 900
HEIGHT = 700
player = Actor("survivor.png")
boolet = Actor("pew pew.png")
zambie = Actor("zombie.png")
player.pos = (500,600)
zambie.x = random.randint(50,850)




def draw():
    screen.fill("black")
    boolet.draw()
    zambie.draw()
    player.draw()
def update():
    pass
    zambie.y+=2
    if zambie.y == 700:
        zambie.y = 0
        zambie.x = random.randint(50,850)
    if keyboard.a:
        player.x-=5
    if keyboard.d:
        player.x+=5







pgzrun.go()