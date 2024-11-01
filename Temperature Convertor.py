
Open In Colab

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Main program
print("Temperature Converter")
print("1. Convert Celsius to Fahrenheit")
print("2. Convert Fahrenheit to Celsius")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == '2':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid choice. Please enter 1 or 2.")

     
Temperature Converter
1. Convert Celsius to Fahrenheit
2. Convert Fahrenheit to Celsius
Enter your choice (1 or 2): 1
Enter temperature in Celsius: 20
20.0°C is equal to 68.0°F


     
