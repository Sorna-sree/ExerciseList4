string="aba1aaba2bab3ababa"
sub_string="aba"

#count the substring values
count=sum(1 for i in range(len(string)) if string.startswith("aba",i))
print("the substring count is: ",count)
