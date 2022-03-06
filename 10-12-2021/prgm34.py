# 34. Program to find the factorial of a given number using user-defined function.

number = int(input("Enter the NUMBER:"))
def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact = fact * i
    return fact
result = factorial(number)
print("fact=", result)
