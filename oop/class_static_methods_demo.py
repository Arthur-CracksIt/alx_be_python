class Calculator:
    @staticmethod
    def add(a, b):
        return a + b  
    
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {Attribute.calculation_type}")
        cls.a = a
        cls.b = b
        return cls.a * cls.b
      
class Attribute:
        calculation_type = "Arithmetic Operations"
    
   