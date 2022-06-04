def credit_number(n):
    l=len(n)
    result = " "
    last_four =" "
    for i in range (-4,0):
        last_four = last_four + n[i]
    for i in range(l-4):
        result = result + "*"
    result = result + last_four    
    return result
n1=input("Enter the credit card number")
result=credit_number(n1)
print (result)
        
        

