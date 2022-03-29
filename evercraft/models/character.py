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

class Character():
    def __init__(self, obj = {"name":"Bob"}):
        if obj:
            self.name = obj["name"]

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name