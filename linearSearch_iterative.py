def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

arr = [2, 3, 4, 10, 40]
x = 10
result = linear_search(arr, x)
print(result)
