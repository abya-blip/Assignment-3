
def factorial(a):
  b = 1
  
  if a == 0:
      b = 1
      return b
  elif a == 1:
      return b
  else:
      
      for i in range(1,a+1):
          b = b * i
      
      
      return b



a = int(input("Enter a number: "))

print(factorial(a))
