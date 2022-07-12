from model import Loot, Unit, Projectile
from config import *
from saved_loot import SavedLoot
from geometry import *


class MyMemory:
    loot: list[SavedLoot]
    # enemies: list[Unit]
    projectiles: list[Projectile]

    def update(self, current_tick: int):
        # обновляем список лута
        # 1) ищем id лута, который сейчас видим
        # 2) бежим по старой памяти и копируем из нее лут
        #  который не видим в пункте 1 и
        #  который не находится в нашем поле зрения
        # 3) Новый лут в памяти: то, что скопировали + видимый лут

        current_loot = GAME.loot
        all_loot = []
        loot_ids = set(current_loot)
        #for item in cur_loot:
           #loot_ids.add(item.id)
        for item in self.loot:
            if distance(item.loot.position, GAME.zone.current_center) > GAME.zone.current_radius:
                item.is_alive = False
            if item.is_alive and not (item.loot.id in loot_ids or item.loot.id not in loot_ids and unit_can_see_point(my_unit, item.loot.position)):
                all_loot.append(item)
        for item in current_loot:
            all_loot.append(Loot(item, GAME.current_tick))

        self.loot = all_loot



