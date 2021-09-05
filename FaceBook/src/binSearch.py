def binSearch(arr: list[int], low: int, high: int, seek: int) -> int:
    if high >= low:
        mid = (high + low) // 2
        if arr[mid] == seek:
            return mid
        elif arr[mid] > seek:
            return binSearch(arr, low, mid - 1, seek)
        else:
            return binSearch(arr, mid + 1, high, seek)
    else:
        return -1
    
if __name__ == '__main__':
    arr = [20, 40, 10, 5, 6, 90, 104, 101, 2, 58, 9, 22, 45, 19, 3, 4, 34]
    arr.sort()
    print(binSearch(arr, 0, len(arr) - 1, 22))
