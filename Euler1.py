#p_s-01

num = int( input( ) )

x = 0
for i in range( num ):
    # Loop over num times to find multiples
    # of 3 and 5
    if ( i % 3 == 0 or
            i % 5 == 0):
        x += i

print(x)
