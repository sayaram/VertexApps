
def wordCount(str):
    lst = str.split(" ")
    dic = {}
    for word in lst:
        if word in dic.keys():
            dic[word] = dic[word] +1
        else:
            dic[word] = 1
    for x, y in dic.items():
        print(x + "=")


if __name__ == '__main__':
    wordCount("Sayaram Gattu Mayukh Gattu Vishali Jangam")
