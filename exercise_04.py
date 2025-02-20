# Your Name
# ITELEC2
# Laboratory #03 – Guided Coding Exercise:
# Using Python's Math Module for Common Mathematical Operations

# Import the math module
import math

# Calculate the square root of a number
number = 16 
sqrt_result = math.sqrt(number)

# Get the value of pi
pi_value = math.pi

# Calculate the sine of an angle (convert degrees to radians first)
angle_degrees = 30 
angle_radians = math.radians(angle_degrees) 
sin_result = math.sin(angle_radians)

# Calculate the cosine and tangent of angles
angle_radians_60 = math.radians(60)
cos_result = math.cos(angle_radians_60)
angle_radians_45 = math.radians(45) 
tan_result = math.tan(angle_radians_45)

# Calculate the exponential and logarithms
exp_result = math.exp(2)  # Exponential of 2 
log_result = math.log(10)  # Natural log (base e) of 10 
log10_result = math.log(100, 10)  # Logarithm base 10 of 100

# Display the results
print(f"Square root of {number} is: {sqrt_result:.2f}")
print(f"Value of pi is: {pi_value:.15f}")  # Ensure full precision of pi
print(f"Sine of 30 degrees (in radians) is: {sin_result:.15f}")
print(f"Cosine of 60 degrees (in radians) is: {cos_result:.15f}")
print(f"Tangent of 45 degrees (in radians) is: {tan_result:.15f}")
print(f"Exponential of 2 is: {exp_result:.15f}")
print(f"Logarithm (base e) of 10 is: {log_result:.15f}")
print(f"Logarithm (base 10) of 100 is: {log10_result:.1f}") # Expected to be exactly 2.0
