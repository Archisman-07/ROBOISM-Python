s=input("enter the string")
sum=0
for i in s:
    if (ord(i)>=48 and ord(i)<=57):
        sum += int(i)
print(sum)
        
