# Define a Pet 
class Pet:
    # Define a class variable all that stores all instances of the Pet class.
    all =[]

    # Define a class variable
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    # pass into the constructor its name, pet_type and an optional owner
    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.owner = owner
        # validate that the pet_type is one of those types in the __init__ method
        if pet_type in Pet.PET_TYPES:
            self.pet_type = pet_type
            Pet.all.append(self)
        else:
            raise ValueError("Invalid pet type")
    
    def __str__(self):
        return f"Name: {self.name} | Pet Type: {self.pet_type} | Owner: {self.owner}"
    


# Define an Owner class
class Owner:

    # pass into the constructor a name argument
    def __init__ (self, name):
        self.name = name

    # In the Owner class write a method called pets(self) that returns a full list of the owner's pets
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    # write a method called add_pet(self, pet) that checks that the the pet is of type Pet and adds the owner to the pet
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise ValueError("Invalid pet")

    # In the Owner class write a method called sort_pets_by_name(self) returns a sorted list of pets by their names.
    def get_sorted_pets(self):
        sorted_pets = sorted(self.pets(), key=lambda pet: pet.name)
        return sorted_pets
        



# pet1 = Pet('Simon', 'cat', 'Rhiannon')
# pet2 = Pet('Puff', 'dog', 'Joe')
# print(pet1)
# print(pet2)
# print(Pet.all)
# print(len(Pet.all))

# owner1 = Owner('Jill')
# print(owner1.name)
# print(owner1.pets())
