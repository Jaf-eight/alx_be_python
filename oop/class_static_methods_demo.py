
"""
class_static_methods_demo.py

Demonstrates @staticmethod and @classmethod using a simple Calculator class.
"""

class Calculator:
    # Class attribute referenced by the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers.

        Static methods do not use class (cls) or instance (self) state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Return the product of two numbers after printing the calculation type.

        Class methods receive the class as the first argument (cls) and can
        access class-level state like class attributes and other class methods.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b


# Optional: allow running this module directly for a quick demo
if __name__ == "__main__":
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")
