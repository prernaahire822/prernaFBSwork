def is_armstrong(num):
    ###Checks if a number is an Armstrong number###
    num_str = str(num)
    num_digits = len(num_str)
    return num == sum(int(digit) ** num_digits for digit in num_str)

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")

