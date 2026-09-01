from ohms_law import calc_resistance    

voltage = float(input("Enter the voltage in volts: "))  # Example voltage in volts
current = float(input("Enter the current in amperes: "))   # Example current in amperes
result = calc_resistance(voltage, current)
print(f"Documentation for calc_resistance:\n{calc_resistance.__doc__}")
print(f"The calculated resistance is: {result} ohms")
