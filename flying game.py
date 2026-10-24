import pgzrun
import random
WIDTH=400
HEIGHT=400
s=0
game_over=False
b=Actor("bee")
b.x=200
b.y=200
f=Actor("flower")
f.x=random.randint(0,400)
f.y=random.randint(0,400)
def draw():
    screen.blit("background",(0,0))
    b.draw()
    f.draw()
    screen.draw.text("score"+ str(s),(0,0),color="black")
    if game_over==True:
        screen.fill("black")
        screen.draw.text("score"+ str(s),(0,0),color="white")
def update():
    global s
    if b.colliderect(f):
        s=s+10
        f.x=random.randint(0,400)
        f.y=random.randint(0,400)
    if keyboard.left:
        b.x=b.x-2
    if keyboard.right:
        b.x=b.x+2
    if keyboard.up:
        b.y=b.y-2
    if keyboard.down:
        b.y=b.y+2
def time_up():
    global game_over
    game_over=True
clock.schedule(time_up,10.0)
pgzrun.go()