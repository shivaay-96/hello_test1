def factorial(n):
    if n==0:
        return
    else:
        return n * factorial(n - 1)
        
number = s
result = factorial(number)
print(f"The factorial of {number} is {result}.")

