import pytest
from evercraft.models.character import Character, do_attack

#As a combatant I want to be able to attack other combatants so that I can survive to fight another day
#roll a 20 sided die (don't code the die)

#roll must meet or beat opponents armor class to hit
def test_canAttack():
    assert attack(10) == 10

#a natural roll of 20 always hits
def test_attackCrit():
    assert attack(20) == "Critical Hit"

def test_attackMiss():
    assert attack(1) == "Missed"

def test_attackLess():
    obj = {
        "name" : "Bob",
        "alignment" : "Good",
        "armor" : 10,
        "HP": 5,
        "attack": 8
    }
    c1 = Character(obj)
    c2 = Character(obj)
    c2.armor = 10
    assert attack(c2, 8) == "Missed"

def test_attackHigh():
    obj = {
        "name" : "Bob",
        "alignment" : "Good",
        "armor" : 10,
        "HP": 5,
        "attack": 8
    }
    c1 = Character(obj)
    c2 = Character(obj)
    c2.armor = 7
    assert attack(c2, 9) == "Hit"