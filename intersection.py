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
#while all of the pointers are not at the end:
    # if all three pointers have the same number, store it
    # if not:
        #find the pointer that has the smallest num
        #move that pointer along by one
    
def intersection(lst1, lst2, lst3):
    i, j, k = 0, 0, 0
    intersection = []

    while i <len(lst1) and j < len(lst2) and k < len(lst3):
        if lst1[i] == lst2[j] == lst3[k]:
            intersection.append(lst1[i])
            i += 1
            j += 1
            k += 1
        else:
            smallest = min(lst1[i], lst2[j], lst3[k])
            if smallest == lst1[i]:
                i+= 1
            elif smallest == lst2[j]:
                j+=1
            else:
                k+=1
    return intersection

print(intersection([1, 2, 3, 4, 5], [2, 4, 5, 6, 8], [3, 4, 5]))