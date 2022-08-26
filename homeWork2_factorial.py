"""
a function that make a factorial for a number that the user choose
"""
def return_the_factorial ():  #using a for loop
   
    num = int(input("enetr a num you want to make factorial for him:"))
    res = num

    for x in range (1,num):
        res *= x
    return res

print (return_the_factorial())
    
