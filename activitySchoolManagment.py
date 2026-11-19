class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

student1 = Person("Stacey", 14)

print(f"Name: {student1.name}")
print(f"Age: {student1.age}")

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_age(self):
        return self.__age

student1 = Person("Stacey", 14)

print(f"Name: {student1.name}")
print(f"Age: {student1.get_age()}")

#Reflection: It protects the data from direct modification and allows controlled, safe access.
