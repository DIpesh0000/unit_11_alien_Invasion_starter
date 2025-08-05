from pathlib import Path

class settings:

    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'summer5.png'
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'newship_2_nobg.png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 6
        self.starting_ship_count = 3

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'beam.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        self.bullet_speed = 7 
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 10

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'new enemy.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 3
        self.fleet_direction = 1
        self.fleet_drop_speed = 40

        self.alien_formation = 'triangle'
        