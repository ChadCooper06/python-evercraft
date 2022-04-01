import pytest
from evercraft.models.character import Character, do_attack, dmg

#As a character I want to have several abilities 
#so that I am /= to other characters except in name

#Abilities are 
#Strength, Dexterity, Constitution, 
#Wisdom, Intelligence, Charisma

#Abilities range from 1 to 20 and default to 10
#Abilities have modifiers according to the following table
"""{
    1:	-5,			
    2:	-4,			
    3:	-4,			
    4:	-3,			
    5:	-3,
    6:	-2,
    7:	-2,
    8:	-1,
    9:	-1,			
    10:	0,
    11:	0,
    12:	+1,
    13:	+1,
    14:	+2,
    15:	+2,
    16:	+3,
    17:	+3,
    18:	+4,
    19:	+4,
    20:	+5
}"""

# testing if the character created has the abilities and they're all defaults
def test_abilities():
    obj = {
        "name" : "Bob",
        "alignment" : "Good",
        "attack": 11,
    }
    c1 = Character(obj)

    assert c1.Str == 10 and c1.Dex == 10 and c1.Con == 10 and c1.Wis == 10 and c1.Int == 10 and c1.Cha == 10

# testing if abilities have a range
# def test_ability_range():
#     obj = {
#         "name" : "Bob",
#         "alignment" : "Good",
#         "attack": 11,
#     }
#     c1 = Character(obj)
#     c1.Str = 13
#     assert c1.Str == 