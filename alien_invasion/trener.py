
from settings import Settings
from ship import Ship
import sys
import pygame

class AlienInvasion():
    """класс для управлением ресурсамии поведением игры"""
    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (
            self.settings.screen_width,
            self.settings.screen_height
            )
        )
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        """запуск основного цикла игры."""
        while True:
            self._check_events()
            self._update_screen()
            #отслеживание клавиатуры и мыши
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        """обновляет изображение на экране и отображает новый экран"""
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

if __name__ == '__main__':
    #создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()