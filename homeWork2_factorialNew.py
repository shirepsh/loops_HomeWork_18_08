"""
a function that return a fsctorial due to the num that given to her
"""
def return_factorial_num (num):  #using a for loop
   
    res = num
    for x in range (1, num):
        res *= x
    return res

print (return_factorial_num(3))    