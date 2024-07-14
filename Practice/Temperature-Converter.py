def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67


def temperature_converter():
    temperature = float(input("Enter temperature: "))
    unit = input("Enter unit (C/F/K): ").upper()

    if unit == 'C':
        celsius = temperature
        fahrenheit = celsius_to_fahrenheit(celsius)
        kelvin = celsius_to_kelvin(celsius)
    elif unit == 'F':
        fahrenheit = temperature
        celsius = fahrenheit_to_celsius(fahrenheit)
        kelvin = fahrenheit_to_kelvin(fahrenheit)
    elif unit == 'K':
        kelvin = temperature
        celsius = kelvin_to_celsius(kelvin)
        fahrenheit = kelvin_to_fahrenheit(kelvin)
    else:
        print("Invalid unit entered.")
        return

    print(f"{temperature} {unit} is:")
    print(f"In Celsius: {celsius} C")
    print(f"In Fahrenheit: {fahrenheit} F")
    print(f"In Kelvin: {kelvin} K")


temperature_converter()

# This is a temperature converter that converts temperatures between Celsius, Fahrenheit, and Kelvin
# If you have any specific questions or need more detailed explanations, feel free to ask!
# on my LinkedIn- https://www.linkedin.com/in/sarthak-bansal-6744a2256/
# It will help both of us to grow and learn more stuff in python

# Thank You for reading my notes. It means a lot!
