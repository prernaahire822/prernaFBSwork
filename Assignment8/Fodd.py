def sum_of_odd_numbers(n):
    sum_odd = sum(i for i in range(1, n + 1) if i % 2 != 0)
    return sum_odd

n = int(input("Enter a positive integer n: "))
print(f"Sum of all odd numbers between 1 and {n}: {sum_of_odd_numbers(n)}")

