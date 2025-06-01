number = int(input("Enter the size of the pattern: "))
count = number
while count > 0:
    for num in range(number):
        print("*", end="")
    print()
    count -=1
