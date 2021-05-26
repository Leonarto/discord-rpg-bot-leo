from models import Hero, Monster, NPC


class Stats:
    PRE_ADDITIVE_STAT_KEYS = [
        'exp',
        'strength',
        'vitality',
        'dexterity',
        'cunning',
        'intelligence',
        'wisdom',
        'charisma',
        'luck'
    ]

    POST_ADDITIVE_STAT_KEYS = [
        'add_max_health',
        'add_max_stamina',
        'add_max_soul_essence',
        'add_max_speed'
    ]

    exp = 0

    strength = 0
    vitality = 0
    dexterity = 0
    cunning = 0
    intelligence = 0
    wisdom = 0
    charisma = 0
    luck = 0

    add_max_health = 0
    add_max_stamina = 0
    add_max_soul_essence = 0
    add_max_speed = 0

    @property
    def level(self):
        return int(1 + (self.exp / 100))

    @property
    def level_stat_multiplier(self):
        return 1 + (self.level * .01)

    @property
    def max_health(self):
        base = 20
        level = 5 * self.level
        vitality = 3 * self.vitality * self.level_stat_multiplier
        strength = .5 * self.strength * self.level_stat_multiplier
        return int(base + level + vitality + strength) + self.add_max_health

    @property
    def max_stamina(self):
        base = 20
        level = 2 * self.level
        vitality = 1 * self.vitality * self.level_stat_multiplier
        strength = 1 * self.strength * self.level_stat_multiplier
        dexterity = 1 * self.dexterity * self.level_stat_multiplier
        cunning = 1 * self.dexterity * self.level_stat_multiplier
        return int(base + level + vitality + strength + dexterity + cunning) + self.add_max_stamina

    @property
    def max_soul_essence(self):
        base = 20
        level = 2 * self.level
        intelligence = 1 * self.intelligence * self.level_stat_multiplier
        wisdom = 3 * self.wisdom * self.level_stat_multiplier
        return int(base + level + intelligence + wisdom) + self.add_max_soul_essence

    @property
    def speed(self):
        base = 1
        strength = .05 * self.strength
        dexterity = .1 * self.dexterity
        cunning = .01 * self.cunning
        intelligence = .02 * self.intelligence
        wisdom = .01 * self.wisdom
        return base + strength + dexterity + cunning + intelligence + wisdom + self.add_max_speed


class StatsService:
    @classmethod
    def get_stats(
            cls,
            hero: Hero = None,
            npc: NPC = None,
            monster: Monster = None
    ):
        if hero:
            return cls.get_hero_stats(hero)
        elif npc:
            return cls.get_npc_stats(npc)
        elif monster:
            return cls.get_monster_stats(monster)
        else:
            raise Exception('You need to pass either hero, npc or monster to get_stats')

    @classmethod
    def get_hero_stats(cls, hero: Hero):
        instances = [hero]
        if hero.hero_class:
            instances += [hero.hero_class]
        return cls._get_additive_stats(instances)

    @classmethod
    def get_npc_stats(cls, npc: NPC):
        return cls._get_additive_stats([npc])

    @classmethod
    def get_monster_stats(cls, monster: Monster):
        return cls._get_additive_stats([monster])

    @classmethod
    def _get_additive_stats(cls, instances: list):
        stats = Stats()
        for stat_key in (stats.PRE_ADDITIVE_STAT_KEYS + stats.POST_ADDITIVE_STAT_KEYS):
            stat_value = cls._get_additive_stat(stat_key, instances)
            setattr(stats, stat_key, stat_value)
        return stats

    @classmethod
    def _get_additive_stat(cls, stat_key: str, instances: list):
        stat_value = 0
        for instance in instances:
            if hasattr(instance, stat_key):
                stat_value += getattr(instance, stat_key)
        return stat_value
