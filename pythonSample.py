print("This is my python printing")
print("fabulous")
print("print python")

# using a recurisve approach
numTerms = int(input("How many terms of Fibonacci sequence to print? "))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))

if numTerms <= 0:
    print(f"Please enter a positive number")
else:
    print(f"Fibonacci serie:")
    for i in range(numTerms):
        print(fibonacci(i))