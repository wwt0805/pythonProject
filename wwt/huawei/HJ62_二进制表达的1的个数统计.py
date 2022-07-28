def hj_62(n):
    div = n // 2
    res = n % 2
    store.append(res)
    if div == 0:
        print(store.count(1))
    else:
        hj_62(div)


if __name__ == '__main__':
    while True:
        try:
            store = []
            n = int(input())
            hj_62(n)
        except:
            break
