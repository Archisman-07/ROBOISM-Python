s=input("enter the string")
n=len(s)
if (n%2==0):
    x=int((n/2))
else:
    x=int((n-1)/2)
for i in range(x):
    if (s[i]!=s[n-1-i]):
        print("not a palindrome string")
        break
else:
    print("is a palindrome string")