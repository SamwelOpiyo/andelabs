def find_missing(a,b):
    if len([c for c in b if c not in a])>0:
        p=[c for c in b if c not in a]
        return p[0]
    else:
        return 0
print find_missing([1, 2], [1, 2, 5])
print find_missing([1],[1,2])
