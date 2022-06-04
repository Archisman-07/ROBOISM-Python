def calculation(n1,operator,n2):
    result=0
    if (operator=="+"):
        result = n1 + n2
    elif(operator == "-"):
        result  = n1-n2
    elif(operator=="/"):
        result = n1 / n2
    elif(operator == "."):
        result = (n1*n2)
    return result 

num1=int(input("enter the first number"))
operator = input("enter the operator")
num2=int(input("enter the second number"))
print(calculation(num1, operator, num2))

4