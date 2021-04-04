pall_list=[]

for i in range(100,1000):
    # for iterating through all three digit nums
    for j in range(100,1000):
        # second digit 
        if(str(i*j)==(str(i*j)[::-1])):
            # checking pallindrome
            pall_list.append(i*j)
print(max(pall_list))