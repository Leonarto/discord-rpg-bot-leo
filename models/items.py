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


class Weapon(Base):
    class Quality(enum.Enum):
        RUSTY = 'Rusty'
        NORMAL = 'Normal'
        REINFORCED = 'Reinforced'
        TEMPERED = 'Tempered'
        MAGICAL = 'Magical'
        LEGENDARY = 'Legendary'
        DIVINE = 'Divine'

    __tablename__ = 'weapon'

    id = Column(Integer, primary_key=True)
    speed_factor = Column(Float, default=1)
    critical_factor = Column(Float, default=1)

    physical = Column(Integer, default=0)
    fire = Column(Integer, default=0)
    ice = Column(Integer, default=0)
    electric = Column(Integer, default=0)
    poison = Column(Integer, default=0)
    light = Column(Integer, default=0)
    dark = Column(Integer, default=0)

    physical_penetration = Column(Integer, default=0)
    magic_penetration = Column(Integer, default=0)


class Consumable(Base):
    class Quality(enum.Enum):
        SMALL = 'Small'
        NORMAL = ''
        MEDIUM = 'Medium'
        BIG = 'Big'
        GRAND = 'Grand'
        LEGENDARY = 'Legendary'
        DIVINE = 'Divine'

    __tablename__ = 'consumable'

    id = Column(Integer, primary_key=True)
    health_amount = Column(Integer, default=0)
    stamina_amount = Column(Integer, default=0)
    soul_essence_amount = Column(Integer, default=0)
    speed_amount = Column(Integer, default=0)


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

    id = Column(Integer, primary_key=True)
    reflect = Column(Integer, default=0)
    block_chance = Column(Integer, default=0)

    physical = Column(Integer, default=0)
    fire = Column(Integer, default=0)
    ice = Column(Integer, default=0)
    electric = Column(Integer, default=0)
    poison = Column(Integer, default=0)
    light = Column(Integer, default=0)
    dark = Column(Integer, default=0)


class Item(Base):
    __tablename__ = 'item'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    base_price = Column(Integer, default=0)

    # Weapons
    weapon = Column(ForeignKey('weapon.id'), nullable=True)
    weapon_quality = Column(Enum(Weapon.Quality), default=None)

    # Consumables
    consumable = Column(ForeignKey('consumable.id'), nullable=True)
    consumable_quality = Column(Enum(Consumable.Quality), default=None)


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
