try:
    x = int(input("Enter a number: "))
    print(x)
except ValueError:
    print("Invalid input! Please enter a valid integer.")