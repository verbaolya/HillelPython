class Car:

    FUEL_TYPES = ['gasoline', 'diesel', 'electricity', 'hybrid']
    COLORS = []
    NUMBER_OF_CARS = 0

    def __init__(self, model, year, fuel_type, color):
        self.model = model
        self.year = year
        self.fuel_type = self.is_valid_fuel_type(fuel_type)
        self.color = color
        self.number = Car.NUMBER_OF_CARS + 1

        # Increase NUMBER_OF_CARS by 1
        Car.NUMBER_OF_CARS += 1

        # Add a unique color to COLORS if it does not already exist
        if color not in Car.COLORS:
            Car.COLORS.append(color)

    @staticmethod
    def is_valid_fuel_type(fuel_type):
        return fuel_type if fuel_type in Car.FUEL_TYPES else Car.FUEL_TYPES[0]

    @property
    def numbers(self):
        return f"{self.number} from {Car.NUMBER_OF_CARS}"

    @classmethod
    def get_used_colors(cls):
        return len(cls.COLORS)

    @classmethod
    def get_number_of_cars(cls):
        return cls.NUMBER_OF_CARS


# Example usage:
car_1 = Car('Zaz', 1979, 'diesel', 'black')
car_2 = Car('BMW', 2000, 'gasoline', 'red')
car_3 = Car('VOLVO', 2012, 'electricity', 'black')
car_4 = Car('Mercedes', 2012, 'hybrid', 'black')

print('COLORS:', Car.get_used_colors())  # -> 'COLORS: 2'
print('NUMBER_OF_CARS:', Car.get_number_of_cars())  # -> 'NUMBER_OF_CARS: 4'

for item in (car_1, car_2, car_3, car_4):
    print('item:', item)
    print('numbers:', item.numbers)
    