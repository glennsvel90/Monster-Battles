import random

class Combat(object):
    dodge_limit= 6
    min_dodge = 1
    attack_limit = 6
    min_attack = 1

    def dodge(self):
        roll=random.randint(self.min_dodge, self.dodge_limit)
        # if roll is returned, then the character dodged
        return roll > 4

    def attack(self):
        roll=random.randint(self.min_attack, self.attack_limit)
        # if the roll is returned the attack hitted the opposing character and the attack didn't miss only
        # on the attacker's end. The opposing character may send try to successfully or unsuccessfully dodge the
        # attack
        return roll > 4
