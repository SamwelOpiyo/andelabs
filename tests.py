def string_length(s):
  if type(s)==str:
    p=[]
    p.append(len(s))
    return p
  elif type(s)==list:
    p=[]
    for i in s:
      counter=0
      while counter<=len(i):
        k=len(i)
        counter=counter+1
      p.append(k)
    return p
  else:
    return False
print string_length("sam")

