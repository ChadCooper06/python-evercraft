class Character:
    alignment = 'Good'
    name = 'Sheeran'

c = Character()

print(c.name, c.alignment)

setattr(c, 'name', 'Chad')
setattr(c, 'alignment', "BADBADNOTGOOD")
print(c.name, c.alignment)
