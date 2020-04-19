# A simple generator function, a function which contains 1 or more yield it becomes generator
def my_gen(n,m):

    print('First Yield')
    # Generator function contains yield statements
    # This will save the n & m value and will to next loop.
    yield n,m # (1, 2)

    n += 3
    m += 2
    print('Second Yield')
    yield n + m # n is 4 & m is 4, So output will be 8

    # print('Checking of Yield or Return')
    # return print(n//m) # If this line is Active(uncomment) then below code will not work because of return
    # yield n * m * 5 # If this line is Active(uncomment) then below code will work

    # Below code will not work if line #15 is Active but will work if #16 line is Active
    n += 1
    m += 4
    print('Third Yield')
    yield n * m # n is 5 & m is 8, So output will be 40

# Iterate function "my_gen" Using for loop.
for _ in my_gen(1,2):
    print("With For Loop :",_)

# Iterate function "my_gen" Using List comprehension
[print("With List comprehension :",item) for item in my_gen(1,2)]

# Iterate function "my_gen" Using "next" function
a = my_gen(5,7) # Here a is iterator object
print(next(a)) # Output : (5, 7)
print(next(a)) # Output : 17
print(next(a)) # Output : 117
print(next(a)) # Output : Error


#------------------------------------------------------------------------------------------------