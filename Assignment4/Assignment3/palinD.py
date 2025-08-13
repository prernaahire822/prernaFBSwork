num = int(input("Enter a 3-digit number: "))

if num < 100 or num > 999:
    print("Not a 3-digit number.")
else:
    original_num = num
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    if original_num == reversed_num:
        print(f"{original_num} is a palindrome.")
    else:
        print(f"{original_num} is not a palindrome.")

