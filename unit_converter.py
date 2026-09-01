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
option = input("if you want to convert from mm to inches '1' if you want to convert from inches to mm '2': ")
if option == '1':
    mm = float(input("Enter length in millimeters: "))
    inches = mm_to_inches(mm)
    millimeters.append(mm)
    incheces.append(inches)
    print(f"{mm} mm is equal to {inches:.2f} inches.")
elif option == '2':
    inches = float(input("Enter length in inches: "))
    mm = inches_to_mm(inches)
    millimeters.append(mm)
    incheces.append(inches)
    print(f"{inches} inches is equal to {mm:.2f} mm.")

print('='*50)



print(mm_to_inches.__doc__)
print(inches_to_mm.__doc__)