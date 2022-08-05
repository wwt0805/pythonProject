"""
coding=utf-8
@Author  : Wu Wentong
@Time    : 2022/7/31 10:41 上午
@Site    : 
@File    : test3.py
@Software: PyCharm
"""


def exam3():
    content = input()
    sign_list = []
    left_list = []
    right_list = []
    for i in range(len(content)):
        if content[i] == "[":
            sign_list.append("[")
            left_list.append(i)
        if content[i] == "]":
            right_list.append(i)
    print(left_list)
    print(right_list)
    if left_list[-1] < right_list[0]:
        left_start = len(left_list) - 1
        right_start = 0
        tmp_res = ""
        while True:
            res = content[left_list[left_start] + 1: right_list[right_start]]
            tmp_res += res
            left_start -= 1
            print(left_list[left_start])
            res_for = content[left_list[left_start] + 1: left_list[left_start] + 2]
            print(res_for)
            break
            # if left_list[left_start].isdigt():
            #     break


if __name__ == '__main__':
    exam3()
