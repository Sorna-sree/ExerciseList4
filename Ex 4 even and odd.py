import random
num1=random.randint(1,100)
num2=random.randint(1,100)
print("The first random number is: ",num1)
print("The second random number is:  ",num2)

if(num1%2==0 and num2%2==0):
    print("All even")
elif(num1%2!=0 and num2%2!=0):
    print("No even")
else:
    print("some even")