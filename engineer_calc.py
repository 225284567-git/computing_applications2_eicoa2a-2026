from ohms_law import  calc_resistance
from unit_converter import mm_to_inches, inches_to_mm
millimeters = []
incheces = []
default_current = 0.5
def show_default():
    print(f"The default current value is: {default_current} amperes.")
def main():
    while True:
        print("\nEngineering Calculator Menu:")
        print('-'*50)
        print("1. Convert millimeters to inches")
        print("2. Convert inches to millimeters")
        print("3. Calculate resistance using Ohm's Law")
        print("4. Exit")
        
        choice = input("Enter your choice (1/2/3/4): ")
        
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
            millimeters.append(mm)
            incheces.append(inches)
            print('-'*50)
            print(f"{inches} inches is equal to {mm:.2f} mm.")
        
        elif choice == '3':
            voltage = float(input("Enter voltage in volts: "))
            current_input =float(input("Enter current in amperes (or press Enter to use default value): "))
            if current_input == "":
                current_input = float(default_current)
                print(f"Using default current value: {current_input} amperes.")
            try:
                resistance = calc_resistance(voltage, current_input)
                print('-'*50)
                print(f"Resistance is {resistance:.2f} ohms.")
            except ValueError:
                print(f"Error: Current cannot be zero.")
        
        elif choice == '4':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please try again.")



print(calc_resistance.__doc__)
print(mm_to_inches.__doc__)
print(inches_to_mm.__doc__)
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
main()
show_default()
print('='*50)
if millimeters:
    print("Millimeters to Inches:")
    for mm in millimeters:
        print('-'*50)
        print(f"{mm} mm = {mm_to_inches(mm):.2f} inches")
if incheces:
    print("Inches to Millimeters:")
    for inches in incheces:
        print('-'*50)
        print(f"{inches} inches = {inches_to_mm(inches):.2f} mm")
print('='*50)
print("Thank you for using the Engineering Calculator. Goodbye!")
print('='*50)
print("This program was developed by FESHY.")