def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9

def main():
    fahrenheit = input("Please enter the temperature in Fahrenheit: ")
    
    try:
        fahrenheit = float(fahrenheit)
        celsius = fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit:.2f} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")
    finally:
        print("Thank you for using the weather forecast application!")

if __name__ == "__main__":
    main()
#Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.
#Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to
#Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9. 
#Task 3: User Experience Implement an else block that prints the converted temperature in a user-friendly format. 
#Task 4: Finally Add a finally block that thanks the user for using the weather forecast application, ensuring that this 
#message is displayed regardless of whether an exception was caught or not.