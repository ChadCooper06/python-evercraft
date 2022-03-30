import pytest
from evercraft.models.character import Character

#As a combatant I want to have an armor class

    #Armor Class that defaults to 10
    #Set Armor Class
def test_createArmorClass():
    character_name = "Bob"
    alignment = "Good"
    armor_level = 10
    obj = {
        "name" : character_name,
        "alignment" : alignment,
        "armor" : armor_level
    }
    c = Character(obj)
    c.set_armor_level(armor_level) 
    assert c.armor == armor_level
    
# get armor class
def test_createArmorClass():
    character_name = "Bob"
    alignment = "Good"
    armor_level = 10
    obj = {
        "name" : character_name,
        "alignment" : alignment,
        "armor" : armor_level
    }
    c = Character(obj)
    new_armor_level = 12
    c.set_armor_level(new_armor_level) 
    assert c.get_armor_level() == new_armor_level

#As a combatant I want to have hit points so that I can resist attacks

    #I have 5 Hit Points by default

def test_createHitPoints():
    character_name = "Bob"
    alignment = "Good"
    armor_level = 10
    hit_points = 5
    obj = {
        "name" : character_name,
        "alignment" : alignment,
        "armor" : armor_level,
        "HP": hit_points
    }
    c = Character(obj)
    c.set_hit_points(hit_points)
    assert c.HP == hit_points

def test_modifyHitPoints():
    character_name = "Bob"
    alignment = "Good"
    armor_level = 10
    hit_points = 5
    obj = {
        "name" : character_name,
        "alignment" : alignment,
        "armor" : armor_level,
        "HP": hit_points
    }
    c = Character(obj)
    new_hit_points = 6
    c.set_hit_points(new_hit_points)
    assert c.get_hit_points() == new_hit_points
