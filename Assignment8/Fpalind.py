
def is_palindrome(num):
    ###Checks if a number is a palindrome###

    return str(abs(num)) == str(abs(num))[::-1]

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")

