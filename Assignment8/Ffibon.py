def print_fibonacci(n):
    ###Prints Fibonacci series up to n terms###
    a, b = 1, 1
    print(a, b, end=' ')
    for _ in range(2, n):
        next_term = a + b
        print(next_term, end=' ')
        a, b = b, next_term

n = int(input("Enter the number of terms in the Fibonacci series: "))
print_fibonacci(n)

