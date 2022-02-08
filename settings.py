class Settings():
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (205, 205, 205)
        self.bullet_allowed = 3

        #Ship Settings
        self.ship_speed = 1.5

        #Параметры Снаряда
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)