class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow..meow")

def animal_sound_in_zoo(animal):
    animal.make_sound()

if __name__ == "__main__":
    dog_instance = Dog()
    cat_instance = Cat()

    print("Dog sound in the zoo: ")
    animal_sound_in_zoo(dog_instance)

    print("Cat sound in the zoo: ")
    animal_sound_in_zoo(cat_instance)