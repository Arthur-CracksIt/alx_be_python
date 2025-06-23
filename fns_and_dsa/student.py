class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def displayStudentInfo(self):
        full_details = f"Your name is {self.name} and you are {self.age} years old"
        return full_details

first_student = Student("David", 15)
print(first_student.displayStudentInfo())

class ProductCatalog:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    def calculateCost(self):
        while True:
            if self.price > 0:
                cost = self.price * self.quantity
            return cost

first_product = ProductCatalog('Mangoes', 10.00, 5)
print(first_product.calculateCost())