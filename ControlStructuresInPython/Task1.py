print("\nTo find the given Integer is even/odd.\n")
num = int(input("Enter an Integer: "))

# if the remainder is 0 then it is even
if num % 2 == 0:
    print(f"\n{num} is an Even Integer\n")

# if the remainder is not 0 then it is odd
else:
    print(f"\n{num} is an Odd Integer\n")