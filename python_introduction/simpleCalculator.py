operators = {
    '+': lambda numbers: sum(numbers),
    '-': lambda numbers: numbers[0] - sum(numbers[1:]),
    '*': lambda numbers: eval('*'.join(map(str, numbers))),
    '/': lambda numbers: numbers[0] / eval('/'.join(map(str, numbers[1:]))) if len(numbers) > 1 else numbers[0],
    '%': lambda numbers: numbers[0] % eval('%'.join(map(str, numbers[1:]))) if len(numbers) > 1 else numbers[0],
    '**': lambda numbers: numbers[0] ** eval('**'.join(map(str, numbers[1:]))) if len(numbers) > 1 else numbers[0],
    '//': lambda numbers: numbers[0] // eval('//'.join(map(str, numbers[1:]))) if len(numbers) > 1 else numbers[0]
}
def calculate(operator, *args):
    if operator not in operators:
        raise ValueError("Invalid operator")
    return operators[operator](args)
# Example usage:
operator = input('Enter an operator (+, -, *, /, %, **, //): ')
try:
    numbers = list(map(float, input('Enter numbers separated by spaces: ').split()))
    result = calculate(operator, *numbers)
    print(f'The result is: {result}')   
except ValueError as e:
    print(f'Error: {e}')
except ZeroDivisionError:
    print('Error: Division by zero is not allowed.')
except Exception as e:
    print(f'An unexpected error occurred: {e}')

