class Pet:
    def __init__(self, name, animal, age):
        self.name = name
        self.animal = animal
        self.age = age
    def show(self):
        print("Name:", self.name)
        print("Animal:", self.animal)
        print("Age:", self.age)
pet1 = Pet("Bruno", "Dog", 3)
pet1.show()