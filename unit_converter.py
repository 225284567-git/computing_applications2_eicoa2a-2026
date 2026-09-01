millimeters = []
incheces = []

def mm_to_inches(mm):
    """
    Convert millimeters to inches.

    Parameters:
    mm (float): The length in millimeters.

    Returns:
    float: The length in inches.
    """
    return mm / 25.4

def inches_to_mm(inches):
    """
    Convert inches to millimeters.

    Parameters:
    inches (float): The length in inches.

    Returns:
    float: The length in millimeters.
    """
    return inches * 25.4

mm_to_inches.__doc__ = 'Converting millimeters to inches.'
inches_to_mm.__doc__ = 'Converting inches to millimeters.'

print('='*50)
def main():
    while True:
        print("\nUnit Conversion Menu:")
        print('-'*50)
        print("1. Convert millimeters to inches")
        print("2. Convert inches to millimeters")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            mm = float(input("Enter length in millimeters: "))
            inches = mm_to_inches(mm)
            millimeters.append(mm)
            incheces.append(inches)
            print('-'*50)
            print(f"{mm} mm is equal to {inches:.2f} inches.")
        
        elif choice == '2':
            inches = float(input("Enter length in inches: "))
            mm = inches_to_mm(inches)
            incheces.append(inches)
            millimeters.append(mm)
            print('-'*50)
            print(f"{inches} inches is equal to {mm:.2f} mm.")
        
        elif choice == '3':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")
main()
print('='*50)
print("Conversion History:")
if millimeters:
    print("Millimeters to Inches:")
    for mm in millimeters:
        print(f"{mm} mm = {mm_to_inches(mm):.2f} inches")
if incheces:
    print("Inches to Millimeters:")
    for inches in incheces:
        print(f"{inches} inches = {inches_to_mm(inches):.2f} mm")


print(mm_to_inches.__doc__)
print(inches_to_mm.__doc__)