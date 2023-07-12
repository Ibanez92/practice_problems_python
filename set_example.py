set1 = {1, 2, 3}
set2 = {2, 3, 4}

union_set = set1 | set2  # using the | operator
print(union_set)
intersection_set = set1 & set2  # using the & operator
print(intersection_set)
# This line creates a new set called difference_set by performing the set difference operation between set1 and set2. 
# The - operator is used to find the elements that are present in set1 but not in set2. 
# In other words, it creates a set containing the elements that are unique to set1.
difference_set = set1 - set2  # using the - operator
print(difference_set)