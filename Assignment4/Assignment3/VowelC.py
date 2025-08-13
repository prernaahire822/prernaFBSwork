char = input("Enter an alphabet: ").lower()

if char in 'aeiou':
    print(f"{char} is a vowel.")
else:
    if char.isalpha():
        print(f"{char} is a consonant.")
    else:
        print(f"{char} is not an alphabet.")

