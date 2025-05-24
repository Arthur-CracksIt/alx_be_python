income = int(input("Enter your monthly income: "))
expenses = int(input("Enter your monthly expenses: "))
monthly_savings = income - expenses
interest = 0.05
print("Your monthly savings are $",monthly_savings)
print("Projected Savings after one year, with interest, is $",monthly_savings * 12 + (monthly_savings * 12 * interest))
