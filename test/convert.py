def convert_distance(km):
    meters = km * 1000
    centimeters = km * 100000
    return meters, centimeters
def main():
    # Input distance in kilometers
    km = float(input("Enter distance in kilometers: "))

    # Convert distance
    meters, centimeters = convert_distance(km)

    # Print results
    print(f" kilometers is equal to:{km}")
    print(f"Meters: {meters}")
    print(f" Centimeters: {centimeters}")
main()