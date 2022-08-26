"""
a function that get an unlimited numbers and a number, and count his shows.
"""
def count_shows(n1, *nums):
    count = 0
    for x in nums:
        if x == n1:
            count += 1
    return count

print (count_shows(4,1,2,3,4,3,5,2,3))