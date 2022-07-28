'''
写一个函数，实现数字不同进制间的转换。函数第一个输入的参数是数字字符串s；第二个是一个整数b1，代表数字的当前进制；第三个参数是整数b2，代表
要转换的进制。其中，1<b2, b1 =16。假设要实现的函数名为numberConvert,那么numberConvert("100",10,16)返回的是100的十六进制0X64
'''


def number_convert(n, b1, b2):
    res10 = int(n, b1)
    print(res10)


if __name__ == '__main__':
    number_convert("0x1B", 16, 13)
