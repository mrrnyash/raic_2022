from debug_interface import DebugInterface
from model.game import Game
from model.order import Order
from model.unit_order import UnitOrder
from model.constants import Constants
from model.vec2 import Vec2
from model.action_order import ActionOrder
from typing import Optional
from behavior import Behavior
from config import GAME, MY_MEMORY, CONSTANTS


class MyStrategy:

    def __init__(self, constants: Constants):
        CONSTANTS = constants

    def get_order(self, game: Game, debug_interface: Optional[DebugInterface]) -> Order:
        GAME = game
        MY_MEMORY.update(GAME.current_tick)

        controlled_unit = None
        enemy_unit = None
        for unit in game.units:
            if unit.player_id == game.my_id:
                controlled_unit = unit
                break

        behavior = Behavior(controlled_unit)

        # Attack

        # Evade

        return Order(behavior.run())

    def debug_update(self, displayed_tick: int, debug_interface: DebugInterface):
        pass

    def finish(self):
        pass
