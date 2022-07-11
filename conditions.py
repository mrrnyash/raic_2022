

class Conditions:
    CONDITIONS = {}
    # Условие для вступления в бой (attack)
    CONDITIONS['ATTACK'] = 'len(game.units) == 2 and controlled_unit.health == constants.unit_health' \
        ' and controlled_unit.shield >= constants.max_shield / 2'
    # Условие для побега (run_away)
    CONDITIONS['RUN_AWAY'] = 'controlled_unit.health < constants.unit_health - (constants.unit_health / 4)'
    # Условия для принятия зелья щита (use_shield_potion)
    CONDITIONS['USE_SHIELD_POTION'] = 'controlled_unit.shield < constants.max_shield' \
                                      ' and controlled_unit.shield_potions > 0'
    # TODO: Условие для определения того, что юнит находится над нужным оружием (take_bow)
    CONDITIONS['TAKE_BOW'] = ''
    # TODO: Условие для определения того, что юнит находится над зельем щита (take_shield_potion)
    CONDITIONS['TAKE_SHIELD_POTION'] = ''
    # TODO: Условие для определения того, что юнит находится над нужными патронами (take_ammo)
    CONDITIONS['TAKE_AMMO'] = ''
    # TODO: Условие для определения края зоны и побега от нее (run_from_edge)
    CONDITIONS['RUN_FROM_EDGE'] = ''
    # TODO: Условие для уклонения (evade)
    CONDITIONS['EVADE'] = ''
    # TODO: Условие для блуждания (wander)
    CONDITIONS['WANDER'] = ''
    # TODO: Условие для ожидания (idle)
    CONDITIONS['IDLE'] = ''
