class Auto:
    def __init__(self, brand, age, color=None, mark=None, weight=None):
        self.brand = brand
        self.age = age
        self.color = color
        self.mark = mark
        self.weight = weight

    @staticmethod
    def move():
        print("move")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday! {self.brand} is now {self.age} years old.")

    @staticmethod
    def stop():
        print("stop")


# Example of using the Auto class
car = Auto(brand="Toyota", age=3, color="blue", mark="Camry")
car.move()
car.birthday()
car.stop()

car2 = Auto(brand="Audi", age=4, mark="Q5")
car2.move()
car2.birthday()
car2.stop()

car.birthday()
