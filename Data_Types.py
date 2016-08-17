def data_type(item):
  if type(item).__name__ == "str":
    return len(item)
  elif type(item).__name__ == "bool":
    return item
  elif type(item).__name__ == "int":
    if item < 100:
      output = "less than 100"
      return output
    elif item > 100:
      output = "more than 100"
      return output
    else:
      output = "equal to 100"
      return output
  elif type(item).__name__ == "list":
    if len(item) > 2:
      return item[2]
    else:
      return None
  elif item == None:
    output = "no value"
    return output
  else:
    output = "Input out of range of check"
    return output
print data_type(3)
