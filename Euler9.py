# p_s-09

# First approach ( slow approach )
"""
for i in range(1,501):
    for j in range(1,501):
        for k in range(1,501):
            if( i**2 + j**2 == k**2):
                if(i + j + k == 1000 ):
                    print( i*j*k )
                    
"""
 # Second approach ( very fast , few seconds only)
 
 # only 2 loops needed as a+b+c = 1000
 
 # one loop for a second for b
 
 # third not needed as c = 1000-a-b
 
 
for i in range(1, 501):
    for j in range( 1, 501):
         k = 1000-i-j
         if (i**2 + j**2 == k**2 ):
             print( i*j*k )
