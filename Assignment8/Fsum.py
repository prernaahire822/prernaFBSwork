def sum_of_digits(num):
   ###Calculates sum of digits of a number###
    sum_digits = sum(int(digit) for digit in str(abs(num)))
    return sum_digits

num = int(input("Enter a number: "))
print(f"Sum of digits of {num}: {sum_of_digits(num)}")

