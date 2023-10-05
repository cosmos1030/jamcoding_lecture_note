def get_first(x):
    return x[0]

arr = [(1,2), (0,1), (5,1), (5,2), (3,0)]

sorted_arr = sorted(arr, key=lambda x: x[0])
print(sorted_arr)

sorted_arr2 = sorted(arr, key=get_first)
print(sorted_arr2)