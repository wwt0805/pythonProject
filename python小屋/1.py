# 阶乘

def main(n):
    init = 1
    for i in range(1, n + 1):
        init = init * i
    return init


if __name__ == '__main__':
    main(3)
