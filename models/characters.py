import enum
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from db_engine import Base


class Character(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True)
    name = Column(String)
    exp = Column(Integer, default=0)

    # Current
    health = Column(Integer, default=0)
    stamina = Column(Integer, default=0)
    soul_essence = Column(Integer, default=0)

    # Stats
    strength = Column(Integer, default=1)
    vitality = Column(Integer, default=1)
    dexterity = Column(Integer, default=1)
    cunning = Column(Integer, default=1)
    intelligence = Column(Integer, default=1)
    wisdom = Column(Integer, default=1)
    charisma = Column(Integer, default=1)
    luck = Column(Integer, default=1)

    karma = Column(Integer, default=0)


class NPCType(Character):
    """
    It represents the stats an NPC have when it's created, we should copy all fields to
    the npc or monster adding some variance to the central NPCType values.
    """
    __tablename__ = 'npc_type'

    __mapper_args__ = {
        'polymorphic_identity': 'npc_type',
        'concrete': True
    }


class NPC(Character):
    """
    When created it should be based of an NPCType with some variance, the name should
    be different as the NPCType
    """
    __tablename__ = 'npc'

    npc_type_id = Column(ForeignKey('npc_type.id'))
    npc_type = relationship('NPCType')

    __mapper_args__ = {
        'polymorphic_identity': 'npc',
        'concrete': True
    }


class Monster(Character):
    """
    When created it should be based of an NPCType with some variance, the name should
    be the same as the NPCType
    """
    __tablename__ = 'monster'

    npc_type_id = Column(ForeignKey('npc_type.id'))
    npc_type = relationship('NPCType')

    __mapper_args__ = {
        'polymorphic_identity': 'monster',
        'concrete': True
    }


class HeroClass(Character):
    """
    This holds the classes a hero can choose, and the HeroClass attributes are added to the Hero attributes.
    """
    class Classes(enum.Enum):
        VILLAGER = 'Villager'
        FIGHTER = 'Fighter'
        MAGE = 'Mage'
        ROGUE = 'Rogue'
        MONK = 'Monk'

    __tablename__ = 'hero_class'

    __mapper_args__ = {
        'polymorphic_identity': 'hero_class',
        'concrete': True
    }


class Hero(Character):
    """
    The Hero which is owned by a player.
    """
    __tablename__ = 'hero'

    owner_id = Column(Integer)
    is_selected = Column(Boolean, default=False)

    hero_class_id = Column(ForeignKey('hero_class.id'))
    hero_class = relationship('HeroClass')

    __mapper_args__ = {
        'polymorphic_identity': 'hero',
        'concrete': True
    }
