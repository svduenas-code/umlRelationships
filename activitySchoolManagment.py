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

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def get_age(self):
        return self.__age 

class Student(Person):
    def study(self):
         print(f"{self.name} is studying")

student1 = Student("Lina", 20)

print(f"Name: {student1.name}")
print(f"Age: {student1.get_age()} (note this age is privately accessed)")
student1.study()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age # Private attribute

    def get_age(self):
        return self.__age

class Teacher(Person):
    def teach(self):
        print(f"{self.name} is teaching")

teacher1 = Teacher("Mona", 30)

print(f"Name: {teacher1.name}")
print(f"Age: {teacher1.get_age()}")
teacher1.teach()