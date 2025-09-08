def min_notes(amount):
    D = [2000, 500, 200, 100, 50, 20, 10, 5]
    notes = 0
    for denomination in D:
        if amount >= denomination:
            count = amount // denomination
            notes += count
            amount %= denomination
            print(f"Denomination: {denomination}, Count: {count}")
    if amount > 0:
        print(f"Amount {amount} cannot be paid with available denominations.")
    else:
        print(f"Minimum number of notes required: {notes}")

amount = int(input("Enter the amount: "))
min_notes(amount)

