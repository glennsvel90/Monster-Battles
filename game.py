import sys
import os

from character import Character
from combat import Combat
from monster import Goblin
from monster import Troll
from monster import Dragon



def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Game():
    """ The monster-battles game with functions """

    def setup(self):
        """ Create instances of all the characters in the game """
        self.player = Character()
        self.monsters = [
        Goblin(),
        Troll(),
        Dragon()
        ]
        self.monster = self.get_next_monster()
        
    def get_next_monster(self):
        """ Make the next monster be able to approach you """
        try:
            return self.monsters.pop(0)
            print("\n" + ">"*60 + "\n A Monster Is Approaching You!!")
        except IndexError:
            return None

    def monster_turn(self):
        """ Sequence of events during enemy's turn """
        if self.monster.attack():
            print("{} is attacking!".format(self.monster))

            if input('Do you want to try to dodge? Y/N  \n').lower() == 'y':
                if self.player.dodge():
                    print('You successfully dodged the attack!')
                else:
                    print('You still got hit')
                    self.player.hit_points -= 1
            else:
                print('{} hit one of your life hit points out!'.format(self.monster))
                self.player.hit_points -= 1
        else:
            print("{} isn't attacking this turn.".format(self.monster))

    def player_turn(self):
        """ Sequence of events during the player's turn """
        player_choice = input("Do you want to [A]ttack, [R]est, or [Q]uit \n").lower()
        if player_choice == 'a':
            print( "\n \n \n \n \n" + "O"*60)
            print("You're attacking {}".format(self.monster))
            if self.player.attack():
                if self.monster.dodge():
                    print ("{} dodged your attack!".format(self.monster))
                else:
                    if self.player.leveled_up():
                        self.monster.hit_points -= 2
                    else:
                        self.monster.hit_points -= 1
                    print("You HIT the {} with your {}!".format(self.monster,self.player.weapon))
            else:
                print("You missed!")
        elif player_choice == 'r':
            print("#"*60)
            self.player.rest()
        elif player_choice == 'q':
            sys.exit()
        else:
            self.player_turn()

    def cleanup(self):
        """ Events that occur after a monster is killed """
        if self.monster.hit_points <= 0:
            self.player.experience += self.monster.experience
            print("You KILLED the {}".format(self.monster))
            self.monster = self.get_next_monster()

    def __init__(self):
        self.setup()

        while self.player.hit_points and (self.monster or self.monsters):
            print('\n'+'='*20)
            print (self.player)
            self.monster_turn()
            print('-'*20)
            self.player_turn()
            self.cleanup()
            print('\n'+'='*20)

        if self.player.hit_points:
            print ("You Win!! Congratulations!!")
        elif self.monsters or self.monster:
            print("You were beaten. =( ")
        sys.exit()

Game()
