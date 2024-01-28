class Calculator:
    def add(self, a, b):
        try:
            result = a + b
        except Exception as e:
            print(f"Error during addition: {e}")
        else:
            return result

    def subtract(self, a, b):
        try:
            result = a - b
        except Exception as e:
            print(f"Error during subtraction: {e}")
        else:
            return result

    def multiply(self, a, b):
        try:
            result = a * b
        except Exception as e:
            print(f"Error during multiplication: {e}")
        else:
            return result

    def divide(self, a, b):
        try:
            result = a / b
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
        except Exception as e:
            print(f"Error during division: {e}")
        else:
            return result

    def power(self, base, exponent):
        try:
            if exponent < 0:
                raise ValueError("Exponent must be a non-negative integer.")
            result = base ** exponent
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Error during exponentiation: {e}")
        else:
            return result

# Example usage:
calculator = Calculator()

print("Addition:", calculator.add(5, 3))
print("Subtraction:", calculator.subtract(7, 2))
print("Multiplication:", calculator.multiply(4, 6))

# Division with error (division by zero)
print("Division:", calculator.divide(8, 0))

# Exponentiation with error (negative exponent)
print("Exponentiation:", calculator.power(2, -3))
