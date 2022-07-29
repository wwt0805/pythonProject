def hj_62(n, jz):
    '''
    可参考HJ62
    :param n: 带转换的十进制数
    :param jz: 需要转换的进制
    :return: 进制转换后的结果
    '''
    div = n // jz
    res = n % jz
    if res >= 10:
        res = chr(ord("A") + res - 10)
    store.append(res)
    print(store)
    if div == 0:
        print("".join(str(x) for x in store[::-1]))
    else:
        hj_62(div, jz)


if __name__ == '__main__':
    while True:
        try:
            store = []
            n = int(input())
            hj_62(n, 16)
        except:
            break
