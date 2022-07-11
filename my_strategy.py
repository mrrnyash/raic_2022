from geometry import Geometry
from debug_interface import DebugInterface
from model.game import Game
from model.order import Order
from model.unit_order import UnitOrder
from model.constants import Constants
from model.vec2 import Vec2
from model.action_order import ActionOrder
from typing import Optional
from unit_behavior import UnitBehavior
from conditions import Conditions

class MyStrategy:

    def __init__(self, constants: Constants):
        self._orders = {}
        self.geometry = Geometry(constants)
        self.constants = constants


    def get_order(self, game: Game, debug_interface: Optional[DebugInterface]) -> Order:
        controlled_unit = None
        enemy_unit = None
        for unit in game.units:
            if unit.player_id == game.my_id:
                controlled_unit = unit
                break
        behavior = UnitBehavior(self.constants, controlled_unit)
        if len(game.units) == 2:
            for unit in game.units:
                if unit.player_id != game.my_id:
                    enemy_unit = unit
                    break
            self._orders[controlled_unit.id] = behavior.attack(controlled_unit, enemy_unit)
        else:
            self._orders[controlled_unit.id] = behavior.wander(controlled_unit)
        return Order(self._orders)

    def debug_update(self, displayed_tick: int, debug_interface: DebugInterface):
        pass

    def finish(self):
        pass
