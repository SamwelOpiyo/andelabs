def find_max_min(list_no):
  if min(list_no)!=max(list_no):
    p=[]
    p.append(min(list_no))
    p.append(max(list_no))
    return p
  else:
    p=[]
    p.append(len(list_no))
    return p
