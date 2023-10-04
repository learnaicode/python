# Step 1: Define a function for addition
def add(x, y):
    return x + y

# Step 2: Define a function for subtraction
def subtract(x, y):
    return x - y

# Step 3: Define a function for multiplication
def multiply(x, y):
    return x * y

# Step 4: Define a function for division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Step 5: Create a menu for the calculator
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

# Step 6: Get user input for operation choice
choice = input("Enter choice (1/2/3/4): ")

# Step 7: Get user input for numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Step 8: Perform the selected operation and display the result
if choice == '1':
    result = add(num1, num2)
    print("Result: ", result)
elif choice == '2':
    result = subtract(num1, num2)
    print("Result: ", result)
elif choice == '3':
    result = multiply(num1, num2)
    print("Result: ", result)
elif choice == '4':
    result = divide(num1, num2)
    print("Result: ", result)
else:
    print("Invalid input")
