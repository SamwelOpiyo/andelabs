def prime():
    integer = int(raw_input("Enter an Integer:"))
    prime_list = list()
    if integer==2:
        prime_list.append(integer)
    elif integer==3:
        prime_list.append(2)
        prime_list.append(integer)
    else:
        prime_list.append(2)
        prime_list.append(3)
        for k in range(4,integer+1):
                                       
            prime_check(k)
                    
    return prime_list
print prime()

