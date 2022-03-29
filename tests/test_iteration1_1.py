import pytest
from evercraft.models.character import Character

#As a character I want to have a name 
# so that I can be distinguished from other characters(multiple)
#can get and set Name

#just create a character
# def test_createCharacter():
#     c = Character()


#create a character class that can then be modified
def test_createCharacter_Class():
    c = Character()
    assert isinstance(c, Character)

#create character class with a name
def test_createCharacterClassWithName():
    c = Character("name")
    assert isinstance(c, Character)

# set a character name
def test_createCharacterWithSetName():
    character_name = "K"
    c = Character()
    c.set_name(character_name)
    assert c.name == character_name

#create character with obj
def test_createGetCharacterName():
    character_name = "Bob"
    obj = {
        "name" : character_name
    }
    c = Character(obj)
    assert c.get_name() == character_name
  