
def binarsearch(arr, key):
    low = 0
    high = len(arr) - 1

    while low <= high :
        mid = (low + high)//2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1

    return -1            

     # Add input and call the function 

arr = [5, 10, 15, 20, 25, 30]
key = 25

result = binarsearch(arr, key)

if result != -1:
    print(f"key {key} found at index: {result}")
else:
    print(f"key {key} not found in array.")

