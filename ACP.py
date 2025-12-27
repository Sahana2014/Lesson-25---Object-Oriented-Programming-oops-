class Dog:
    species = "pup"  # Class Attribute

    def __init__(self, name, breed):
        self.name = name  # Instance Attribute
        self.breed = breed  # Instance Attribute
        
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Fluffy", "Pomeranian")

print("Buddy is a {} " .format(dog1.species))
print("Fluffy is also a {}" .format(dog2.species))

print("{} is a {}" .format(dog1.name, dog1.breed))
print("{} is a {}" .format(dog2.name, dog2.breed))