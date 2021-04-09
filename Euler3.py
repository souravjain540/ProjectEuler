
# p_s-03

# This solution is taking very much time for a big number
'''
N = 600851475143

add_final = []

for i in range(1,N):
    # loop to iterate till N
    if N % i == 0:
        # to find factors of N
        add_final.append(i)
new_list=[]

for dig in add_final:
    for j in range( 2,dig ):
        if dig % j == 0:
            break
    else:
        new_list.append(dig)
    
print(max(new_list))      

'''   
        
# Next try

# In this i will take the concept of sqr root



N = 600851475143

add_final = []

for i in range( 1, int( N**0.5) + 1 ):
    
    # Square root because factors start only after the
    # sqrt of the num and we can find the other
    # factor just by dividing that dig
    # by this method we don't have to iterate millions of num
    if N % i == 0:
        # to find factors of N
        add_final.append(i)
        add_final.append( N // i)

new_list=[]

for dig in add_final:
    for j in range( 2,dig ):
        if dig % j == 0:
            break
    else:
        new_list.append(dig)
    
print(max(new_list))   
        

