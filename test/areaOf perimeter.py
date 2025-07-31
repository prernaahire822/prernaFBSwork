import math 

def calculate_area_perimeter():
    length = float(input("Enter the length of the rectangle: "))
    breadth = float(input("Enter the breadth of the rectangle: "))
    radius = breadth / 2  


    # Calculate areas
    area_rectangle = length * breadth
    area_semicircle = (math.pi * (radius ** 2)) / 2
    total_area = area_rectangle + area_semicircle

    # Calculate perimeters
    perimeter_rectangle = 2 * (length + breadth)
    perimeter_semicircle = math.pi * radius
    total_perimeter = perimeter_rectangle - breadth + perimeter_semicircle

    print(f"Total Area: {total_area:.2f}")
    print(f"Total Perimeter: {total_perimeter:.2f}")

# Call the function
calculate_area_perimeter()