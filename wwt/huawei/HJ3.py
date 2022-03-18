"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/18 上午10:28
@Site   : 
@File   : HJ3.py
@SoftWare: PyCharm
"""


def hj_3():
    num = int(input())
    store_list = []
    for _ in range(num):
        data = input()
        if data not in store_list:
            store_list.append(data)
    for i in range(len(store_list) - 1):
        for j in range(len(store_list) - i - 1):
            if int(store_list[j]) > int(store_list[j + 1]):
                store_list[j], store_list[j + 1] = store_list[j + 1], store_list[j]
    for _ in store_list:
        print(_)


if __name__ == '__main__':
    hj_3()
