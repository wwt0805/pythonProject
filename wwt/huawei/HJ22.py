def hj_22():
    while True:
        num = int(input())
        if num == 0:
            break
        else:
            count = 0
            while True:
                coke_num = num // 3
                empty_num = num % 3
                num = coke_num + empty_num
                count += coke_num
                if num == 2:
                    count += 1
                    print(count)
                    break
                elif num < 2:
                    print(count)
                    break


if __name__ == '__main__':
    hj_22()
