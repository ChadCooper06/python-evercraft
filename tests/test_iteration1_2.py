import pytest
from evercraft.models.character import Character

#As a character I want to have an alignment so that I have something to guide my actions
#can get and set alignment
#alignments are Good, Evil, and Neutral

def test_createCharacter_Alignment():
    character_name = "Bob"
    alignment = "Good"
    obj = {
        "name" : character_name,
        "alignment" : alignment
    }
    c = Character(obj)
    new_alignment = "Evil"
    c.set_alignment(new_alignment)
    assert c.get_alignment() == new_alignment
