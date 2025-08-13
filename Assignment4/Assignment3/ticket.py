ticket_amount = float(input("Enter per person ticket amount: "))

total_amount = 0

for i in range(5):
    age = int(input(f"Enter age of person {i+1}: "))
    
    if age < 12:
        amount = ticket_amount * 0.7  # 30% discount
    elif age > 59:
        amount = ticket_amount * 0.5  # 50% discount
    else:
        amount = ticket_amount  # full amount
    
    total_amount += amount
    print(f"Amount for person {i+1}: {amount}")

print(f"Total amount for all tickets: {total_amount}")

