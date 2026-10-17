import pgzrun
import random
WIDTH=400
HEIGHT=400
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
def update():
    if keyboard.left:
        b.x=b.x-2
    if keyboard.right:
        b.x=b.x-2
    if keyboard.up:
        b.x=b.x-2
    if keyboard.down:
        b.x=b.x-2
pgzrun.go()