import pgzrun, random
game_over = False
game_win = False
lives = 3
score = 0
WIDTH = 900
HEIGHT = 700
player = Actor("survivor.png")
zambie = Actor("zombie.png")
player.pos = (500,600)
zambie.x = random.randint(50,850)



bullets = []
def on_key_down(key):
    if key == keys.SPACE:
        bullets.append(Actor("pew pew.png"))
        bullets[-1].x = player.x
        bullets[-1].y = player.y - 100

def draw():
    screen.fill("black")
    zambie.draw()
    player.draw()
    for i in bullets:
        i.draw()
    screen.draw.text(str(score),(0,0),fontsize = 70)
    screen.draw.text(str(lives),(850,650),fontsize = 70)
    if game_over:
        screen.fill("RED")
        screen.draw.text("You are dead",(250,300),fontsize = 100)
    if game_win:
        screen.fill("green")
        screen.draw.text("You have triumphed",(150,300),fontsize = 100)
        

def update():
    pass
    global score
    global game_win
    global lives
    global game_over
    zambie.y+=2
    if zambie.y == 700:
        lives -=1
        if lives == 0:
            game_over = True
        zambie.y = 0
        zambie.x = random.randint(50,850)
    if keyboard.a:
        player.x-=5
    if keyboard.d:
        player.x+=5
    for i in bullets:
        i.y-=5
        if i.colliderect(zambie):
            zambie.y = 0
            zambie.x = random.randint(50,850)
            bullets.remove(i)
            score+=1
    if score == 30:
        game_win = True
   







pgzrun.go()

