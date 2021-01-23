def cummulativeSum(numbers):
    pos = []
    for num in numbers:
        if len(pos) <= 0:
            pos.append(num)
        else:
            pos.append(pos[-1] + num)
    return pos


if __name__ == '__main__':
    print(cummulativeSum([1, -1, 3]))
