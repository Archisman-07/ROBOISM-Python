def highest_frequency(list):
    l1=[]
    
    for i in list:
        l1.append(list.count(i))
    maximum=max(l1)
    if(maximum==1):
        print("all elements are present only once!")
    else:
        for i in range(len(l1)):
            if (l1[i]==maximum):
                print("the element having the highest frequency in the list is :",list[i])
                break
                       
l=eval(input("enter the list of elements")) 
highest_frequency(l)

    
     


