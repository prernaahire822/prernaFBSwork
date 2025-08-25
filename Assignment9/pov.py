def sum_of_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_n(n - 1)

num = int(input("Enter a number n: "))
if num < 1:
    print("Input should be a positive integer.")
else:
    print(f"Sum of first {num} natural numbers: {sum_of_n(num)}")
