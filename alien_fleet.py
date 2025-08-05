import pygame
from alien import Alien
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        self.formation = self.settings.alien_formation

        self.create_fleet()

    def create_fleet(self):
        form = self.formation.lower()
        if form == 'diamond':
            self._create_diamond_fleet()
        elif form == 'hourglass':
            self._create_hourglass_fleet()
        elif form == 'zigzag':
            self._create_zigzag_fleet()
        elif form == 'square':
            self._create_square_fleet()
        elif form == 'triangle':
            self._create_triangle_fleet()
        else:
            self._create_default_grid()

    def _create_default_grid(self):
        alien_w = self.settings.alien_w
        alien_h = self.settings.alien_h
        sw = self.settings.screen_w
        sh = self.settings.screen_h
        fleet_w, fleet_h = self.calculate_fleet_size(alien_w, sw, alien_h, sh)
        x_offset, y_offset = self.calculate_offsets(alien_w, alien_h, sw, fleet_w, fleet_h)
        self._create_rectangle_fleet(alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_w, alien_h, fleet_w, fleet_h, x_offset, y_offset):
        for row in range(fleet_h):
            for col in range(fleet_w):
                if col % 2 == 0 or row % 2 == 0:
                    continue
                x = alien_w * col + x_offset
                y = alien_h * row + y_offset
                self._create_alien(x, y)

    def _create_square_fleet(self):
        aw, ah = self.settings.alien_w, self.settings.alien_h
        sw = self.settings.screen_w
        N = 6
        x_off = (sw - N * aw) // 2
        y_off = 60
        for row in range(N):
            for col in range(N):
                x = x_off + col * aw
                y = y_off + row * ah
                self._create_alien(x, y)

    def _create_triangle_fleet(self):
        aw, ah = self.settings.alien_w, self.settings.alien_h
        sw = self.settings.screen_w
        rows = 7
        base_width = rows * aw
        x_off = (sw - base_width) // 2
        y_off = 60
        for r in range(rows):
            row_width = (r + 1) * aw
            row_x_off = x_off + (base_width - row_width) // 2
            y = y_off + r * ah
            for c in range(r + 1):
                x = row_x_off + c * aw
                self._create_alien(x, y)


    def calculate_offsets(self, alien_w, alien_h, screen_w, fleet_w, fleet_h):
        half_screen = self.settings.screen_h // 2
        fleet_horizontal_space = fleet_w * alien_w
        fleet_vertical_space = fleet_h * alien_h
        x_offset = (screen_w - fleet_horizontal_space) // 2
        y_offset = (half_screen - fleet_vertical_space) // 2
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_w, screen_w, alien_h, screen_h):
        fleet_w = screen_w // alien_w
        fleet_h = (screen_h / 2) // alien_h
        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2
        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2
        return int(fleet_w), int(fleet_h)

    def _create_alien(self, x: int, y: int):
        new_alien = Alien(self, x, y)
        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        for alien in self.fleet:
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break

    def _drop_alien_fleet(self):
        for alien in self.fleet:
            alien.y += self.fleet_drop_speed

    def update_fleet(self):
        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        for alien in self.fleet:
            alien.draw_alien()

    def check_collisions(self, other_group):
        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)

    def check_fleet_bottom(self):
        for alien in self.fleet:
            if alien.rect.bottom >= self.settings.screen_h:
                return True
        return False

    def check_destroyed_status(self):
        return not self.fleet
