def main(num):
    tem = []
    t1 = num / pow(10, len(str(num)) - 1)
    tem.append(int(t1))
    result1 = str(t1).split(".")
    if len(result1[-1]) == 1:
        tem.append(int(result1[-1]))
        return print(sum(tem))

    else:
        main(int(result1[-1]))


if __name__ == '__main__':
    main(16)
