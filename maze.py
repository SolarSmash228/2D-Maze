from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self,player_speed, player_x, player_y, player_image, x, y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (x,y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
    
class Player(GameSprite):
    def move(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5 or key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.y < 700 or key_pressed[K_s] and self.rect.y < 700:
            self.rect.y += self.speed
        if key_pressed[K_RIGHT] and self.rect.x < 1100 or key_pressed[K_d] and self.rect.x < 1100:
            self.rect.x += self.speed
        if key_pressed[K_LEFT] and self.rect.x > 5 or key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        
class Enemy(GameSprite):
    direction = 'left'
    direction1 = 'down'    
    
    def move(self, x1, x2):
        if self.rect.x <= x1:
            self.direction = 'right' 
        if self.rect.x > x2:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed
    
    def move_up_down(self,x1,x2):
        if self.rect.y <= x1:
            self.direction1 = 'up'
        if self.rect.y > x2:
            self.direction1 = 'down'
        if self.direction1 == 'down':
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        
class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, width, height, x, y):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.width = width
        self.height = height
        self.image = Surface((self.width, self.height))
        self.image.fill((color1,color2,color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def wall_show(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

w = 1200
h = 800
finish = False
window = display.set_mode((w,h))
font.init()
font = font.Font(None,70)
win = font.render('YOU WIN!', True, (255,215,0))
lose = font.render('YOU LOSE!', True, (255, 0, 47))
display.set_caption('Лабиринт')
clock = time.Clock()
background = transform.scale(image.load('background.jpg'), (w,h))
mixer.init()
mixer.music.load('7b809fb1bc83164.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')
game = True
player = Player(5, 50, 380, 'hero.png', 100,100)
cyborg = Enemy(7, 1000, 400, 'cyborg.png', 100,100)
enemy = Enemy(20, 500, 100, 'cyborg.png', 110,110)
wall1 = Wall(98, 0, 255, 10, 650, 470, 0)
wall2 = Wall(98, 0, 255, 10, 650, 620, 0)
wall3 = Wall(98, 0, 255, 480, 10, 0, 350)
wall4 = Wall(98, 0, 255, 330, 10, 0, 500)
wall5 = Wall(98, 0, 255, 10, 700, 330, 500)
wall6 = Wall(98, 0, 255, 10, 680, 760, 130)
wall7 = Wall(98, 0, 255, 325, 10, 760, 130)
finish1 = GameSprite(0, 900, 600, 'treasure.png', 200,200) 
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player.reset()
        cyborg.reset()
        enemy.reset()
        player.move()
        wall1.wall_show()
        wall2.wall_show()
        wall3.wall_show()
        wall4.wall_show()
        wall5.wall_show()
        wall6.wall_show()
        wall7.wall_show()
        finish1.reset()
        enemy.move_up_down(30,700)
        cyborg.move(800,1100)
        clock.tick(60)
        if sprite.collide_rect(player, cyborg) or sprite.collide_rect(player, enemy) or sprite.collide_rect(player, wall1) or sprite.collide_rect(player, wall2) or sprite.collide_rect(player, wall3) or sprite.collide_rect(player, wall4) or sprite.collide_rect(player, wall5) or sprite.collide_rect(player, wall6) or sprite.collide_rect(player, wall7):
            window.blit(lose, (460,350))
            finish = True
            kick.play()
        if sprite.collide_rect(player, finish1):
            window.blit(win,(453,350))
            finish = True
            money.play()
        display.update()
