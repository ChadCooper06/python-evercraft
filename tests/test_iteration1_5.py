import pytest
from evercraft.models.character import Character, attack, dmg

#As an attacker I want to be able to damage my enemies so that they will die and I will live

#If attack is successful, other character takes 1 point of damage when hit

#If a roll is a natural 20 then a critical hit is dealt and the damage is doubled

#when hit points are 0 or fewer, the character is dead


def test_attackHits():
    obj = {
        "name" : "Bob",
        "alignment" : "Good",
        "armor" : 10,
        "HP": 5,
        "attack": 8
    }
    c1 = Character(obj)
    c2 = Character(obj)
    c1.attack = 9
    c2.armor = 7
    c2.HP = 5
    assert c1.attack >= c2.armor

def test_attackCrit():
    obj = {
        "name" : "Bob",
        "alignment" : "Good",
        "armor" : 10,
        "HP": 5,
        "attack": 8
    }
    c1 = Character(obj)
    c2 = Character(obj)
    c1.attack = 20
    c2.armor = 10
    c2.HP = 2
    assert c1.attack > c2.armor