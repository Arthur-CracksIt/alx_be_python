def safe_divide(numerator, denominator):
    try:
        result = float(numerator) / float(denominator)
        print("The result of the division is", result)  # ALX expects this
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")

