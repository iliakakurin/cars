from random import randint
import pygame as pg
import sys

pg.time.set_timer(pg.USEREVENT, 2000)

W = 800
H = 600
WHITE = (255, 255, 255)
CARS = ('car1.png', 'car2.png', 'car3.png')
# для хранения готовых машин-поверхностей
CARS_SURF = []
cars_passed = 0

# надо установить видео режим
# до вызова image.load()
sc = pg.display.set_mode((W, H))

for i in range(len(CARS)):
    CARS_SURF.append(
        pg.image.load(CARS[i]).convert_alpha())


class Car(pg.sprite.Sprite):
    def __init__(self, x, surf, group):
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(
            center=(x, 0))
        # добавляем в группу
        self.add(group)
        # у машин будет разная скорость
        self.speed = randint(1, 4)

    def update(self):
        global cars_passed
        if self.rect.y < H:
            self.rect.y += self.speed
        else:
            # теперь не перебрасываем вверх,
            # а удаляем из всех групп
            self.kill()
            cars_passed += 1


class Player(pg.sprite.Sprite):
    def __init__(self, surf):
        global W, H
        pg.sprite.Sprite.__init__(self)
        self.image = surf
        self.rect = self.image.get_rect(
            center=(W // 2, H - 50))
        # у машин будет разная скорость
        self.speed = 5

    def update(self):
        # проверить выезд влево и вправо
        if pg.sprite.spritecollideany(self, cars):
            # закончить игру
            print(111)
            pass

cars = pg.sprite.Group()

# добавляем первую машину,
# которая появляется сразу
Car(randint(1, W),
    CARS_SURF[randint(0, 2)], cars)
Car(randint(1, W),
    CARS_SURF[randint(0, 2)], cars)
pl = Player(CARS_SURF[randint(0, 2)])

while 1:
    for i in pg.event.get():
        print(i)
        if i.type == pg.QUIT:
            sys.exit()
        elif i.type == pg.USEREVENT:
            Car(randint(1, W),
                CARS_SURF[randint(0, 2)], cars)

    sc.fill(WHITE)

    cars.draw(sc)
    sc.blit(pl.image, pl.rect)
    pg.display.set_caption(f'Проехало машин: {cars_passed}')
    pg.display.update()
    pg.time.delay(20)
    pl.update()
    cars.update()

# 0) вычислить FPS для этой программы                           +
# 1) появление кадые 2 секунды                                  +
# 2) скорость была от 1 до 4 включительно                       +
# 3) экран 800 в ширину на 600 в высоту                         +
# 4) чтобы сразу создавалось 2 машины                           +
# 5) название окна установить со счетчиком проехавших машин     +
