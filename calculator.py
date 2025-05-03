num1 = float(input("Enter the first number: "))

operation = input("Enter your operation:")

# Ask the user to input the second number
num2 = float(input("Enter the second number: "))

# Add the two numbers
sum_result = num1 + num2
# Subtract the second number from the first
difference_result = num1 - num2
# Multiply the two numbers 
product_result = num1 * num2

quotient_result = num1 / num2

modulus_result = num1 % num2

if num1 + num2:
 print(f"Sum: {sum_result}") 
elif num1 - num2:
 print(f"Difference: {difference_result}")  
elif num1 * num2:
 print(f"Product: {product_result}") 
elif num1 / num2:
 print(f"Quotient: {quotient_result}")
elif num1 % num2:
 print(f"Modulus:{modulus_result}")


 
