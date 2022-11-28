user_word=input("Enter the word: ")
print(user_word)
count=0
list2=["y","x"]
list=["a","e","i","o","u"]
for i in user_word:
    if i in list or i in list2:
        count+=1
    
print(count)  
if(count>=1):
    
    print("has vowels")
else:
    print("No vowels")