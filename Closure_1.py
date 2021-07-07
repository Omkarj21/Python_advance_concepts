def make_multiplier_of(n): # This "make_multiplier_of" is enclosing function
    # This is enclosing scope
    # The variables defined here can be accessed in Nested function i.e. in multiplier()
    def multiplier(x): # This is Nested Function
        return x * n
    return multiplier # Here returning(Not Call) Nested Function reference

# Multiplier of 3
times3 = make_multiplier_of(3)
print("Name of the Function : ",times3.__name__) # This will show the Name of the Function i.e. "multiplier"

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))