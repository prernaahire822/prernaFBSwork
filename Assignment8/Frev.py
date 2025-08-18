def reverse_number(num):
    ###calculates a reverse number###
    reverse = int(str(abs(num))[::-1])
    if num < 0:
        return -reverse
    return reverse

num = int(input("Enter a number: "))
print(f"Reverse of {num}: {reverse_number(num)}")

