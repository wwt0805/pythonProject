"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/22 下午3:46
@Site   : 
@File   : HJ21.py
@SoftWare: PyCharm
"""


def hj_21():
    data = input()
    output = ""
    for item in data:
        if item.isupper():
            if item != "Z":
                item = chr(ord(item.lower()) + 1)
                output += item
            else:
                item = chr(ord(item.lower()) - 25)
                output += item
        elif item.islower():
            if item in "abc":
                output += "2"
            elif item in "def":
                output += "3"
            elif item in "ghi":
                output += "4"
            elif item in "jkl":
                output += "5"
            elif item in "mno":
                output += "6"
            elif item in "pqrs":
                output += "7"
            elif item in "tuv":
                output += "8"
            elif item in "wxyz":
                output += "9"
        else:
            output += item
    print(output)


if __name__ == '__main__':
    hj_21()
