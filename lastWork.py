# Задача 17.3
import random


class Combat:
    Nick = "Alex"
    HP = 100
    MP = 100
    Armor = 5
    __Attack = 10
    __Lvl = 1

    def __init__(self, n, w):
        self.HP = n
        self.Armor = w

    def lvlUp(self, experience):
        self.__Lvl += experience - Combat.__Lvl

    def get_lvl(self):
        return self.__Lvl

    def set_attack(self, upLvl):
        self.__Attack += upLvl - Combat.__Attack

    def get_attack(self):
        return self.__Attack


class Paladin(Combat):
    Russ = "Human"

    def get_lvl(self):
        print("Переопределение из класса Paladin")
        return 10


class Mage(Combat):
    Russ = "Goblin"

    def get_lvl(self):
        print("Переопределение из класса Mage")
        return 50


user1 = Mage(600, 10)
user1.Nick = "Bill"
user1.set_attack(13)
user1.Russ = "Goblin"
user1.lvlUp(25)

user2 = Paladin(1500, 50)
user2.Nick = "Matt"
user2.set_attack(56)
user2.Russ = "Human"
user2.lvlUp(50)

print(
"user1 lvl - ", user1.get_lvl(), ", user2 lvl - ", user2.get_lvl(), " \n", "user1 hp  - ", user1.HP, ", user2 hp - ",
user2.HP, " \n", "user1 armor - ", user1.Armor, ", user2 armor - ", user2.Armor)
print("user1 attack - ", user1.get_attack(), ", user2 attack - ", user2.get_attack())

lo = []
for i in range(10):
    y = random.randint(1, 10)
    m = random.randint(100, 1000)
    n = random.randint(10, 100)
    if (y % 2 == 0):
        user_i = Mage(m, n)
        lo.append(user_i)
    else:
        user_i = Paladin(m, n)
        lo.append(user_i)
    print(lo[i].get_lvl())