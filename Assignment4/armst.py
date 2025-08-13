n = int(input("Enter a number: "))

num_digits = len(str(n))  # number of digits in n
temp_num = n
total = 0

while temp_num > 0:
    digit = temp_num % 10  # get last digit
    total += digit ** num_digits  # add digit^num_digits to total
    temp_num //= 10  # remove last digit

if n == total:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")

