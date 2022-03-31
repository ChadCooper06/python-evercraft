# this is where your character code will go

#create a character--passed
# def Character():
#     pass

#create a character class--passed
# class Character():
#     def __init__(self):
#         self.data = "character"

#character class with a name--passed
# class Character():
#     def __init__(self, name):
#          self.name = "name"

#character named something--passed
# class Character():
#     def __init__(self, name = "Bob"):
#         print (name)
#         self.name = name

#     def set_name(self, name):
#         self.name = name

#     def get_name(self):
#         self.name = name

#character with name as an object--passed
# class Character():
#     def __init__(self, obj = {"name":"Bob"}):
#         if obj:
#             self.name = obj["name"]

#     def set_name(self, name):
#         self.name = name

#     def get_name(self):
#         return self.name

# def set_var(): {
#     "name" : name,
#     "alignment" : alignment,
#     "armor" : armor_level
# }
# def get_var(): {
#     "name" : name,
#     "alignment" : alignment,
#     "armor" : armor_level
# }

class Character:
    def __init__(self, obj):
        self.name = obj["name"],
        self.alignment = obj["alignment"],
        self.armor = obj["armor"],
        self.HP = obj["HP"],
        self.attack = obj["attack"]
#helper fns that get and set name
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

#helper fns that set and get alignment of good, evil or neutral
    def set_alignment(self, alignment):
        self.alignment = alignment

    def get_alignment(self):
        return self.alignment

#helper fns that set and get armor    
    def set_armor_level(self, armor):
        self.armor = armor

    def get_armor_level(self):
        return self.armor

#function that sets initial HP to 5
    def set_hit_points(self, HP):
        self.HP = HP

#function that gets HP
    def get_hit_points(self):
        return self.HP

# #function to ATTACK
#     def set_attack(self, attack):
#         self.attack = attack


def do_attack(c1, c2, roll):
    if roll == 20:
        return True
    elif roll < c2.armor:
        return False
    elif roll >= c2.armor:
        return True

# function to doDmg


# def xpReduce(attack, c2):
#     if attack == "Critical Hit":
#         return c2.XP - 2
#     elif attack == "Missed":
#         return c2.XP
#     else attack == "Hit":
#         return c2.XP - 1

# def dmg(atkr, dfind):
#     if c1.attack > c2.armor:
#         return c2.HP-1

#def hit(c1, c2):
    #if "Hit" == True:
        #c2.HP = c2.HP-1