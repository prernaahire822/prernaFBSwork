n = int(input("Enter n: "))
sum_series = 0

for i in range(1, n + 1):
    fact = 1
    for j in range(1, i + 1):
        fact *= j
    sum_series += i / fact
print(f"Sum of series: {sum_series:.4f}")
