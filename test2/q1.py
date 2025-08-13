n = int(input("Enter how many prime numbers to print: "))
count = 0
num = 2

print(f"First {n} prime numbers:")
while count < n:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=" ")
        count += 1
    num += 1
