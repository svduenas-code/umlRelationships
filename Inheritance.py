class Phone:
    def __init__(self, brand):
        self.brand = brand

    def make_call(self, number):
        print(f"Calling {number} from your {self.brand} phone...")
