import sys


import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(ai_settings)
    play_button = Button(ai_settings, screen, 'Play')
    sb = Scoreboard(ai_settings, screen, stats)

    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets) 
        gf.update_screen(ai_settings, screen, stats, sb, ship, bullets, aliens, play_button)
        if stats.game_active:
            ship.update()
            # print(len(bullets))
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)
run_game()

        