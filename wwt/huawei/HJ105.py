def hj_105():
    count_neg = 0
    count_pos = 0
    acc = 0
    while True:
        num = input()
        if int(num) < 0:
            count_neg += 1
        else:
            count_pos += 1
            acc += int(num)
            avg = acc / count_pos
        # if num == "\t":
        #     print(count_neg, avg)
        #     break


if __name__ == '__main__':
    hj_105()
