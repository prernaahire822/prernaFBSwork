n = 5
for i in range(n):
    print(' ' * (n - i - 1), end='')
    num = i + 1
    for j in range(2 * i + 1):
        print(num, end=' ')
        if j < i:
            num += 1
        else:
            num -= 1
    print()

