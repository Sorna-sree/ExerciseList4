user_num=input("Enter the number: ")
divide=int(user_num)/3
print("first divided result: ",divide)
divide_again=int(divide)/3
print("second divided result: ",divide_again)
count=0

while(divide_again>3):
    divide_again=divide_again/3
    count+=1
print("final result: ",divide_again)
print("divide cound: ",count)
