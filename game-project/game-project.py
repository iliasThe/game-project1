import pygame, controler
from ship import Ship
from pygame.sprite import Group
from stats import Stats


def run():
      pygame.init()
      screen = pygame.display.set_mode((600, 600))
      pygame.display.set_caption("Star wars(infinity)")
      bg_color = (0, 0, 0)
      ship = Ship(screen)
      bullets = Group()
      ino = Group()
      controler.create_army(screen, ino)
      stats = Stats()

      while True:
          controler.events(screen, ship, bullets)
          ship.update_ship()
          controler.update(bg_color, screen, ship, ino, bullets)
          controler.update_bullets(ino, bullets)
          controler.update_ino(stats, screen, ship, ino, bullets)



run()