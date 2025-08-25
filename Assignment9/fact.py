def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def sum_of_series(n):
    if n == 1:
        return factorial(n)
    else:
        return sum_of_series(n - 1) + factorial(n)

num = int(input("Enter a number n: "))
if num < 1:
    print("Input should be a positive integer.")
else:
    print(f"Sum of series 1! + 2! + ... + {num}!: {sum_of_series(num)}")
