#p_s-06

sum1=0
sum2=0

for i in range(1,101):
    sum1+=i
    sum2+= i**2
    
print( ( sum1**2 ) - sum2 )