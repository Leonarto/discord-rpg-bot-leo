from models import Hero, HeroClass
from services.BaseService import BaseService
from services.StatsService import StatsService
from services.ClassService import ClassService


class HeroService(BaseService):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.class_service = ClassService()

    def get_stats(self, hero: Hero):
        return StatsService.get_stats(hero=hero)

    def get_selected_hero(self, owner_id: int):
        return self._selected_hero_query(owner_id)[0]

    def assign_name(self, name: str, owner_id: int):
        heroes_query = self._selected_hero_query(owner_id)
        hero_count = heroes_query.count()

        if hero_count == 0:
            return self.create_hero(name, owner_id)
        elif hero_count == 1:
            hero = heroes_query[0]
            hero.name = name
            self.session.add(hero)
            self.session.commit()
            return heroes_query[0]
        else:
            raise Exception('More than one selected heroes error')

    def assign_class_by_name(self, hero: Hero, name: HeroClass.Classes = HeroClass.Classes.VILLAGER.value):
        hero_class = self.class_service.get_hero_class(name)
        return self.assign_class(hero, hero_class)

    def assign_class(self, hero: Hero, hero_class: HeroClass):
        hero.hero_class = hero_class
        self.session.add(hero)
        self.session.commit()
        return hero

    def create_hero(self, name: str, owner_id: int):
        hero_exists = self.hero_exists(name, owner_id)
        if hero_exists:
            raise Exception('Hero already exists with name %s and owner_id %s' % (name, owner_id))

        self._selected_hero_query(owner_id).update({"is_selected": False})

        hero_class = self.class_service.get_hero_class()
        new_hero = Hero(owner_id=owner_id, name=name, is_selected=True, hero_class_id=hero_class.id)
        self.session.add(new_hero)
        self.session.commit()
        return new_hero

    def _selected_hero_query(self, owner_id: int):
        return self.session.query(Hero) \
            .filter(Hero.owner_id == owner_id) \
            .filter(Hero.is_selected == True)

    def hero_exists(self, name: str, owner_id: int):
        return bool(
            self.session.query(Hero) \
                .filter(Hero.owner_id == owner_id) \
                .filter(Hero.name == name) \
                .count()
        )
