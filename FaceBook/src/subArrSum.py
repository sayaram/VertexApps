
def subArraySum(arr, n, s):
    flag = 0
    wsum = 0
    start = 0
    for i in range(n):
        if flag == 0:
            wsum = wsum + arr[i]
            while wsum > s:
                wsum = wsum - arr[start]
                start = start + 1
            if wsum == s:
                flag = 1
                print(start + 1, end=" ")
                print(i +1)
    print('-1')


if __name__ == '__main__':
    N = 5
    S = 12
    A = [1, 2, 3, 7, 5]
    subArraySum(A, N, S)
