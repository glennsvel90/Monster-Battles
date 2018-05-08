import unittest
import character
import combat



class CombatTests(unittest.TestCase):
    def test_dodge(self):
        combat.Combat.dodge_limit = 1
        self.player = character.Character()
        assert not self.player.dodge() is True

    def test_attack(self):
        combat.Combat.min_attack = 5
        self.player2 = character.Character()
        assert self.player2.attack() is True
