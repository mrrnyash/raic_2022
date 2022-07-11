from geometry import Geometry
from model import Vec2, UnitOrder, ActionOrder, Constants


class UnitBehavior:
    # TODO: Настроить приоритет выполнения поведений
    _BEHAVIOR_PRIORITY = {
        'EVADE',
        'RUN_FROM_EDGE',
        'ATTACK',
        'RUN_AWAY',
        'USE_SHIELD_POTION',
        'TAKE_SHIELD_POTION',
        'TAKE_AMMO',
        'TAKE_BOW',
        'WANDER',
        'IDLE'
    }

    def __init__(self, constants: Constants, controlled_unit):
        self.controlled_unit = controlled_unit
        self.geometry = Geometry(constants)

    # TODO: Бродить вдоль края зоны вращаясь постепенно сдвигаясь к центру зоны
    def wander(self, controlled_unit):
        return UnitOrder(
            Vec2(-controlled_unit.position.x,
                 -controlled_unit.position.y),
            Vec2(-controlled_unit.direction.y,
                 controlled_unit.direction.x),
            None)

    def attack(self, controlled_unit, enemy_unit):
        move_point, aim_point = self.geometry.calculate_aim_point(controlled_unit, enemy_unit)
        return UnitOrder(
            move_point,
            aim_point,
            ActionOrder.Aim(True))

    def evade(self, controlled_unit):
        return UnitOrder(
            Vec2(-controlled_unit.position.x,
                 -controlled_unit.position.y),
            Vec2(0,
                 0),
            None)
