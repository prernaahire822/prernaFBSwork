n = int(input("Enter a number n: "))

print(f"Even numbers until {n}:")
for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)


