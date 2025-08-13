n = int(input("Enter number of employees: "))

total_all_employees = 0

for i in range(n):
    basic_salary =float(input(f"Enter basic salary of employee {i+1}: "))
    
    if basic_salary < 20000:
        da = basic_salary * 0.10
        ta = basic_salary * 0.12
        hra = basic_salary * 0.15
    else:
        da = basic_salary * 0.15
        ta = basic_salary * 0.18
        hra = basic_salary * 0.20
    
    total_salary = basic_salary + da + ta + hra
    total_all_employees += total_salary
    
    print(f"Total salary of employee {i+1}: {total_salary:}")

print(f"Total salary of all employees: {total_all_employees:}")

