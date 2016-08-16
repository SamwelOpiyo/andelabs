
def fibon():
    n=int(raw_input("Input an Integer:"))
    a, b = 0, 1
    my=[1]
    for i in range(0,n):
        num = a
	a = b
	b = num + a
	my.append(b)
    return(my)
		
print fibon()
	
	
