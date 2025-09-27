set1 = {2,6,1,3,8,5,4,2,6,1,3,8,5,4  }
print (set1)
#numbers in a set cannot be duplicated
#addition of a new element
set1.add(7)
print(set1)
#removing item from set
set1.remove(5)
print(set1)
#discard does not show error
set1.discard(40000)
#pop function
num = set1.pop()
print (num)
#set operations
set2 = {4,6,3,77,88,33}
#union of sets
print (set1|set2)
#Intersection of sets(print same items in both sets)
print (set1&set2)
#Difference of sets
print(set1-set2)
#Membership
print(4 in set1)
print(0 in set1)
print(0 not in set1)