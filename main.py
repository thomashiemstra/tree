import pygame
from random import choice, randrange

pygame.init()

WIDTH, HEIGHT = 1920, 1080
RES = (WIDTH, HEIGHT)

FONT_SIZE = 30
alpha_value = randrange(30, 40, 5)

chars = ['ｦ', 'ｱ', 'ｳ', 'ｴ', 'ｵ', 'ｶ', 'ｷ', 'ｹ', 'ｺ', 'ｻ', 'ｼ', 'ｽ', 'ｾ', 'ｿ', 'ﾀ', 'ﾂ', 'ﾃ', 'ﾅ', 'ﾆ', 'ﾇ', 'ﾈ',
         'ﾊ', 'ﾋ', 'ﾎ', 'ﾏ', 'ﾐ', 'ﾑ', 'ﾒ', 'ﾓ', 'ﾔ', 'ﾕ', 'ﾗ', 'ﾘ', 'ﾜ', '9', '8', '7', '5', '2', '1', ':', '.',
         '"', '=', '*', '+', '-', '¦', '|', '_', '╌', '日']

font = pygame.font.Font('font/ms mincho.ttf', FONT_SIZE)
font_2 = pygame.font.Font('font/ms mincho.ttf', FONT_SIZE - FONT_SIZE // 6)
font_3 = pygame.font.Font('font/ms mincho.ttf', FONT_SIZE - FONT_SIZE // 3)
font_4 = pygame.font.Font('font/ms mincho.ttf', FONT_SIZE - FONT_SIZE // 4)

green_chars = [font.render(char, True, (0, 255, 0)) for char in chars]
green_chars_2 = [font_2.render(char, True, (0, 255, 0)) for char in chars]
green_chars_3 = [font_3.render(char, True, (0, 255, 0)) for char in chars]
green_chars_4 = [font_4.render(char, True, (0, 255, 0)) for char in chars]

screen = pygame.display.set_mode(RES)
background = pygame.Surface(RES)
display_surface = pygame.Surface(RES)
display_surface.set_alpha(20)
# pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

clock = pygame.time.Clock()


class Symbol:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 30
        self.value = choice(green_chars)

    def draw(self):
        val = choice(green_chars)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        if HEIGHT > self.y > 0 and background.get_at((self.x, self.y)) != (255, 255, 255, 255):
            screen.blit(val, (self.x, self.y))

    def draw_2(self):
        val = choice(green_chars_2)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        if HEIGHT > self.y > 0 and background.get_at((self.x, self.y)) != (255, 255, 255, 255):
            screen.blit(val, (self.x, self.y))

    def draw_3(self):
        val = choice(green_chars_3)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        if HEIGHT > self.y > 0 and background.get_at((self.x, self.y)) != (255, 255, 255, 255):
            screen.blit(val, (self.x, self.y))

    def draw_4(self):
        val = choice(green_chars_4)
        self.y = self.y + self.speed if self.y < HEIGHT else -FONT_SIZE * randrange(1, 10)
        if HEIGHT > self.y > 0 and background.get_at((self.x, self.y)) != (255, 255, 255, 255):
            screen.blit(val, (self.x, self.y))


symbols = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE * 4)]
symbols_2 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE, WIDTH, FONT_SIZE * 4)]
symbols_3 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE * 2, WIDTH, FONT_SIZE * 4)]
symbols_4 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE * 3, WIDTH, FONT_SIZE * 4)]

run = True

bg = pygame.image.load("tree.png")
bg = pygame.transform.scale(bg, (WIDTH, HEIGHT))
rect = bg.get_rect()
x_c, y_c = rect.center
background.blit(bg, (WIDTH/2 - x_c, HEIGHT/2 - y_c))

while run:

    screen.blit(display_surface, (0, 0))
    display_surface.fill(pygame.Color('black'))

    [symbol.draw() for symbol in symbols]
    [symbol_2.draw_2() for symbol_2 in symbols_2]
    [symbol_3.draw_3() for symbol_3 in symbols_3]
    [symbol_4.draw_3() for symbol_4 in symbols_4]

    pygame.time.delay(100)

    pygame.display.update()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False