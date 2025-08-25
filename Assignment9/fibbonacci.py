def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

num = int(input("Enter number of terms: "))
if num <= 0:
    print("Input should be a positive integer.")
else:
    print("Fibonacci series:")
    for i in range(num):
        print(fibonacci(i))

