from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_p1(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_w] and self.rect.y < 495:
            self.rect.y -= self.speed

        if keys_pressed[K_s] and self.rect.y > 5:
            self.rect.y += self.speed
    def update_p2(self):
        keys_pressed = key.get_pressed()

        if keys_pressed[K_UP] and self.rect.y > 495:
            self.rect.y -= self.speed

        if keys_pressed[K_DOWN] and self.rect.y < 5:
            self.rect.y += self.speed

window = display.set_mode((700,500))
display.set_caption('Ping Pong')
back = (75,75,255)
window.fill(back)

game = True
clock = time.Clock()
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)