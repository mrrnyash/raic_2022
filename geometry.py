from math import sqrt, dist
from model.vec2 import Vec2
from model.constants import Constants
from functions import define_projectile_properties


class Geometry:

    def __init__(self, constants: Constants):
        self.constants = constants

    def vector_magnitude(self, vector: list) -> float:
        return sqrt(pow(vector[0], 2) + pow(vector[1], 2))

    def vector_norm(self, vector: list) -> list:
        if vector[0] == 0.0 and vector[1] == 0.0:
            return vector
        else:
            vector[0] = vector[0] / self.vector_magnitude(vector)
            vector[1] = vector[1] / self.vector_magnitude(vector)
        return vector

    def subtract_vector(self, vector1: list, vector2: list) -> list:
        return [vector1[0] - vector2[0], vector1[1] - vector2[1]]

    def calculate_aim_point(self, controlled_unit, enemy_unit):
        move_point = Vec2(0, 0)
        aim_point = Vec2(0, 0)
        # Aim point
        distance = dist([enemy_unit.position.x, enemy_unit.position.y],
                        [controlled_unit.position.x, controlled_unit.position.y])
        t = (distance - 2 * self.constants.unit_radius) / \
            define_projectile_properties(controlled_unit, self.constants)[1]
        aim_point_x = enemy_unit.position.x + \
                      self.vector_magnitude([enemy_unit.velocity.x,
                                             enemy_unit.velocity.y]) \
                      * t * self.vector_norm([enemy_unit.velocity.x,
                                              enemy_unit.velocity.y])[0]
        aim_point_y = enemy_unit.position.y + \
                      self.vector_magnitude([enemy_unit.velocity.x,
                                             enemy_unit.velocity.y]) \
                      * t * self.vector_norm([enemy_unit.velocity.x,
                                              enemy_unit.velocity.y])[1]
        aim_point.x = aim_point_x
        aim_point.y = aim_point_y
        # Move point
        _range = define_projectile_properties(controlled_unit, self.constants)[0] * \
                 define_projectile_properties(controlled_unit, self.constants)[1]
        vector_difference = self.subtract_vector([controlled_unit.position.x, controlled_unit.position.y],
                                                 [aim_point.x, aim_point.y])
        move_point_x = aim_point.x + \
                       self.vector_magnitude(vector_difference) * _range
        move_point_y = aim_point.y + \
                       self.vector_magnitude(vector_difference) * _range
        move_point.x = move_point_x
        move_point.x = move_point_y
        return move_point, aim_point
