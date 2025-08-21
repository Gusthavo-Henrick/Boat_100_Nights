class Player:
    def __init__(self, name: str):
        self.name = name
        self.hp = 100 # Percentage XD 0% = dead and 100% = max
        self.speed = 2 # px per FPS

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