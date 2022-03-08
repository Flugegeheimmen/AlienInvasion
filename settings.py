class Settings():
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (255, 255, 255)
        self.bullet_allowed = 3

        #Ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        #Параметры Снаряда
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

        #Настройки пришельцев
        self.alien_speed = 1.0
        self.fleet_drop_speed = 5
        #fleet)direction = 1 обозначает движение вправо а -1 влево
        self.fleet_direction = 1