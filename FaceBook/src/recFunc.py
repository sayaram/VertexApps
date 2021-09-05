def sumNums(num):
    if num <= 1:
        return num
    return num + sumNums(num - 1)

if __name__ == '__main__':
    print(sumNums(100))
