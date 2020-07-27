

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
arr = ["hello","good","hey","how","do"]

for h in range(len(arr) - 1):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
            print(arr)
