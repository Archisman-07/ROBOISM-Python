def is_prime(n):
    if (n==1):
        return False
    for i in range(2,int(n/2)+1):
        if (n%i==0):
            return False 
    else:
        return True
    
n1=int(input("Enter the start of the range"))
n2=int(input("Enter the end of the range"))
for i in range(n1,n2):
    if (is_prime(i)):
        print(i)

