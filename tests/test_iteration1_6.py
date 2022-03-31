import pytest
from evercraft.models.character import Character, do_attack

#As an attacker I want to be able to damage my enemies so that they 
# will die and I will live

#If attack is successful, other character takes 1 point of damage when hit
#If a roll is a natural 20 then a critical hit is dealt damage x2
#when hit points are 0 or fewer, the character is dead

def test_didDoDmg():
    obj = {
        "name" : "Bob",
        "alignment" : "Good",
        "armor" : 10,
        "HP": 5,
        "attack": 8
    }
    roll = 14
    c1 = Character(obj)
    c2 = Character(obj)

    assert dmg((c2.HP - 1), roll)