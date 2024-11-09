def linear_search(arr, x, index=0):
    if index >= len(arr):
        return -1
    if arr[index] == x:
        return index
    return linear_search(arr, x, index + 1)

arr = [2, 3, 4, 10, 40]
x = 10
result = linear_search(arr, x)
print(result)
