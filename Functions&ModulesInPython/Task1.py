# Calculate Factorial Using a Function
def factorial(a):
    f=1
    for i in range(a,1,-1):
        f*=i
    return f

num = int(input("\nEnter the number to find it's factorial: "))
print(f"\nThe factorial of {num}! is {factorial(num)}\n")
