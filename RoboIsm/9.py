s=input("enter the string")
l=[]
result = " "     
for i in s:                           #assuming only lowercase letters in the string
    l.append(ord(i))
l.sort()
for i in range(len(l)):
    result += chr(l[i])
print(result)
    