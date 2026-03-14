from random import randint
import pygame


class Sprite:
    def __init__(self, center, image):
        self.image = image
        self.rect = self.image.get_frect()
        self.rect.center = center

    def render(self, surface):
        surface.blit(self.image, self.rect)


class MoveSprite(Sprite):
    def __init__(self, center, image, speed, direction):
        super().__init__(center, image)

        self.speed = speed
        self.direction = direction.normalize()

    def update(self):
        vector = self.direction * self.speed
        self.rect.move_ip(vector)


WINDOW_SIZE = (800, 600)
MAX_FPS = 60

window = pygame.Window("Tower Defense", WINDOW_SIZE)
surface = window.get_surface()

clock = pygame.Clock()

center = WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2
image = pygame.Surface((50, 50))
image.fill("blue")
player = Sprite(center, image)
bullets = []
enemies = []
score = 0

running = True

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.WINDOWCLOSE:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            image = pygame.Surface((6, 6))
            image.fill("green")
            center = pygame.Vector2(player.rect.center)
            pos = pygame.Vector2(pygame.mouse.get_pos())
            direction = pos - center

            bullet = MoveSprite(center, image, 7, direction)
            bullets.append(bullet)

    # Обновление объектов
    if randint(0, 100) <= 5:
        image = pygame.Surgace((50, 50))
        image.fill("red")
        center = pygame.Vector2(player.rect.center)\
        
        r = randint(1,4)
        if r == 1:
            pos = pygame.Vector2(randint(0, WINDOW_SIZE[0]), -100)
        elif r == 2:
            pos = pygame.Vector2(WINDOW_SIZE[0] + 100, randint(0,WINDOW_SIZE[1]))
        elif r == 3:
            pos = pygame.Vector2(randint(0,WINDOW_SIZE[0]), WINDOW_SIZE[1] + 100)
        else:       
            pos = pygame.Vector2(-100, randint(0,WINDOW_SIZE[1]))

        direction = center - pos 
        enemy - MoveSprite(pos, image,randint(100,400) / 100,direction)
        enemies.append(enemy)

    for bullet in bullets:
        bullet.update()
    for enemy in enemies:
        enemy.update()

        for bullets  in bullets:
            for enemy in enemies:
                if bullet.rect.colliderect(enemy.rect):
                    score += 1
                    bullets.remore(bullet)
                    enemies.remove(enemy)
                    break
    for enemy in enemies:
        if player.rect.colliderect(enemy.rect):
            score = 0
            enemies.clear()
            bullets.clear()
            break

    # Отрисовка
    surface.fill("white")
    player.render(surface)
    for bullet in bullets:
        bullet.render(surface)
    for enemy in enemies:
        enemy.render(surface)
    window.flip()

    clock.tick(MAX_FPS)