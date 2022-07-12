from model import Unit, Projectile
from config import *
from geometry import *


def define_projectile_properties(controlled_unit: Unit):
    current_weapon_index = controlled_unit.weapon
    lifetime = CONSTANTS.weapons[current_weapon_index].projectile_life_time
    speed = CONSTANTS.weapons[current_weapon_index].projectile_speed
    return lifetime, speed


def is_dangerous(unit: Unit, projectile: Projectile) -> bool:
    pass


def get_most_dangerous_projectile(unit: Unit, projectiles: list[Projectile]) -> Projectile:
    pass




