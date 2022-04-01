import pytest
from evercraft.models.character import Character, do_attack

#As an attacker I want to be able to damage my enemies so that they will die and I will live

#If attack is successful, other character takes 1 point of damage when hit

#If a roll is a natural 20 then a critical hit is dealt and the damage is doubled

#when hit points are 0 or fewer, the character is dead

#any attack that hits
def test_attackHits():
    # arrange
    obj = {
        "name" : "Bob",
        "alignment" : "Good",
        "attack": 8
    }
    roll = 18
    c1 = Character(obj)
    c2 = Character(obj)
    c1.attack = 9
    c2.armor = 7
    c2.HP = 5
    
    # act
    result = do_attack(c1, c2, roll) 

    # assert
    assert result == True

#critical attack
def test_attackCrit():
    obj = {
        "name" : "Bob",
        "alignment" : "Good",
        "attack": 8
    }
    roll = 20
    c1 = Character(obj)
    c2 = Character(obj)
    assert do_attack(c1, c2, roll)

