side1 = int(input("Enter first side: "))
side2 = int(input("Enter second side: "))
side3 = int(input("Enter third side: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
    print("The triangle is valid.")
else:
    print("The triangle is not valid.")

