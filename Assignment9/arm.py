def power(num, p):
    if p == 0:
        return 1
    else:
        return num * power(num, p - 1)

def check_armstrong(n, original, digits):
    if n == 0:
        return 0
    else:
        return power(n % 10, digits) + check_armstrong(n // 10, original, digits)

num = int(input("Enter a number: "))
digits = len(str(num))
if num == check_armstrong(num, num, digits):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
