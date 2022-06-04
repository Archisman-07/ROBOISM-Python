def my_function(l,s):
    if(s=="asc"):
        l.sort()
    elif(s=="desc"):
        l.sort(reverse=True)
    elif(s=="none"):
        l=l
    return(l)

l=eval(input("enter the list of numbers"))
s="asc"
a=my_function(l,s)
print(a)
