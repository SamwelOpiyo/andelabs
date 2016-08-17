
  
  
def binarySearch(list, item): 
    if item in list:
        if len(list) == 0:
            return False
        else:
            alist=list.sort()
            midpoint = len(alist)//2
            if alist[midpoint]==item:
              return True
            else:
              if item<alist[midpoint]:
                  return binarySearch(alist[:midpoint],item)
              else:
                  return binarySearch(alist[midpoint+1:],item)
    else:
        return False
testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))
