task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        if time_bound == 'yes':
            print(f"Reminder: {task} is a {priority} priority task that requires immediate attention today!")
        else:
            print(f"{task} is a {priority} priority  but non-time bound")
    case 'medium':
        if time_bound == 'yes':
            print(f"Reminder: {task} is a  {priority} priority task that requires medium attention today!")
        else:
            print(f"{task} is a {priority} priority and non-time bound")
    case 'low':
        if time_bound == 'yes':
            print(f"Note: {task} is a  {priority} priority task. Consider completing it when you have free time.")
        else:
            print(f"{task} is a {priority} priority and non-time bound")
    case _:
        print("Choose a priority")