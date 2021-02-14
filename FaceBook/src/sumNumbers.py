def findSumNums(arr, num):
    stnum = set()
    for i in arr:
        diff = num - i
        if i in stnum:
            return str(i) + "+" + str(diff)
        else:
            stnum.add(diff)


if __name__ == '__main__':
    li = [1, 4, 5, 7, 9, 12]
    su = 12
    print(findSumNums(li, su))
