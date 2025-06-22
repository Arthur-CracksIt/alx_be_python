from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    current_date = datetime.now()
    return current_date
def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to current "))
    future_date = datetime.now() + timedelta(days= number_of_days)
    return future_date