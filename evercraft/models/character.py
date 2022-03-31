# this is where your character code will go

class Character:
    def __init__(self, obj):
        self.name = obj["name"],
        self.alignment = obj["alignment"],
        self.armor = obj["armor"],
        self.HP = obj["HP"],
        self.attack = obj["attack"],
        self.Str = obj["Str"],
        self.Dex = obj["Dex"],
        self.Con = obj["Con"],
        self.Wis = obj["Wis"],
        self.Int = obj["Int"],
        self.Cha = obj["Cha"]
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

#determine if alive or not
    def alive(self):
        if self.HP <= 0:
            return False

#determine if Character has the 6 abilities
        

# #function to ATTACK
def do_attack(c1, c2, roll):
    if roll == 20:
        return True
    elif roll < c2.armor:
        return False
    elif roll >= c2.armor:
        return True

# function to doDmg
def dmg(c2, roll):
    hit = 1
    if roll == 20:
        hit = hit * 2
    c2.HP = c2.HP - hit

# #function if dead
# def dead(c2, alive):
#     if c2.HP <= 0:
#         c2.alive is c2.HP
        

# def did_dmg(attack, c2):
#     if roll == True:
#         return c2.HP - 2
#     elif attack == "Missed":
#         return c2.HP
#     else attack == "Hit":
#         return c2.HP - 1

# def dmg(atkr, dfind):
#     if c1.attack > c2.armor:
#         return c2.HP-1

#def hit(c1, c2):
    #if "Hit" == True:
        #c2.HP = c2.HP-1

# def dead(c2):
#     if c2.life != dead:
#         return False
#     else:
#         return True