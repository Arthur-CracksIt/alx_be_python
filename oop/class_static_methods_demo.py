class Calculator:
    @staticmethod
    def add(x, y):
        return x + y
    
    class Attribute:
        calculation_type = "Arithmetic Operations"
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.Attribute.calculation_type}")
        cls.a = a
        cls.b = b
        return cls.a * cls.b