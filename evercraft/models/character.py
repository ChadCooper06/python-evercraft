# this is where your character code will go

class Character:
    def __init__(self, obj):
        self.name = obj["name"]
        self.alignment = obj["alignment"]
        self.armor = 10
        self.HP = 5
        self.attack = obj["attack"]
        self.Str = 10
        self.Dex = 10
        self.Con = 10
        self.Wis = 10
        self.Int = 10
        self.Cha = 10
            
        
        
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

    #determine range of abilities
    


# function to ATTACK
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
