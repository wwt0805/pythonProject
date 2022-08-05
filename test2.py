"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2022/7/31 9:25 上午
@Site    :
            近些年来，我国防沙治沙取得显著成果。某沙漠新种植N棵胡杨（编号1-N），排成一排。一个月后，有M棵胡杨未能成活。
            现可补种胡杨K棵，请问如何补种（只能补种，不能新种），可以得到最多的连续胡杨树？
            输入描述:
            N 总种植数量 1<=N<=100000 M 未成活胡杨数量 1<=M<=N M 个空格分隔的数，按编号从小到大排列 K 最多可以补种的数量 0<=K<=M
            输出描述:
            最多的连续胡杨棵树
            示例1
            输入
            5
            2
            2 4
            1
            输出
            3
            说明
            补种到2或4结果一样，最多的连续胡杨棵树都是3
            示例2
            输入
            10
            3
            2 4 7
            1
            输出
            6
            说明
            补种第7棵树，最多的连续胡杨棵树为6(5,6,7,8,9,10)
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
