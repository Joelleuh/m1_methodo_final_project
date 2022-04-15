from Module import Person, Wizard, HealthPotion
from main import *

# TESTS UNITAIRES SUR LES CLASSES

def test_Person():
    user_1 = Person("Hero")
    user_3 = Person("Lamba")
    user_4 = Person(10)
    #Test sur type
    assert isinstance(user_1.name,str)
