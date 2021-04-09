pall_list=[]

def isPallindrome( num ):
    temp = num
    rev = 0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        return True

for i in range(100,1000):
    # for iterating through all three digit nums
    for j in range(100,1000):
        # second digit 
        if(isPallindrome(i*j)):
            # checking pallindrome
            pall_list.append(i*j)

    
print(max(pall_list))






# str(i*j)==(str(i*j)[::-1])