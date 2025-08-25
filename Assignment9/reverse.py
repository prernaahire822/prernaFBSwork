def reverse_number(n):
    if n < 10:
        return n
    else:
        return int(str(n % 10) + str(reverse_number(n // 10)))

num = int(input("Enter a number: "))
print(f"Reverse of {num}: {reverse_number(num)}")


