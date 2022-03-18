"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/23 下午3:20
@Site   : 
@File   : HJ31.py
@SoftWare: PyCharm
"""


def hj_31():
    data = input().split(" ")
    res = ""
    for _ in data[::-1]:
        if _.isalnum() == True:
            # print(_, end=" ")
            res += _ + " "
        else:
            res += _ + " "
            res.replace(_, "")
    print(res)


if __name__ == '__main__':
    hj_31()
