def moveZeros(li):
    if len(li) <= 1:
        pass
    read_index = len(li) - 1
    write_index = len(li) - 1
    while read_index >= 0:
        if li[read_index] != 0:
            li[write_index] = li[read_index]
            write_index -= 1
        read_index -= 1
    while write_index >= 0:
        li[write_index] = 0
        write_index -= 1

li = [1, 10, 0, 65, 0, 20, 30, 90, 0, 56]
moveZeros(li)
print(li)
