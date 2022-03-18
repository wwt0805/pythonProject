"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/22 下午5:28
@Site   : 
@File   : HJ22_test.py
@SoftWare: PyCharm
"""

# record = 0


def bottle(num):
    while True:
        tmp = num // 3
        record = tmp
        if tmp >= 3:
            bottle(tmp)
        else:
            record += 1
            break
        print(record)
        break
        # print(record)


if __name__ == '__main__':
   bottle(10)