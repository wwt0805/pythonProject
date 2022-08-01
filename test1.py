"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2022/7/31 9:25 上午
@Site    : 
@File    : test1.py
@Software: PyCharm
"""


def exam2():
    n = int(input())
    m = int(input())
    m1 = input().split(" ")
    k = int(input())
    # print(n)
    # print(m)
    # print(m1)
    # print(k)

    if "1" not in m1 and str(n) not in m1:
        m1.insert(0, "1")
        m1.insert(-1, n)
    print(m1)




if __name__ == '__main__':
    exam2()