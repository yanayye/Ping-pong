from pygame import *

win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("PING PONG")
BACK = (200,255,255) # фон с цветом 
window.fill(BACK)

game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        # window.blit(background,(0, 0))
        window.fill(BACK)

    display.update()
    clock.tick(FPS)
