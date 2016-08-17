    

def factorial(number):
  if number == 0 or number == 1:
    return number
  else:
    k = number * factorial(number-1)
  return k  

