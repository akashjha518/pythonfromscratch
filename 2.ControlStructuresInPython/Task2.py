print("\nTo find the sum of first 'n' +ve integer.\n")
num = int(input("Enter an positive Integer: ")) #Taking input from the user
sum=0
count=0
# sum of 1 to n integers
for i in range(1,num+1):
    sum +=i
    count+=1


print(f"\nThe sum of first {count} integer is {sum}.\n")
