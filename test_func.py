from Module import Person, Wizard, HealthPotion
from main import *

def test_Person():
    P1 = Person("Hero")
    P2 = Person("Second")
    P3 = Person(10)
    assert isinstance(P1.name,str)
    assert P1.get_life_points() == 100

    P1.hit(P2)
    assert P2.get_life_points() == 90

    for i in range(10):
        P2.hit(P1)
    assert P1.get_life_points() == 0
    assert P1.is_dead() == True


def test_Wizard():
    W1 = Wizard("Wizard")
    P1 = Person("Hero")
    assert W1.get_life_points() == 80

    for i in range(2):
        W1.hit(P1) 
    assert P1.get_life_points() == 70

    P1.hit(W1)
    assert W1.get_life_points() == 70


def test_HealthPotion():
    W1 = Wizard("Wizard")
    P1 = Person("Hero")
    for i in range(5):
        W1.hit(P1) 
    for i in range(2):
        HealthPotion.was_used_by(P1)
    assert P1.get_life_points() == 45

