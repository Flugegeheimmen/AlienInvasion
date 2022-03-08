class GameStats():
    """ОТслеживание статистики для игры"""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Инициализирует статистику"""
        self.ships_left = self.settings.ship_limit