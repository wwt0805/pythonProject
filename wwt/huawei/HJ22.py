"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/22 下午5:00
@Site   : 
@File   : HJ22.py
@SoftWare: PyCharm
"""


def hj_22():
    store_list = []
    while True:
        data = input()
        if data == "0":
            break
        else:
            store_list.append(data)

    for num in store_list:
        while True:
            div = num // 3


if __name__ == '__main__':
    hj_22()
