import random
from combat import Combat
COLORS= ['yellow', 'red', 'blue', 'green']


class Monster(Combat):
    min_hit_points=1
    max_hit_points=10
    min_experience=1
    max_experience=15
    weapon='sword'
    sound='roar'

    def __init__(self, **kwarg):
        self.hit_points=random.randint(self.min_hit_points,self.max_hit_points)
        self.experience=random.randint(self.min_experience,self.max_experience)
        self.color=random.choice(COLORS)

        for k,v in kwarg.items():
            setattr(self,k,v)
        # self.hit_points=kwarg.get('hit_points', 1)
        # self.weapon=kwarg.get('weapon', 'sword')
        # self.sound=kwarg.get('sound', 'roar')
        # self.color=kwarg.get('color', 'yellow')
    def __str__(self):
        return '{} {} (HP:{}, XP:{})'.format(self.color.title(),
        self.__class__.__name__, self.hit_points, self.experience)


    def battlecry(self):
        return self.sound.upper()


class Goblin(Monster):
    max_hit_points=3
    max_experience=4
    sound='gob'

class Troll(Monster):
    min_hit_points=2
    max_hit_points=7
    min_experience=3
    max_experience=10
    sound='oooll'

class Dragon(Monster):
    min_hit_points=7
    max_hit_points=11
    min_experience=8
    max_experience=15
    sound='raaaaaaaar'
