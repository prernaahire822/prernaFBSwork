num = int(input("Enter a number: "))
original_num = num
sum_of_powers = 0
num_digits = 0

# Calculate number of digits
temp_num = num
while temp_num > 0:
    temp_num //= 10
    num_digits += 1

# Calculate sum of powers
while num > 0:
    digit = num % 10
    sum_of_powers += digit ** num_digits
    num //= 10

if sum_of_powers == original_num:
    print(f"{original_num} is an Armstrong number.")
else:
    print(f"{original_num} is not an Armstrong number.")
    