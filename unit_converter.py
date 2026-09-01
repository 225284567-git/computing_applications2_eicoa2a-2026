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
option = input("Choose conversion type (1 for mm to inches, 2 for inches to mm): ")
print('-'*50)
if option == '1':
    mm = float(input("Enter length in millimeters: "))
    result = mm_to_inches(mm)
    millimeters.append(mm)
    print(f"{mm} mm is equal to {result:.2f} inches.")
elif option == '2':
    inches = float(input("Enter length in inches: "))
    result = inches_to_mm(inches)
    incheces.append(inches)
    print(f"{inches} inches is equal to {result:.2f} mm.")

else:
    print("Invalid option selected. Please choose 1 or 2.")

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