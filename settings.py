class Settings:
    """Класс для хранения всех настроек игры "Инопланетное вторжение"."""

    def __init__(self):
        """Инициализирует настройки игры"""
        # Параметры экрана.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)
        self.bullets_allowed = 5

        # Настрока корабля
        self.ship_limit = 3

        # Настройки снарядов
        self.bullet_width = 7
        self.bullet_height = 15
        self.bullet_color = (255, 140, 0)
        self.bullet_speed = 5.5

        # Настройка пришельцев
        self.fleet_drop_speed = 15

        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменившиеся в ходе игры"""
        self.ship_speed = 4.5
        self.bullet_speed = 7.0
        self.alien_speed = 1.2

        # fleet_direction = 1 - обозначает движение вправо; а -1 - влево
        self.fleet_direction = 1

        # Подсчет очков
        self.alien_points = 50
    
    def increase_speed(self):
        """Увеличивает настройки скорости и стоимость пришельцев."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)

    def set_difficulty(self, level):
        """Увеличивает сложность."""
        if level == "easy":
            self.alien_speed = 1.2
            self.speedup_scale = 1.0
        elif level == "medium":
            self.alien_speed = 2.0
            self.speedup_scale = 1.7
        elif level == "hard":
            self.alien_speed = 2.5
            self.speedup_scale = 2.2
