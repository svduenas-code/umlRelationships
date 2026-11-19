class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

student1 = Person("Stacey", 14)

print(f"Name: {student1.name}")
print(f"Age: {student1.age}")

