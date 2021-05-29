import enum
from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey, Float
from sqlalchemy.orm import relationship
from db_engine import Base


class Storage(Base):
    class StorageTypes(enum.Enum):
        INVENTORY = 'Inventory'
        VAULT = 'Vault'
        CHEST = 'Chest'

    __tablename__ = 'storage'

    id = Column(Integer, primary_key=True)
    hero = Column(ForeignKey('hero.id'), default=None)
    type = Column(Enum(StorageTypes), default=StorageTypes.CHEST)
    size = Column(Integer, default=30)


class Item(Base):
    id = Column(Integer, primary_key=True)
    speed_factor = Column(Float, default=1)
    critical_factor = Column(Float, default=1)
    reflect = Column(Integer, default=0)
    block_chance = Column(Integer, default=0)

    add_max_health = Column(Integer, default=0)
    add_max_stamina = Column(Integer, default=0)
    add_max_soul_essence = Column(Integer, default=0)

    health_per_second = Column(Integer, default=0)
    stamina_per_second = Column(Integer, default=0)
    soul_essence_per_second = Column(Integer, default=0)

    physical = Column(Integer, default=0)
    fire = Column(Integer, default=0)
    ice = Column(Integer, default=0)
    electric = Column(Integer, default=0)
    poison = Column(Integer, default=0)
    light = Column(Integer, default=0)
    dark = Column(Integer, default=0)
    gravity = Column(Integer, default=0)
    space = Column(Integer, default=0)

    magic_res = Column(Integer, default=0)
    elemental_res = Column(Integer, default=0)

    physical_res = Column(Integer, default=0)
    fire_res = Column(Integer, default=0)
    ice_res = Column(Integer, default=0)
    electric_res = Column(Integer, default=0)
    poison_res = Column(Integer, default=0)
    light_res = Column(Integer, default=0)
    dark_res = Column(Integer, default=0)
    gravity_res = Column(Integer, default=0)
    space_res = Column(Integer, default=0)

    physical_penetration = Column(Integer, default=0)
    magic_penetration = Column(Integer, default=0)

    __mapper_args__ = {
        'polymorphic_identity': 'item',
        'polymorphic_on': type
    }


class Weapon(Item):
    class Quality(enum.Enum):
        RUSTY = 'Rusty'
        NORMAL = 'Normal'
        REINFORCED = 'Reinforced'
        TEMPERED = 'Tempered'
        MAGICAL = 'Magical'
        LEGENDARY = 'Legendary'
        DIVINE = 'Divine'

    __tablename__ = 'weapon'

    quality = Column(Enum(Quality), default=Quality.RUSTY)

    __mapper_args__ = {
        'polymorphic_identity': 'weapon'
    }


class Consumable(Item):
    class Quality(enum.Enum):
        SMALL = 'Small'
        NORMAL = ''
        MEDIUM = 'Medium'
        BIG = 'Big'
        GRAND = 'Grand'
        LEGENDARY = 'Legendary'
        DIVINE = 'Divine'

    __tablename__ = 'consumable'

    quality = Column(Enum(Quality), default=Quality.SMALL)

    health = Column(Integer, default=0)
    stamina = Column(Integer, default=0)
    soul_essence = Column(Integer, default=0)

    __mapper_args__ = {
        'polymorphic_identity': 'consumable'
    }


class Wearable(Base):
    class Quality(enum.Enum):
        RUSTY = 'Rusty'
        NORMAL = 'Normal'
        REINFORCED = 'Reinforced'
        TEMPERED = 'Tempered'
        MAGICAL = 'Magical'
        LEGENDARY = 'Legendary'
        DIVINE = 'Divine'

    __tablename__ = 'wearable'

    quality = Column(Enum(Quality), default=Quality.SMALL)

    __mapper_args__ = {
        'polymorphic_identity': 'wearable'
    }


class StorageItem(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    quality = Column(String, default=None)
    storage = Column(ForeignKey('storage.id'))
    item = Column(ForeignKey('item.id'))


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, primary_key=True)
    hero = Column(ForeignKey('item.id'))

    head = Column(ForeignKey('item.id'), default=None)
    chest = Column(ForeignKey('item.id'), default=None)
    shoulders = Column(ForeignKey('item.id'), default=None)
    arms = Column(ForeignKey('item.id'), default=None)
    hands = Column(ForeignKey('item.id'), default=None)
    legs = Column(ForeignKey('item.id'), default=None)
    feet = Column(ForeignKey('item.id'), default=None)
    right_finger = Column(ForeignKey('item.id'), default=None)
    left_finger = Column(ForeignKey('item.id'), default=None)
    right_ear = Column(ForeignKey('item.id'), default=None)
    left_ear = Column(ForeignKey('item.id'), default=None)
    cape = Column(ForeignKey('item.id'), default=None)
    eyes = Column(ForeignKey('item.id'), default=None)
