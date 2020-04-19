def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return
      else:
          print(a,"/",b,"=", a/b)
      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    return print(a/b)

if __name__ == '__main__':
    divide(8,2)