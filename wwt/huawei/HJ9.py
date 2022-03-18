"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/18 上午10:22
@Site   : 
@File   : HJ9.py
@SoftWare: PyCharm
"""


def hj_9():
    data = input()[::-1]
    store = ""
    for _ in data:
        if _ not in store:
            store += _
    print(store)


if __name__ == '__main__':
    hj_9()
