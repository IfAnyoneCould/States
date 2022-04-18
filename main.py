from States import *
from pygame import *
from time import sleep
init()
flags = DOUBLEBUF
win = display.set_mode((960,600),flags)
display.set_caption("States")
states = []
select = True
state = None
clock = time.Clock()
def GetTrans(sprite):
    new = sprite
    new.image.set_alpha(100)
    return new
def GetNorm(sprite):
    new = sprite
    new.image.set_alpha(255)
    return new
class Cursor(sprite.Sprite):
    def __init__(self,cursor):
        super().__init__()
        self.image = transform.scale(image.load("Sprites/"+cursor+".png"),(2,2)).convert_alpha()
        self.image.set_alpha(0)
        self.rect = self.image.get_rect(center=mouse.get_pos())
        self.mask = mask.from_surface(self.image)
    def Render(self):
        self.rect = self.image.get_rect(center=mouse.get_pos())
        win.blit(self.image,self.rect)
    def Collide(self):
        global allSprites
        for i in allSprites:
            if sprite.collide_mask(self,i) != None:
                allSprites.remove(i)
                i = GetTrans(i)
                allSprites.add(i)
                if mouse.get_pressed()[0] == True:
                    global select, state
                    state = i.state
                    state.Load()
                    select = False
            else:
                allSprites.remove(i)
                i = GetNorm(i)
                allSprites.add(i)
running = True
cursor = Cursor("cursor")
offset = 0
for i in allSprites:
    i.image = i.image.convert_alpha()
while running:
    win.fill((255,255,255))
    for i in event.get():
        if i.type == QUIT:
            running = False
    if key.get_pressed()[K_q]:
        running = False
    if select == True:
        allSprites.draw(win)
        cursor.Collide()
    else:
        state.Render(win)
        if key.get_pressed()[K_b]:
            select = True
            state.birdSong.stop()
            state = None
        if key.get_pressed()[K_p]:
            state.birdSong.play()
        if key.get_pressed()[K_s]:
            state.birdSong.stop()
    cursor.Render()
    clock.tick()
    display.flip()