num_students = int(input("Enter number of students: "))

percentages = []

for i in range(num_students):
    print(f"\nEnter marks for student {i+1}:")
    marks = [float(input(f"Subject {j+1}: ")) for j in range(5)]
    percentage = (sum(marks) / 500) * 100
    percentages.append(percentage)
    print(f"Percentage of student {i+1}: {percentage:}%")

average_percentage = sum(percentages) / num_students
print(f"\nAverage percentage of all students: {average_percentage:}%")

