my_list = [1, 2, 3, 4, 5]

# Get an iterator(object) using iter() function of above my_list
# This will transfer control of one index to another
my_iter = iter(my_list)

# Iterate elements using next() function i.e.
print(next(my_iter)) #prints 1
print(next(my_iter)) #prints 2

# "next(obj)" is same as "obj.__next__()"
# next(obj) == obj.__next__()

print(my_iter.__next__()) #prints 3
print(my_iter.__next__()) #prints 4
print(my_iter.__next__()) #prints 5

## This will raise error, no items left
print(next(my_iter))

#----------------------------------------------------------------------------------------------
# Loops implements method iter & next internally.
# These methods are also called as Iterator Protocols.
my_list = [1, 2, 3, 4, 5]
for i in my_list:
    print("Using For-Loop : ", i )
# Result =>
# Using For-Loop :  1
# Using For-Loop :  2
# Using For-Loop :  3
# Using For-Loop :  4
# Using For-Loop :  5