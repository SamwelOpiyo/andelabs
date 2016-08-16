    
class PrimeChecker(object): 
  def __init__(self, number = ""):
    self.number = number
    
  def is_prime(self):
        if self.number == "":
          return False
        for i in range(2, int((int(self.number)**0.5) + 1)):
          if int(self.number) % i == 0:
            return False
        return True
    


class PrimeChecker(object): 
  def __init__(self, number = ""):
    self.number = number
    
  def is_prime(self):
    if self.number=="":
      return False
    else:
      new_s=int(self.number)
      return prime_no(new_s)
          
def prime_no(integer):
  if integer%2==0 and integer!=2:
    return False
  elif integer == 1:
    return False
  elif integer == 2: 
    return True
  elif integer == 3: 
    return True
  else:
    x = True 
    for i in range(2, integer):
      if integer%i == 0:
        x = False
        break 
      if x:
        return True
      else:
        return False
    else:
      return False
