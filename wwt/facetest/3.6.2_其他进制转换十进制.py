'''
把s表示的数字字符串转换成b进制数
'''


def str2int(s, b):
    val = 0
    base = 1
    i = len(s) - 1
    while i >= 0:
        c = s[i]
        v = 0
        # 把字符串转换成对应的数字
        if '0' <= c <= '9':
            v = ord(c) - ord('0')
        # 如果超过9，判断其是否属于十六进制的'A'到'E'之间
        if 'A' <= c <= 'E':
            v = 10 + ord(c) - ord('A')
        if i < len(s) - 1:
            '''
            每次读取一个数字就要乘以相应进位，例如s='1234'，读取4时val=4，读取3时val=3*10+4 以此类推
            '''
            base *= b
        val += v * base
        i -= 1
    return val


if __name__ == '__main__':
    print(str2int('1234', 5))
    print(str2int('1B', 13))
