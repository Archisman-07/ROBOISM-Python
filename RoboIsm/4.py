def string_double(s):
    n=len(s)
    result=" "
    for i in range(n):
        result  =result + (s[i]*2)
    return result

s1=input("enter the string")
print(string_double(s1))

