from pathlib import Path

class settings:

    def __init__(self):
        self.name: str = 'Alien Invasion'
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        self.bg_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images' / 'summer5.png'
        self.ship_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images' / 'newship_2_nobg.png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / 'unit_11_alien_Invasion_starter' / 'Assets' / 'images' / 'beam.png'
        self.laser_sound = Path.cwd() /  'unit_11_alien_Invasion_starter' / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7 
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5