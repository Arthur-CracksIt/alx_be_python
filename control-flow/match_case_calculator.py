num1 = int(input('Enter first number: '))
num2 = int(input('Enter second number: '))
operator = input("Choose the operation (+, -, *, /): ")

match operator:
    case '+':
        print("The result is:", num1 + num2)
    case '-':
        print("The result is:", num1 - num2)
    case '*':
        print("The result is:", num1 * num2)
    case '/':
        if(num2 == 0):
            print("Cannot divide by zero")

        else:
            print("The result is:", num1 / num2)
    case _:
        print("Enter valid numbers")
    
    
    
    
