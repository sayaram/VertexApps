def reverseRec(s: str) -> str:
    print(s)
    if len(s) <= 1:
        return s
    else:
        return reverseRec(s[1:]) + s[0]

def reverseLoop(s: str) -> str:
    str = ""
    for i in s:
        str = i + str
    return str

txt = "Sayaram Gattu"
print(reverseRec(txt))
print(reverseLoop(txt))