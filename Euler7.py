#p_s-07


# This solution takes 35 seconds
"""

N = int( input( ) )


dig = 2
new_list=[]

while(N != len(new_list) ):
    for j in range( 2, dig//2 +1 ):
        if dig % j == 0:
            break
    else:
        new_list.append(dig)
    dig += 1
    
print(new_list[-1])


"""

# This solution takes 25 seconds

N = int( input( ) )


dig = 2
new_list=[]

while(N != len(new_list) ):
    
        
    
    for j in range( 3, dig//2 +2 ,2):
        if dig % 2 == 0:
            break
        
        elif dig % j == 0:
            break
    else:
        new_list.append(dig)
    dig += 1
    
print(new_list[-1])
