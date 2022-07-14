def hj_35():
    num = int(input())
    for index in range(1, num):
        for column in range(index, num, column + 1):
            print(column, end=" ")


if __name__ == '__main__':
    hj_35()
