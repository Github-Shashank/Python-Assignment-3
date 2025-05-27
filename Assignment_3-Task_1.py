#  Calculate Factorial Using a Function

num_1 = int(input("Enter a number: "))

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

value = factorial(num_1)
print(f"Factorial of {num_1} is: {value}")
