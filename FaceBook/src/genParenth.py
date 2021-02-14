def AllParenthesis(num):
    if num <= 1:
        return "("
    return AllParenthesis(num - 1) + ")"


if __name__ == '__main__':
    count = 3
    string = "(" * count
    print(string + AllParenthesis(count))
