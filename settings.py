class Settings():
    """Класс для хранения всех настроек игры"""
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (205, 205, 205)

        #Ship Settings
        self.ship_speed = 1.5