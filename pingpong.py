from pygame import *

class GameSprite(sprite.Sprite):
   #конструктор класса
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self): #перемещение для левой ракетки
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 200:
            self.rect.y += self.speed
    def update_r(self): #перемещение для правой
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 200:
            self.rect.y += self.speed
            
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

# картинка, координата х, координата y, скорость, размер по х, размер по y
player_r = Player("racket.png", 620, 200, 5, 50, 200)
player_l = Player("racket.png",30, 200 , 5, 50, 200)
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        # window.blit(background,(0, 0))
        window.fill(BACK)
        player_l.reset()
        player_r.reset()

        player_r.update_r()
        player_l.update_l()

    display.update()
    clock.tick(FPS)
