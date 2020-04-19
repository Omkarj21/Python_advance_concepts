def print_msg(number): # This "print_msg" is enclosing function
    # This is enclosing scope
    # The variables defined here can be accessed in Nested function i.e. in printer()
    def printer(): # This is nested function
        # Here we are using the nonlocal keyword to Edit/Modify value of variable.
        nonlocal number
        number=3
        print(number)
    printer()
    print(number)

print_msg(9)
# output with "nonlocal" keyword = 3 3
# output with NO "nonlocal" keyword = 3 9