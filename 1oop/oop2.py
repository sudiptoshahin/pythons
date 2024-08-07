
from datetime import datetime

class Vehicle:
    """class representing general vehicle"""
    def __init__(self, brand: str, model: str) -> None:
        self.brand = brand
        self.model = model

    def move(self):
        print('MOVE!')

class Car(Vehicle):
    """class represents car"""
    pass

class Boat(Vehicle):
    """class represents car"""
    def move(self):
        print("Sail")

class Plane(Vehicle):
    """This is a plane"""
    def move(self):
        print("FLY")


if __name__ == "__main__":
    car1 = Car("Ford", "Mustang")
    boat1 = Boat("Ibize", "Touring 20")
    plane1 = Plane("Boeing", "737")

    for x in (car1, boat1, plane1):
        print(x.brand)
        print(x.model)
        x.move()

    print(f"Current datetime: {datetime.now()}")
    print(f"Custom dates: {datetime(2024, 8, 2)}")