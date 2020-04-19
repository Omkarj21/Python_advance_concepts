############################### 1st Way without @ sign
# Original Function which used to divide 2 values
def f_div(m,n):
    return m/n
print("Original Function Result :",f_div(4,8))

# Below Decorator function used to customize Original Function.
def smrt_f_div(func):
    def logic(m, n):
        if m < n:
            m, n = n, m
        return func(m, n)
    return logic # If This is Active then line 14th and line 24th should be comment out and 23rd should be active
    # return logic() # If This is Active then line 13th and line 23rd should be comment out and 24th should be active

# In Below, we are passing Original function "f_div" to new function "smrt_f_div" as a parameter.
# Here "f_div" which is at left side of sign "=" can be anything, like it could be pqr = smrt_f_div(f_div)
# Then you have to call pqr function or functin which is at left side of "=" sign.
f_div = smrt_f_div(f_div)
# In Below, we are calling & printing.
# In Below, when Original function "f_div" gets called then before calling "f_div" function it will
# call new function "smrt_f_div".
print("Decorator Function Result : ",f_div(4,8)) # This is "Call by Function-Value", If This is Active then line 14th and line 24th should be comment out and 13th should be active
# print("Decorator Function Result : ",f_div) # This is "Call by Reference", If This is Active then line 13th and line 23rd should be comment out and 14th should be active
# --------------------------------------------------------------------------------------------
############################### 2nd Way with @ sign
# Below Decorator function used to customize Original Function.
def smrt_f_div(func):
    def logic(m, n):
        if m < n:
            m, n = n, m
        return func(m, n)
    return logic

# In Below, we are setting "@" to new function "smrt_f_div" with Original Function
# Original Function which used to divide 2 values
@smrt_f_div
def f_div(m,n):
    return m/n
# In Below, when Original function "f_div" gets called then before calling "f_div" function it will
# call new function "smrt_f_div".
print(f_div(4,4))
# # --------------------------------------------------------------------------------------------