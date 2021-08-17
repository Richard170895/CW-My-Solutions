def move_zeros(array):
    a = []
    b = []
    for i in array:
        if i == 0:
            b.append(i)
        else:
            a.append(i)
            
    for i in b:
        a.append(i)
        
    return a
