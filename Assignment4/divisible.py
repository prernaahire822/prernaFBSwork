n = int(input("Enter a number n: "))
i = int(input("Enter a divisor i: "))

print(f"Numbers up to {n} divisible by {i}:")
for num in range(1, n + 1):
    if num % i == 0:
        print(num)


