class Car:
    def __init__(self, model):
        self.model = model

    def drive(self):
        print(f"The {self.model} is zooming down the road!")

class Driver:
    def __init__(self, name):
        self.name = name

    # The association happens here: a car object is passed as a parameter
    def operate_vehicle(self, car):
        print(f"{self.name} gets behind the wheel.")
        car.drive()
