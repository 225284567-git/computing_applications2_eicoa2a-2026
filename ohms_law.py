def calc_resistance(voltage, current):
    
    if current == 0:
        raise ValueError("Current cannot be zero when calculating resistance.")
    return voltage / current
calc_resistance.__doc__= """
    Calculating resistance using Ohm's Law.

    Parameters:
    voltage (float): The voltage in volts.
    current (float): The current in amperes.

    Returns:
    float: The resistance in ohms.
    """