from geometry import Geometry
from model import Vec2, UnitOrder, ActionOrder, Constants, Game, Unit, Loot
from model.item import Weapon, Ammo

inf = 999999999.0

class Behavior:

    def __init__(self, constants: Constants, controlled_unit: Unit, game: Game):
        self.controlled_unit = controlled_unit
        self.geometry = Geometry(constants)
        self.game = game
        self.constants = Constants

    # TODO: Бродить вдоль края зоны вращаясь постепенно сдвигаясь к центру зоны
    def wander(self, controlled_unit: Unit) -> UnitOrder:
        return UnitOrder(
            Vec2(-controlled_unit.position.x, -controlled_unit.position.y),
            Vec2(-controlled_unit.direction.y, controlled_unit.direction.x),
            None)

    def attack(self, controlled_unit: Unit, enemy_unit) -> UnitOrder:
        move_point, aim_point = self.geometry.calculate_attack_directions(controlled_unit, enemy_unit)
        return UnitOrder(
            move_point,
            aim_point,
            ActionOrder.Aim(True))

    def evade(self, controlled_unit) -> UnitOrder:
        return UnitOrder(
            Vec2(-controlled_unit.position.x,
                 -controlled_unit.position.y),
            Vec2(0.0, 0.0),
            None)

    def take_loot(self, constants: Constants, controlled_unit: Unit, visible_loot: list[Loot]) -> UnitOrder:
        loot_weapons = []
        loot_ammo = []
        loot_shield_potions = []

        for loot in visible_loot:
            if isinstance(loot.item, Weapon):
                loot_weapons.append(loot)
            elif isinstance(loot.item, Ammo):
                loot_ammo.append(loot)
            else:
                loot_shield_potions.append(loot)

       # Find the nearest bow
        if len(loot_weapons) > 0:
            id = None
            init_distance = inf
            loot_position = Vec2(0.0, 0.0)
            for loot in loot_weapons:
                if loot.item.type_index == 2:
                    loot_distance = self.geometry.distance(loot.position, controlled_unit.position)
                    if loot_distance < init_distance:
                        init_distance = loot_distance
                        loot_position = loot.position
                        id = loot.id
            if init_distance < inf:
                if init_distance < constants.unit_radius:
                    return UnitOrder(
                        self.geometry.velocity_to_point(controlled_unit, loot_position),
                        self.geometry.velocity_to_point(controlled_unit, loot_position),
                        ActionOrder.Pickup(id))
                else:
                    return UnitOrder(
                        self.geometry.velocity_to_point(controlled_unit, loot_position),
                        self.geometry.velocity_to_point(controlled_unit, loot_position),
                        None)
        # Find the nearest ammo
        if len(loot_ammo) > 0:
            id = None
            init_distance = inf
            loot_position = Vec2(0.0, 0.0)
            for loot in loot_ammo:
                if loot.item.weapon_type_index == controlled_unit.weapon:
                    loot_distance = self.geometry.distance(loot.position, controlled_unit.position)
                    if loot_distance < init_distance:
                        init_distance = loot_distance
                        loot_position = loot.position
                        id = loot.id
                else:
                    loot_distance = self.geometry.distance(loot.position, controlled_unit.position)
                    if loot_distance < init_distance:
                        init_distance = loot_distance
                        loot_position = loot.position
                        id = loot.id

            if init_distance < inf:
                if init_distance < constants.unit_radius:
                    return UnitOrder(
                        self.geometry.velocity_to_point(controlled_unit, loot_position),
                        self.geometry.velocity_to_point(controlled_unit, loot_position),
                        ActionOrder.Pickup(id))
                else:
                    return UnitOrder(
                        self.geometry.velocity_to_point(controlled_unit, loot_position),
                        self.geometry.velocity_to_point(controlled_unit, loot_position),
                        None)

            # Find the nearest potion
            if len(loot_shield_potions) > 0:
                id = None
                init_distance = inf
                loot_position = Vec2(0.0, 0.0)
                for loot in loot_shield_potions:
                    loot_distance = self.geometry.distance(loot.position, controlled_unit.position)
                    if loot_distance < init_distance:
                        init_distance = loot_distance
                        loot_position = loot.position
                        id = loot.id
                if init_distance < inf:
                    if init_distance < constants.unit_radius:
                        return UnitOrder(
                            self.geometry.velocity_to_point(controlled_unit, loot_position),
                            self.geometry.velocity_to_point(controlled_unit, loot_position),
                            ActionOrder.Pickup(id))
                    else:
                        return UnitOrder(
                            self.geometry.velocity_to_point(controlled_unit, loot_position),
                            self.geometry.velocity_to_point(controlled_unit, loot_position),
                            None)

