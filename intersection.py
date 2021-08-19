'''
Given 3 sorted lists, find the intersection of those 3 lists.

ex. intersection([1, 2, 3, 4], [2, 4, 6, 8], [3, 4, 5])
    >>> [4]
'''

###brute force###
#intersection = common num
#go through each list
#count the number of occurrance of each num
    #return the num that occurred 3 times

# def intersection(lst1, lst2, lst3):
#     occurrance = {}

#     for num in lst1:
#         occurrance[num] = occurrance.get(num, 0) + 1

#     for num in lst2:
#         occurrance[num] = occurrance.get(num, 0) + 1

#     for num in lst3:
#         occurrance[num] = occurrance.get(num, 0) + 1

#     return [key for key, value in occurrance.items() if value == 3]

###three pointers###
# have three separate pointers starting at beg of each list
# 

print(intersection([1, 2, 5, 4], [2, 4, 5, 8], [3, 0, 5]))