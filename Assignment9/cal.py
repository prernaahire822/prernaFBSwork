def calculate_power(m, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / calculate_power(m, -n)
    else:
        return m * calculate_power(m, n - 1)

m = float(input("Enter base (m): "))
n = int(input("Enter exponent (n): "))
print(f"{m} to the power {n}: {calculate_power(m, n)}")

