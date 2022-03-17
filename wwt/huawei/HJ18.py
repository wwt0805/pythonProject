"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/17 上午8:58
@Site   : 
@File   : HJ18.py
@SoftWare: PyCharm
"""


def HJ18():
    num = int(input())
    store_dict = {}
    for _ in range(num):
        data = input().split(" ")
        if int(data[0]) in store_dict.keys():
            store_dict[int(data[0])] = store_dict[int(data[0])] + int(data[1])
        else:
            store_dict[int(data[0])] = int(data[1])

    # for k, v in store_dict.items():
    #     print(k, v)
    for i in sorted(store_dict):
        # print((int(i), store_dict[i]))
        print(i, store_dict[i])


if __name__ == '__main__':
    HJ18()
