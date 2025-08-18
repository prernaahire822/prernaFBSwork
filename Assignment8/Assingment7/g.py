n = 5
for i in range(n):
    print(' ' * (n - i - 1), end='')
    for j in range(2 * i + 1):
        if j <= i:
            print(j + 1, end=' ')
        else:
            print(2 * i - j + 1, end=' ')
    print()


