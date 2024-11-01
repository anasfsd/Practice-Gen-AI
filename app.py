def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("🌡️ Welcome to the Temperature Converter!")
    while True:
        print("\nChoose a conversion type:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            try:
                celsius = float(input("Enter temperature in Celsius: "))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"✅ {celsius}°C is equal to {fahrenheit:.2f}°F")
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
        
        elif choice == '2':
            try:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                celsius = fahrenheit_to_celsius(fahrenheit)
                print(f"✅ {fahrenheit}°F is equal to {celsius:.2f}°C")
            except ValueError:
                print("❌ Invalid input! Please enter a valid number.")
        
        elif choice == '3':
            print("Thank you for using the Temperature Converter! Goodbye! 👋")
            break

        else:
            print("❌ Invalid choice! Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
