import pytest
from evercraft.models.character import Character, do_attack, dmg

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
        "attack": 11
    }
    roll = 18
    c1 = Character(obj)
    c2 = Character(obj)
    c1.attack = 9
    c2.armor = 6
    c2.HP = 5
    new_HP = 4
    dmg(c2,roll)
    assert new_HP == c2.HP

def test_didDoubleDmg():
    obj = {
        "name" : "Bob",
        "alignment" : "Good",
        "armor" : 10,
        "HP": 5,
        "attack": 11
    }
    roll = 20
    c1 = Character(obj)
    c2 = Character(obj)
    c1.attack = 9
    c2.armor = 6
    c2.HP = 5
    new_HP = 3
    dmg(c2,roll)
    assert new_HP == c2.HP

def test_heDied():
    obj = {
        "name" : "Bob",
        "alignment" : "Good",
        "armor" : 10,
        "HP": 5,
        "attack": 11
    }
    c1 = Character(obj)
    c2 = Character(obj)
    c2.HP = 0
    assert c2.alive() == False