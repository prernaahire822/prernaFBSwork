num_passengers = int(input("Enter number of passengers: "))
ticket_cost = int(input("Enter per ticket cost: "))

total_amount = 0

for i in range(num_passengers):
    age = int(input(f"Enter age of passenger {i+1}: "))
    
    if age < 12:
        amount = ticket_cost * 0.7  # 30% discount
    elif age > 59:
        amount = ticket_cost * 0.5  # 50% discount
    else:
        amount = ticket_cost  # full amount
    
    total_amount += amount
    print(f"Amount for passenger {i+1}: {amount}")

print(f"Total amount for all tickets: {total_amount}")

