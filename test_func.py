from Module import Person, Wizard, HealthPotion
from main import *


# TESTS UNITAIRES SUR LES CLASSES

def test_Person():
    user_1 = Person("Hero")
    user_3 = Person("Lamba")
    user_4 = Person(10)
    #Test sur type
    assert isinstance(user_1.name,str)
    #Test sur PV (100)
    assert user_1.get_life_points() == 100
    #Test sur état
    assert user_1.is_dead() == False

    #Test sur PV après 1 hit (100-10)
    user_1.hit(user_3)
    assert user_3.get_life_points() == 90

    #Test sur PV + état après 10 hit (100-10*10)
    for i in range(10):
        user_3.hit(user_1)
    assert user_1.get_life_points() == 0
    assert user_1.is_dead() == True

    #Test sur PV + état après 4 hit (100-10*5)
    for i in range(4):
        user_1.hit(user_3)
    assert user_3.get_life_points() == 50
    assert user_3.is_dead() == False



def test_Wizard():
    user_2 = Wizard("Wizard")
    user_1 = Person("Hero")
    #Test sur PV (80)
    assert user_2.get_life_points() == 80

    #Test sur PV après 2 hit sur Person (100-15*2)
    for i in range(2):
        user_2.hit(user_1) 
    assert user_1.get_life_points() == 70

    #Test sur PV après 1 hit sur Wizard (80-10)
    user_1.hit(user_2)
    assert user_2.get_life_points() == 70

    #Test sur état après X hit sur Wizard menant mort obligatoire (80-10*14)
    for i in range(14):
        user_1.hit(user_2)
    assert user_2.is_dead() == True



def test_HealthPotion():
    user_2 = Wizard("Wizard")
    user_1 = Person("Hero")

    #Test sur état + PV après 5 hit de Wizard sur Person (100-15*5) puis prise 2 potions (25+10*2)
    for i in range(5):
        user_2.hit(user_1) 
    for i in range(2):
        HealthPotion.was_used_by(user_1)
    assert user_1.get_life_points() == 45
    assert user_1.is_dead() == False



# TESTS INTEGRATIONS

def test_while1():
    #Test avec while, Person hit Wizard (80-10*X)
    user_1 = Person("Hero")
    user_2 = Wizard("Wizard")
    while user_1.is_dead() == False and user_2.is_dead() == False:
        nb1 = 1
        if nb1 == 1 :
            user_1.hit(user_2)
        else:
            user_2.hit(user_1)
    assert user_2.get_life_points() == 0
    assert user_2.is_dead() == True



def test_while2():
    #Test avec while, Wizard hit Person (100-15*X)
    user_1 = Person("Hero")
    user_2 = Wizard("Wizard")
    while user_1.is_dead() == False and user_2.is_dead() == False:
        nb2 = 13
        if nb2 == 1 :
            user_1.hit(user_2)
        else:
            user_2.hit(user_1)
        bn2 = 5
        if bn2 == 0 :
            HealthPotion.was_used_by(user_1)
        elif bn2 == 1 :
            HealthPotion.was_used_by(user_2)
        else:
            pass

    assert user_1.get_life_points() == -5
    assert user_1.is_dead() == True



def test_while_potion1():
    user_1 = Person("Hero")
    user_2 = Wizard("Wizard")
    #Test avec while + potion, Person hit Wizard (80-10*X), Person boit potion(100+10*X)
    while user_1.is_dead() == False and user_2.is_dead() == False:
        nb1 = 1
        if nb1 == 1 :
            user_1.hit(user_2)
        else:
            user_2.hit(user_1)
        bn1 = 0
        if bn1 == 0 :
            HealthPotion.was_used_by(user_1)
        elif bn1 == 1 :
            HealthPotion.was_used_by(user_2)
        else:
            pass
    assert user_2.get_life_points() <= 0
    assert user_2.is_dead() == True
    assert user_1.get_life_points() == 180
    assert user_1.is_dead() == False



#BOULLE INFINIE
#def test_while_potion2():
#    user_1 = Person("Hero")
#    user_2 = Wizard("Wizard")
#     Test avec while + potion, Person hit Wizard (80-10*X), Wizard boit potion(80+10*X)
#    while user_1.is_dead() == False and user_2.is_dead() == False:
#        nb2 = 1
#        if nb2 == 1 :
#            user_1.hit(user_2)
#        else:
#            user_2.hit(user_1)
#        bn2 = 1
#        if bn1 == 0 :
#            HealthPotion.was_used_by(user_1)
#        elif bn2 == 1 :
#            HealthPotion.was_used_by(user_2)
#        else:
#            pass
#    assert user_2.get_life_points() == 80
#    assert user_2.is_dead() == False
#    assert user_1.get_life_points() == 100
#    assert user_1.is_dead() == False



def test_while_potion3():
    user_1 = Person("Hero")
    user_2 = Wizard("Wizard")
    #Test avec while + potion, Wizard hit Person (-15*X), Person boit potion(+10*X)
    #20 itérations
    user_1 = Person("Hero")
    user_2 = Wizard("Wizard")
    while user_1.is_dead() == False and user_2.is_dead() == False:
        x = 75687
        if x == 1 :
            user_1.hit(user_2)
            HealthPotion.was_used_by(user_2)
        else :
            user_2.hit(user_1)
            HealthPotion.was_used_by(user_1)
    assert user_1.get_life_points() == 0
    assert user_1.is_dead() == True


def test_divers():
    user_1 = Person("Hero")
    user_2 = Wizard("Wizard")
    #Test avec enchaînement divers
    user_2.hit(user_1)
    for i in range(2):
        HealthPotion.was_used_by(user_1)
    for i in range(5):
        user_1.hit(user_2)
    HealthPotion.was_used_by(user_2)
    for i in range(9):
        user_2.hit(user_1)
    assert user_1.get_life_points() == -30
    assert user_1.is_dead() == True
    assert user_2.get_life_points() == 40
    assert user_2.is_dead() == False
