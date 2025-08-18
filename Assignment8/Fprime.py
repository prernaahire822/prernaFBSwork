def is_prime(num):
    ###Check if a number is prime###
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(n):
    ###Calculates sum of all prime numbers between 1 and n###
    sum_primes = sum(i for i in range(1, n + 1) if is_prime(i))
    return sum_primes

n = int(input("Enter a positive integer n: "))
print(f"Sum of all prime numbers between 1 and {n}: {sum_of_primes(n)}")

