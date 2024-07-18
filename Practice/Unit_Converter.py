def convert_length(value, from_unit, to_unit):
    length_units = {'meters': 1, 'kilometers': 0.001, 'centimeters': 100, 'millimeters': 1000, 'miles': 0.000621371,
                    'yards': 1.09361, 'feet': 3.28084, 'inches': 39.3701}

    if from_unit in length_units and to_unit in length_units:
        return value * (length_units[to_unit] / length_units[from_unit])

    else:
        return "Invalid length units."


def convert_weight(value, from_unit, to_unit):
    weight_units = {'kilograms': 1, 'grams': 1000, 'milligrams': 1000000, 'pounds': 2.20462, 'ounces': 35.274}

    if from_unit in weight_units and to_unit in weight_units:
        return value * (weight_units[to_unit] / weight_units[from_unit])

    else:
        return "Invalid weight units."


def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32

    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9

    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15

    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15

    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5/9 + 273.15

    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9/5 + 32

    else:
        return "Invalid temperature units."


def unit_converter():
    print("Unit Converter")
    print("Options: length, weight, temperature")
    conversion_type = input("Choose a conversion type: ").strip().lower()

    if conversion_type == 'length':
        print("Enter Full Name for each unit")
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from: ").strip().lower()
        to_unit = input("Enter the unit to convert to: ").strip().lower()
        result = convert_length(value, from_unit, to_unit)

    elif conversion_type == 'weight':
        print("Enter Full Name for each unit")
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from: ").strip().lower()
        to_unit = input("Enter the unit to convert to: ").strip().lower()
        result = convert_weight(value, from_unit, to_unit)

    elif conversion_type == 'temperature':
        print("Enter Full Name for each unit")
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from: ").strip().lower()
        to_unit = input("Enter the unit to convert to: ").strip().lower()
        result = convert_temperature(value, from_unit, to_unit)
    else:
        result = "Invalid conversion type."

    print(f"Converted value: {result}")


unit_converter()

# This program converts units of length, weight, and temperature.
# It allows the user to choose a type of conversion and input values accordingly.
# The program includes functions to handle each type of conversion and provides the converted result.
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
