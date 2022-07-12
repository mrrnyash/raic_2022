from math import sqrt, dist, cos, sin, radians
from config import *
from model import Unit
from model.vec2 import Vec2
from functions import define_projectile_properties


# Функция вычисления длины вектора
def vec2_magnitude(vec2: Vec2) -> float:
    return sqrt(pow(vec2.x, 2) + pow(vec2.y, 2))

# Функция вычисления нормы вектора
def vec2_norm(vec2: Vec2) -> Vec2:
    if vec2.x == 0.0 and vec2.y == 0.0:
        return vec2
    else:
        norm = vec2 / vec2_magnitude(vec2)
    return norm


# Функция вычисления вектора движения юнита к точке
def velocity_to_point(controlled_unit: Unit, point: Vec2) -> Vec2:
    return vec2_norm(point - controlled_unit.position) * 100000


# Функция вычисления move_point, aim_point для атаки
def calculate_attack_directions(controlled_unit: Unit, enemy_unit: Unit) -> tuple[Vec2, Vec2]:
    # Aim point
    distance = dist([enemy_unit.position.x, enemy_unit.position.y],
                    [controlled_unit.position.x, controlled_unit.position.y])
    t = (distance - 2 * CONSTANTS.unit_radius) / define_projectile_properties(controlled_unit)[1]
    aim_point = enemy_unit.position + vec2_norm(enemy_unit.velocity) * vec2_magnitude(enemy_unit.velocity) * t
    # Move point
    _range = define_projectile_properties(controlled_unit)[0] * define_projectile_properties(controlled_unit)[1]
    move_point = aim_point + vec2_magnitude(controlled_unit.position - aim_point) * _range

    return velocity_to_point(controlled_unit, move_point), velocity_to_point(controlled_unit, aim_point)


def distance(a: Vec2, b: Vec2) -> float:
    return sqrt(pow(b.x - a.x, 2) + pow(b.y - a.y, 2))


# Поворот точки на угол
def rotate(a: Vec2, alpha) -> Vec2:
    point = Vec2(0.0, 0.0)
    point.x = a.x * cos(radians(alpha)) - a.y * sin(radians(alpha))
    point.y = a.x * sin(radians(alpha)) + a.y * cos(radians(alpha))
    return point

# Видит ли юнит предмет
def unit_can_see_point(unit, loot):
    pass