n = 5
for i in range(n):
    print(' ' * (n - i - 1), end='')
    if i == n-1:
        for j in range(1, i+2):
            print(j, end='  ')
        print()
    else:
        print(1, end='')
        if i > 0:
            print(' ' * (2*i-1), end='   ')
            print(i+1)
        else:
            print()
