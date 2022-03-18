"""
conding = utf-8
@Author : Wu Wentong
@Time   : 2022/3/18 下午1:53
@Site   : 
@File   : HJ17.py
@SoftWare: PyCharm
"""


def hj_17():
    location = [0, 0]
    data = input().split(";")
    for item in data:
        # if item[0] in ["A", "S", "D", "W"] and item[1] not in ["A", "S", "D", "W"] and item[-1].isnumeric() and len(
        # item) <= 3:
        if item != "" and item[0] in ["A", "S", "D", "W"]:
            if len(item) >= 2 and item[1:].isnumeric() == True:
                if item[0] == "A":
                    location[0] = location[0] - int(item[1:])
                if item[0] == "D":
                    location[0] = location[0] + int(item[1:])
                if item[0] == "S":
                    location[1] = location[1] - int(item[1:])
                if item[0] == "W":
                    location[1] = location[1] + int(item[1:])
    print(str(location[0]) + "," + str(location[1]))


if __name__ == '__main__':
    hj_17()
