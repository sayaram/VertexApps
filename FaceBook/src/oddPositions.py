def oddPositions(elem):
    pos = []
    for x in range(0, len(elem)):
        if (x % 2) > 0 or x == 0:
            pos.append(x)
    return pos

if __name__ == '__main__':
    lst = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(oddPositions(lst))
