import logging
logging.basicConfig(filename='char.log', level=logging.DEBUG)
from combat import Combat
import random

class Character(Combat):
    """ The user player's character """
    
    attack_limit=10
    experience=0
    base_hit_points=10
    
    def __init__(self,**kwarg):
        """ Ask for player's name """
        
        self.name= input("What's your name: ")
        self.weapon=self.get_weapon()
        self.hit_points=self.base_hit_points

        for k,v in kwarg.items():
            setattr(self,k,v)

    def attack(self):
        """ attacks a monster """
        
        roll=random.randint(1,self.attack_limit)
        if self.weapon=='sword':
            roll+=1
        elif self.weapon=='axe':
            roll+=2
        return roll >4

    def get_weapon(self):
        """ Makes main character choose a sword, axe, or bow """
        
        weapon_choice=input('Choose a weapon: [S]word, [A]xe, [B]ow: ').lower()

        if weapon_choice in 'sab':
            if weapon_choice=='s':
                return 'sword'
            elif weapon_choice=='a':
                return 'axe'
            else:
                return 'bow'
        else:
            return self.get_weapon()

    def __str__(self):
        """ Return the character name, HP,  and XP """
        
        return '{} (HP:{}, XP:{})'.format(self.name, self.hit_points,self.experience)

    def rest(self):
        """ Increase life hit points by 1 """
        
        if self.hit_points<self.base_hit_points:
            self.hit_points+=1

    def leveled_up(self):
        """ Level up the main character """
        
        return self.experience>=5
