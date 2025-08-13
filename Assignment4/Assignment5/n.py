amount = int(input("Enter an amount: "))
denominations = [2000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
notes_count = 0

for denomination in denominations:
    notes = amount // denomination
    amount %= denomination
    notes_count += notes
    if notes > 0:
        print(f"{notes} note(s) of Rs. {denomination}")

print(f"Minimum number of notes needed: {notes_count}")
