import time


class Auto:
    def __init__(self, brand, age, color=None, mark=None, weight=None):
        self.brand = brand  # Brand of the auto
        self.age = age  # Age of the auto in years
        self.color = color  # Color of the auto
        self.mark = mark  # Mark or model of the auto
        self.weight = weight  # Weight of the auto in kilograms

    def move(self):
        print("move")  # Displaying a message when the auto moves

    def birthday(self):
        self.age += 1  # Incrementing the age of the auto by 1
        print(f"Happy Birthday! {self.brand} is now {self.age} years old.")  # Displaying a auto message

    @staticmethod
    def stop():
        print("stop")  # Displaying a message when the auto stops


class Truck(Auto):
    def __init__(self, brand, age, max_load, color=None, mark=None, weight=None):
        super().__init__(brand, age, color, mark, weight)
        self.max_load = max_load  # Maximum load capacity of the truck

    def move(self):
        print("attention")  # Displaying an attention message before moving
        super().move()

    @staticmethod
    def load():
        time.sleep(1)  # Pause for 1 second
        print("load")  # Displaying a message when loading
        time.sleep(1)  # Pause for 1 second


class Car(Auto):
    def __init__(self, brand, age, max_speed, color=None, mark=None, weight=None):
        super().__init__(brand, age, color, mark, weight)
        self.max_speed = max_speed  # Maximum speed of the car

    def move(self):
        super().move()
        print(f"max speed is {self.max_speed}")  # Displaying the maximum speed of the car


# Example of using the classes
truck_1 = Truck(brand="Volvo", age=5, max_load=5000, color="blue", mark="XC90")
truck_2 = Truck(brand="Mercedes", age=3, max_load=6000, color="white", mark="Actros")

car_1 = Car(brand="Toyota", age=2, max_speed=180, color="red", mark="Camry")
car_2 = Car(brand="BMW", age=1, max_speed=200, color="black", mark="X5")

# Checking methods and attributes
print("Truck 1:")
truck_1.move()
truck_1.birthday()
truck_1.stop()
truck_1.load()

print("\nTruck 2:")
truck_2.move()
truck_2.birthday()
truck_2.stop()
truck_2.load()

print("\nCar 1:")
car_1.move()
car_1.birthday()
car_1.stop()

print("\nCar 2:")
car_2.move()
car_2.birthday()
car_2.stop()
