from models import HeroClass
from services.BaseService import BaseService


class ClassService(BaseService):
    def add_hero_class(self, **kwargs):
        hero_class = HeroClass(**kwargs)
        self.session.add(hero_class)
        self.session.commit()

    def get_hero_class(self, name: HeroClass.Classes = HeroClass.Classes.VILLAGER.value):
        return self.session.query(HeroClass).filter(HeroClass.name == name)[0]
