# 1. Read Generator values with function "next"

my_list = [5, 3, 9, 10]

# Here, a is Generator Object
a = (x**2 for x in my_list)
# Output: 25
print(next(a))

# Output: 9
print(next(a))

# Output: 81
print(next(a))

# Output: 100
print(next(a))

# Output: StopIteration error, as value of the generator "a" has become NONE
print (next(a))
# ------------------------------------------------------------------------------------------------
# 2. Read Generator values with "For Loop"
# You cannot perform "for item in mygenerator" second time since generators can only be used once.
mygenerator = (x*x for x in range(3)) # mygenerator is generator object
# Below will process value of mygenerator and after end of process it will permanently empty the mygenerator
for item in mygenerator:
    print("Generator Value 1st Time : ",item)

# Here mygenerator is empty as it is already processed above.
# You will not get result for below, as generators can only be used once.
for item in mygenerator:
    print("Generator Value 2nd Time : ",item)
#-----------------------------------------------------------------------------------------------
#