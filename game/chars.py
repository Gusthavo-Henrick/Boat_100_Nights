class Player:
    def __init__(self, name: str):
        self.name = name
        self.hp = 100 # Percentage XD 0% = dead and 100% = max
        self.speed = 2 # px per FPS
        self.x = 0
        self.y = 0

    def move(self, x: int = 0, y: int = 0):
        x_is_zero = x == 0
        y_is_zero = y == 0

        if not x_is_zero:
            factor_x = -1 if x < 0 else 1
            self.x += self.speed * factor_x
        if not y_is_zero:
            factor_y = -1 if y < 0 else 1
            self.y += self.speed * factor_y

    def __repr__(self):
        return f'Player(name={self.name}, _hp={self.hp}, _speed={self.speed})'

    def __str__(self):
        return self.name

class Boat:
    def __init__(self):
        self.hp = 100
        self.speed = 5 # in water obvius
        self.level = 0

    def __repr__(self):
        return f'Boat(_hp={self.hp}, _speed={self.speed})'
