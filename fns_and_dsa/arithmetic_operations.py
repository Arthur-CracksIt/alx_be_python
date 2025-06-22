def perform_operation(num1, num2, operation):
    match operation:
        case 'add':
            return num1 + num2
        case 'subtract':
            return num1 - num2
        case 'divide': 
            while num2 == 0:
                print(f"{num2} cannot divide {num1}. Please enter a significant number...")
                num2 = float(input("Reenter second number: "))
            return num1 / num2
        case 'multiply':
            return num1 * num2
        case _:
            return print("Re-run program")
    

