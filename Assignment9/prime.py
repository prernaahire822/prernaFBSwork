def is_prime(n, i=2):
    if n <= 2:
        return True if n == 2 else False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

num = int(input("Enter a number: "))
if is_prime(abs(num)):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

