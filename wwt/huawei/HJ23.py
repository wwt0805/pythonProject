"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/22 下午5:54
@Site   : 
@File   : HJ23.py
@SoftWare: PyCharm
"""


def hj_23():
    data = input()
    store_list = {}
    for item in data:
        if item in store_list:
            store_list[item] += 1
        else:
            store_list[item] = 1
    # print(store_list)

    for k, v in store_list.items():
        if v == min(store_list.values()):
            data = data.replace(k, "")
    print(data)


if __name__ == '__main__':
    hj_23()
