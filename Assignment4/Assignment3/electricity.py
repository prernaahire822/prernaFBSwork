units=110

total_bill=0

if(units>0):
    if(units>50):
        if(units>150):
            pass
        else:
            total_bill=50*0.5
            unit2=units-50
            total_bill=total_bill+(unit2*0.75)
    else:
        total_bill=units=0.5
else:
    print("Invalid input")
    #Add 20% of bill in total bill
    print(total_bill)
