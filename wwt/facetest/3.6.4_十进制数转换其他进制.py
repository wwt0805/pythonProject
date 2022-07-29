def int2str(v, b):
    s = ''
    c = '0'
    while v > 0:
        d = v % b
        if 0 <= d <= 9:
            c = chr(ord("0") + d)
        elif d >= 10:
            c = chr(ord("A") + d - 10)
        s = c + s
        b = int(v / b)
    return s


if __name__ == '__main__':
    print(int2str(26, 16))
