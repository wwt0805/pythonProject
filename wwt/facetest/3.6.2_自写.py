def str2ten(n: str, s: int):
    '''

    :param n: 输入的字符串
    :param s: 对应的进制（不大于16）
    :return: 返回该字符串和进制对应的十进制数
    '''
    value = 0  # 累加求和变量
    base = 1  # 下一位的base，等于当前位的base * base

    stringlength: int = len(n)
    start = stringlength - 1
    while True:
        if "9" >= n[start] >= "0":  # 如果当前值再0和9之间
            v = int(n[start])
        elif "F" >= n[start] >= "A":  # 如果当前值再A-F之间
            v = 10 + ord(n[start]) - ord("A")

        if stringlength - start > 1:  # 第一位无论什么底数都是1
            base *= s
        value += base * v

        if start == 0:
            return value
        else:
            start -= 1


if __name__ == '__main__':
    print(str2ten("1234", 10))
    print(str2ten('1B', 13))
