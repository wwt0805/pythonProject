def hj_37():
    month = int(input())
    i = 1
    res = 0
    while True:
        current = month - 2 * i
        if current <= 0:
            print(res + i - 1)
            break
        else:
            res += current
            i += 1


if __name__ == '__main__':
    hj_37()
