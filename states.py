from abc import ABC
from config import *
from geometry import calculate_attack_directions
from model import UnitOrder, Unit


class State(ABC):

    @property
    def state_value(self):
        raise NotImplementedError

    def __lt__(self, other):
        if self.state_value < other.state_value:
            return True
        else:
            return False

    '''Less'''

    def __gt__(self, other):
        if self.state_value > other.state_value:
            return True
        else:
            return False

    '''Greater'''

    def __eq__(self, other):
        if self.state_value == other.state_value:
            return True
        else:
            return False

    '''Equal'''

    def __le__(self, other):
        if self.state_value <= other.state_value:
            return True
        else:
            return False

    '''Less or equal'''

    def __ge__(self, other):
        if self.state_value >= other.state_value:
            return True
        else:
            return False

    '''Greater or equal'''


class Evade(State):
    state_value = 1

    def run(self, unit) -> UnitOrder:
        pass

    def unit_can_do(self, unit) -> bool:
        pass


class RunFromEdge(State):
    state_value = 2

    def run(self, unit) -> UnitOrder:
        pass

    def unit_can_do(self, unit: Unit) -> bool:
        pass


class RunAway(State):
    state_value = 3

    def run(self, unit: Unit) -> UnitOrder:
        pass

    def unit_can_do(self, unit) -> bool:
        pass


class UseShieldPotion(State):
    state_value = 4

    def run(self, unit: Unit) -> UnitOrder:
        pass

    def unit_can_do(self, unit: Unit) -> bool:
        pass


class TakeLoot(State):
    state_value = 5

    def run(self, unit: Unit) -> UnitOrder:
        pass

    def unit_can_do(self, unit: Unit) -> bool:
        pass


class Attack(State):
    state_value = 6

    def run(self, unit: Unit, enemy_unit: Unit) -> UnitOrder:
        move_point, aim_point = calculate_attack_directions(unit, enemy_unit)
        return UnitOrder(
            move_point,
            aim_point,
            ActionOrder.Aim(True))

    def unit_can_do(self, unit: Unit) -> bool:
        pass


class Wander(State):
    state_value = 7

    def run(self, unit: Unit) -> UnitOrder:
        pass

    def unit_can_do(self, unit: Unit) -> bool:
        pass


class Idle(State):
    state_value = 8

    def run(self, unit: Unit) -> UnitOrder:
        pass

    def unit_can_do(self, unit: Unit) -> bool:
        pass
