def duplicate(list):
    n=len(list)
    for i in range(n):
        if((list.count(list[i]))>1):
            return (list[i]) 
        #assuming there is only one element in the array which has duplicate value 
        
l=eval(input("enter the list of numbers"))
print("the element which is duplicate is",duplicate(l))
