import Closure

call1 = Closure.outerf(10,20,30) # calll will have reference of Nested Function
call1(2,3,4) # Calling of Nested Function
print(call1.__name__) # This will show u the function pointing to i.e will show Nested Function