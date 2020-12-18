# Lecture Pets, Part A

class Pet:
    def __init__(self,n="Name",a="Age",h="Hunger",p="Playful"):
        self.name = n
        self.age = a
        self.hunger = h
        self.playful = p

    # getters

    def getName(self):
        return self.name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.playful


    # setters

    def setName(self,name):
        self.name = name

    def setAge(self,age):
        self.age = age

    def setHunger(self,hunger):
        self.hunger = hunger

    def setPlayul(self, playful):
        self.playful = playful

class Dog(Pet):

    def __init__(self, name, age, hunger, playful, breed, favorite_toy):
        Pet.__init__(self, name, age, hunger, playful)
        self.breed = breed
        self.favorite_toy = favorite_toy

    def wantsToPlay(self):
        if self.playful == True:
            return ("Dog wants to play with " + self.favorite_toy)
        else:
            return ("Dog doesn't want to play.")

husky = Dog("Snowball", 5, False, True, "Husky", "Stick")

play = husky.wantsToPlay()

print(play)

husky.playful = False

play = husky.wantsToPlay()


pet1 = Pet("Jim", 3, False, True)

print(pet1.getName())
print(pet1.getPlayful())

pet1.setName("Snowball")

print(pet1.getName())
print(pet1.name)

pet1.name = "Jim"

print(pet1.name)

