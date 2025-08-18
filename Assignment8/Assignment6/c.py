n = 4
for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(i + 1):
        result = 1
        for k in range(1, j + 1):
            result = result * (i - k + 1) // k
        print(result, end=' ')
    print()

