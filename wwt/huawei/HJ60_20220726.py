def hj_60_rep1():
    n = int(input())
    prime_list = [2]
    for i in range(2, n + 1):
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                if j == i - 1:
                    prime_list.append(i)

    minus = n
    num1 = 0
    num2 = 0
    for i in prime_list:
        if n - i in prime_list and abs(n - i - i) < minus:
            minus = abs(n - i - i)
            num1 = i
            num2 = n - i
    print(num1)
    print(num2)


if __name__ == '__main__':
    hj_60_rep1()
