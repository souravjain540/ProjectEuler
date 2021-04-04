
#p_s-02

var_first , var_second = 0 , 1

even_sum = 0
while( var_second < 4000000 ):
    
    var_first ,var_second = var_second , var_first + var_second
    
    if ( var_second % 2 == 0 ):
        even_sum += var_second

print( even_sum )