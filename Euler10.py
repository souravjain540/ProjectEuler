#p_s-08

# Not an optimal solution for 2 million limit
"""
N = 2000000

dig = 2
new_list=[]

while(N > dig):
    for j in range( 2, dig//2 +1 ):
        if dig % j == 0:
            break
    else:
        new_list.append(dig)
    dig += 1
    
print(sum(new_list) )
"""


# This question can be done in 3 parts -
# making a set excluding even numbers
# looping upto only sqrt of 2 million
#  using sum() for sum of list

N = 2000000

numbers = set(range(3, N + 1, 2)) 

for number in range(3, int(N ** 0.5) + 1):
    
    if number not in numbers:
        continue

    num = number
    while num < N:
        num += number
        if num in numbers:
            # Remove multiples of prime found
            numbers.remove(num)

print(2 + sum(numbers))