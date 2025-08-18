def factorial(n):
    """Calculates n!"""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def sum_of_natural_numbers(n):
    """Calculates sum of 1 + 2 + 3 + ... + n"""
    sum_n = n * (n + 1) // 2
    return sum_n

def sum_of_factorials(n):
    """Calculates sum of 1! + 2! + 3! + ... + n!"""
    sum_factorials = sum(factorial(i) for i in range(1, n + 1))
    return sum_factorials

def sum_of_powers(n):
    """Calculates sum of 1^1 + 2^2 + 3^3 + ... + n^n"""
    sum_powers = sum(i ** i for i in range(1, n + 1))
    return sum_powers

n = int(input("Enter a positive integer n: "))
print(f"Sum of 1 + 2 + 3 + ... + {n}: {sum_of_natural_numbers(n)}")
print(f"Sum of 1! + 2! + 3! + ... + {n}!: {sum_of_factorials(n)}")
print(f"Sum of 1^1 + 2^2 + 3^3 + ... + {n}^{n}: {sum_of_powers(n)}")
