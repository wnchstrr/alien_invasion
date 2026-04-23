from storage import JsonStorage


class GameStats:
    """Отслеживает статистику для игры "Инопланетное вторжение"."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        # Рекорд не должен сбрасываться.
        self.high_score = 0

        # Сохранение рекорда в json.
        self.storage = JsonStorage("high_score.json")
        self.high_score = self.storage.load()

    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit  
        self.score = 0
        self.level = 1
