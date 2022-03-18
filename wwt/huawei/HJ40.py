"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/24 下午2:29
@Site   : 
@File   : HJ40.py
@SoftWare: PyCharm
"""


def hj_40():
    data = input()
    alpha_counts = 0
    empty_counts = 0
    number_counts = 0
    other_counts = 0
    for item in data:
        if item.isalpha() == True:
            alpha_counts += 1
        elif item.isspace() == True:
            empty_counts += 1
        elif item.isnumeric() == True:
            number_counts += 1
        else:
            other_counts += 1
    print(alpha_counts)
    print(empty_counts)
    print(number_counts)
    print(other_counts)


if __name__ == '__main__':
    hj_40()
