num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is a positive number.")
else:
    if num < 0:
        print(f"{num} is a negative number.")
    else:
        print(f"{num} is zero.")