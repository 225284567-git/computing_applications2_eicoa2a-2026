from ohms_law import calc_resistance    

voltage = float(input("Enter the voltage in volts: "))  # Example voltage in volts
current = float(input("Enter the current in amperes: "))   # Example current in amperes
result = calc_resistance(voltage, current)
#resistance = calc_resistance(10, 0)
print(f"Documentation for calc_resistance:\n{calc_resistance.__doc__}")
print(f"The calculated resistance is: {result:.2f} ohms")
#print(f"The calculated resistance is: {resistance} ohms")
assert calc_resistance(9,0.3)== 300
assert calc_resistance(24,2)== 12