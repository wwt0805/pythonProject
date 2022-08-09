'''
假定有两个字符串表示整型数，要求写一个函数，实现两个数字字符串相乘，函数返回值也是字符串
'''


def multiply(a: str, b: str):
    end = len(b) - 1
    acc = 0
    base = 0
    while end >= 0:
        acc += int(a) * int(b[end]) * (10 ** base)
        base += 1
        end -= 1
    print(acc)


if __name__ == '__main__':
    multiply('1234', '5678')
