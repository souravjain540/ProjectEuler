# p_s-05




def divisible(number):
    for i in range( 1, 21 ):
        if number % i == 0:
            return False
    return True

number = 1

while True:
    if divisible(number):
        break
    number += 1

print(number)
    