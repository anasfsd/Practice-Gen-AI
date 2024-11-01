import streamlit as st

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Streamlit app
st.title("Temperature Converter")

# Select conversion type
conversion_type = st.radio("Choose conversion type:", ("Celsius to Fahrenheit", "Fahrenheit to Celsius"))

# Input temperature based on the selection
if conversion_type == "Celsius to Fahrenheit":
    celsius = st.number_input("Enter temperature in Celsius:", value=0.0)
    if st.button("Convert"):
        fahrenheit = celsius_to_fahrenheit(celsius)
        st.success(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
else:
    fahrenheit = st.number_input("Enter temperature in Fahrenheit:", value=32.0)
    if st.button("Convert"):
        celsius = fahrenheit_to_celsius(fahrenheit)
        st.success(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
