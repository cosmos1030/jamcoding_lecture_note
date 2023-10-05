def cantor(l, start, end):
    length = (end-start+1)
    new_st = start+(end-start+1)//3
    new_end = new_st+length//3-1
    l[new_st: new_end+1] = [" "]*(length//3)
    # print(l)
    if new_st>=new_end:
        return l
    cantor(l, start, new_st-1)
    cantor(l, new_end+1, end)
    return l

while 1:
    try:
        n = int(input())
        length = 3**n
        l = ['-']*length
        result = cantor(l, 0, length-1)
        for i in result:
            print(i, end="")
        print("")
    except:
        break