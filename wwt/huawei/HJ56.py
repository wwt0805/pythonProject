"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/24 下午4:56
@Site   : 
@File   : HJ56.py
@SoftWare: PyCharm
"""


def hj_56():
    num = int(input())
    store_list = []
    count = 0
    for j in range(3, num + 1):
        for i in range(1, j):
            if j % i == 0:
                store_list.append(i)
        if sum(store_list) == j:
            # print(j)
            count += 1
            store_list = []
        else:
            store_list = []
    print(count)


if __name__ == '__main__':
    hj_56()
