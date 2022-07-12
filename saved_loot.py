from model import Loot


class SavedLoot:
    loot: Loot
    tick: int
    is_alive: bool

    def __init__(self, loot: Loot, current_tick: int):
        self.loot = loot
        self.tick = current_tick
        self.is_alive = True
