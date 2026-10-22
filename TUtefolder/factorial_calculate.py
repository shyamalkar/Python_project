# Task 1: Calculate Factorial Using a Function

def factorial(n):
    # Start with 1 because multiplying by 1 does not change the result
    result = 1

    # Calculate factorial using a loop
    for i in range(1, n + 1):
        result = result * i

    # Return the calculated factorial
    return result


# Take input from the user
number = int(input("Enter a number: "))

# Call the factorial function
result = factorial(number)

# Display the result
print(f"Factorial of {number} is: {result}")