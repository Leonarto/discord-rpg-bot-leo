from models import HeroClass
from services.ClassService import ClassService


def add_hero_classes():
    service = ClassService()
    service.add_hero_class(
        name=HeroClass.Classes.VILLAGER.value,
        strength=1,
        vitality=1,
        dexterity=1,
        cunning=1,
        intelligence=1,
        wisdom=1,
        charisma=1,
        luck=1
    )
    service.add_hero_class(
        name=HeroClass.Classes.FIGHTER.value,
        strength=5,
        vitality=4,
        dexterity=2,
        cunning=1,
        intelligence=0,
        wisdom=0,
        charisma=1,
        luck=0
    )
    service.add_hero_class(
        name=HeroClass.Classes.MAGE.value,
        strength=0,
        vitality=0,
        dexterity=0,
        cunning=1,
        intelligence=5,
        wisdom=5,
        charisma=0,
        luck=1
    )
    service.add_hero_class(
        name=HeroClass.Classes.ROGUE.value,
        strength=2,
        vitality=1,
        dexterity=3,
        cunning=4,
        intelligence=0,
        wisdom=0,
        charisma=2,
        luck=2
    )
    service.add_hero_class(
        name=HeroClass.Classes.MONK.value,
        strength=4,
        vitality=4,
        dexterity=0,
        cunning=0,
        intelligence=2,
        wisdom=2,
        charisma=0,
        luck=0
    )
