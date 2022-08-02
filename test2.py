"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2022/7/31 9:25 上午
@Site    : 
@File    : test2.py
@Software: PyCharm
"""


def exam2():
    try:
        while True:
            n = int(input())
            m = int(input())
            m1 = list(map(int, input().split(" ")))
            k = int(input())

            counts = [1 for _ in range(n)]
            for i in m1:
                counts[i - 1] = 0

            forhead = 0
            behind = 0
            remind = 0
            for behind in range(n):
                k -= 1 - counts[behind]
                while k < 0:
                    k += 1 - counts[forhead]
                    behind += 1
                remind = max(remind, behind - forhead + 1)
            print(remind)
    except:
        print("error")


if __name__ == '__main__':
    print(exam2())
