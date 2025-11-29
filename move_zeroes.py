def moveZerosToEnd(arr: List[int]) -> List[int]:
    s = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[i], arr[s] = arr[s], arr[i]
            s += 1
    return arr