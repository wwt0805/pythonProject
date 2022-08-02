"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2022/7/31 10:44 上午
@Site    :
@File    : test3_1.py
@Software: PyCharm
"""


def exam3():
    content = input()
    tmp_list = []
    l = len(content)
    endline = l - 1
    while endline >= 0:
        if not content[endline].isdigit():
            tmp_list.append(content[endline])
            endline -= 1
        else:
            num = ''
            res = ''
            while endline >= 0 and content[endline].isdigit():
                num = content[endline] + num
                endline -= 1
            while tmp_list[-1] != ']':
                ls = tmp_list.pop()
                if ls != "[":
                    res += ls
            tmp_list.pop()
            res = int(num) * res
            tmp_list.append(res)
    tmp_list.reverse()
    print("".join([x for x in tmp_list if x not in "[]"]))


if __name__ == '__main__':
    exam3()
