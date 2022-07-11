from model import Unit, Constants


def define_projectile_properties(controlled_unit: Unit, constants: Constants):
    current_weapon_index = controlled_unit.weapon
    lifetime = constants.weapons[current_weapon_index].projectile_life_time
    speed = constants.weapons[current_weapon_index].projectile_speed
    return lifetime, speed
