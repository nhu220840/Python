# Duck typing: gan giong nhu overloading, dai khai la neu 1 class co 1 ham trung ten voi nhung class khac thi class y co the 
# duoc coi nhu nhung ham kia (y la o day class Car co the duoc coi nhu Animal)

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:
    alive = False
    # def horn(self):
    #     print("HONK!")

    def speak(self):
        print("HONK!")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()