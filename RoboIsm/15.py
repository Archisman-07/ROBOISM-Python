s=input("enter the string")
count_alpha ,count_digits,count_specialchar=0,0,0
for i in s:
    if(ord(i)>=48 and ord(i)<=57):
        count_digits +=1
    elif((ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90)):
        count_alpha +=1
        
    elif((ord(i)>=32 and ord(i)<=47) or (ord(i)>=52 and ord(i)<=64) or (ord(i)>=123 and ord(i)<=126) or (ord(i)>=91 and ord(i)<=96)):
        count_specialchar += 1
        
print("The number of digits are :",count_digits)
print("The number of alphabets are :",count_alpha)
print("The number of special characters are :",count_specialchar)