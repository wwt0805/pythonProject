def hj_107():
    n = float(input())
    last = n
    new = last - ((last ** 3 - n) / (3 * last ** 2))
    while abs(new - last) > 0.000001:  # 精度要求
        last = new
        new = last - ((last ** 3 - n) / (3 * last ** 2))
    print(format(new, '.1f'))


if __name__ == '__main__':
    hj_107()
