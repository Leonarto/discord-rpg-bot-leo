from test_main import db_from_scratch
from unittest import TestCase
from models import HeroClass
from services.HeroService import HeroService


class TestHeroService(TestCase):
    def setUp(self):
        db_from_scratch()
        self.service = HeroService()

    def test_hero_creation(self):
        self.service.create_hero('John', 123)
        self.assertTrue(self.service.hero_exists('John', 123))
        self.assertRaises(Exception, self.service.create_hero, 'John', 123)

    def test_get_selected_hero(self):
        self.service.create_hero('John', 123)
        hero = self.service.get_selected_hero(123)
        self.assertEqual(hero.name, 'John')
        self.assertTrue(hero.is_selected)

    def test_assign_name_creation_and_name_change(self):
        self.service.assign_name('John', 123)
        self.assertTrue(self.service.hero_exists('John', 123))

        self.service.assign_name('Edgard', 123)
        self.assertFalse(self.service.hero_exists('John', 123))
        self.assertTrue(self.service.hero_exists('Edgard', 123))

    def test_get_hero_stats(self):
        hero = self.service.assign_name('John', 123)
        hero = self.service.assign_class_by_name(hero, HeroClass.Classes.FIGHTER.value)

        stats = self.service.get_stats(hero)
        self.assertEqual(stats.vitality, 5)

        hero = self.service.assign_name('Golo', 123)
        hero = self.service.assign_class_by_name(hero, HeroClass.Classes.MAGE.value)

        self.assertEqual(stats.strength, 6)

        stats = self.service.get_stats(hero)

        self.assertEqual(stats.strength, 1)
        self.assertEqual(stats.intelligence, 6)

        hero.exp = 200
        stats = self.service.get_stats(hero)

        self.assertEqual(stats.level, 3)

    def test_hero_equip(self):
        pass
