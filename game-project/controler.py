import pygame, sys
from bullet import Bullet
from ino import Ino
import time

def events(screen, ship, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #Right key
            if event.key == pygame.K_RIGHT:
                ship.mright = True
            elif event.key == pygame.K_LEFT:
                ship.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, ship)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            # Right key
            if event.key == pygame.K_RIGHT:
                ship.mright = False
            elif event.key == pygame.K_LEFT:
                    ship.mleft = False

def update(bg_color, screen, ship, inos, bullets):
    """Обновление экрана"""
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(ino, bullets):
    """Обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, ino, True, True)

def ship_kill(stats, screen, ship, ino, bullets):
    stats.ships_left -=1
    ino.empty()
    bullets.empty()
    create_army(screen, ino)
    ship.create_ship()
    time.sleep(1)

def update_ino(stats, screen, ship, ino, bullets):
    ino.update()
    if pygame.sprite.spritecollideany(ship, ino):
        ship_kill(stats, screen, ship, ino, bullets)
    ino_check(stats, screen, ship, ino, bullets)

def ino_check(stats, screen, ship, ino, bullets):
    screen_rect = screen.get_rect()
    for ino in ino.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            ship_kill(stats, screen, ship, ino, bullets)
            break

def create_army(screen, inos):
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 300 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 1):
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + ino_width * ino_number
            ino.y = ino_height + ino_height * row_number
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)
