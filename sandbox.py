class Character:
    alignment = 'Good'
    name = 'Sheeran'

c = Character()

print(c.name, c.alignment)

setattr(c, 'name', 'Chad')
setattr(c, 'alignment', "BADBADNOTGOOD")
print(c.name, c.alignment)


abilities = {
            "Str": 10,
            "Dex": 10,
            "Con": 10,
            "Wis": 10,
            "Int": 10,
            "Cha": 10
}

for i in abilities :
    print(i, abilities[i])