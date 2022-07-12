from model import Unit


class SavedEnemies:
    unit: Unit
    tick: int
    is_alive: bool

    def __init__(self, unit: Unit, current_tick: int):
        self.unit = unit
        self.tick = current_tick
