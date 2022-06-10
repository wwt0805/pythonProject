def hj_108():
    """
    最小公倍数=两数乘积 / 两数最大公约数
    :return:
    """
    a, b = input().split(" ")
    a, b = int(a), int(b)
    store_a = []
    store_b = []
    store_com = []
    for i in range(1, a + 1):  # a的因数
        if a % i == 0:
            store_a.append(i)
    for j in range(1, b + 1):
        if b % j == 0:
            store_b.append(j)
    for i in store_a:
        if i in store_b:
            store_com.append(i)
    res = a * b / max(store_com)
    print(int(res))


if __name__ == '__main__':
    hj_108()
