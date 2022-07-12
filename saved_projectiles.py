from model import Projectile
from config import CONSTANTS

class SavedProjectiles:
    projectile: Projectile
    tick: int
    is_alive: bool

    def __init__(self, projectile: Projectile, current_tick: int):
        self.projectile = projectile
        self.tick = current_tick

    def update(self, current_tick):
        pass