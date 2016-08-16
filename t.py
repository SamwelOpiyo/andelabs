def find(d):
  p=[]
  for i in d:
    counter=0
    while counter<=len(i):
      k=len(i)
      counter=counter+1
    p.append(k)
  return p
  
def string_length(s):
  if type(s)==list:
    find(s)
  elif type(s)==str:
    new_s=list(s)
    find(new_s)
  else:
    return False  
print string_length("sam")
