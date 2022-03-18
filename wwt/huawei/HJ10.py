"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/18 上午10:37
@Site   : 
@File   : HJ10.py
@SoftWare: PyCharm
"""


def hj10():
    data = input()
    store_str = ""
    for _ in data:
        if _ not in store_str:
            store_str += _
    print(len(store_str))


if __name__ == '__main__':
    hj10()
