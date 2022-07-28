'''
题目描述
若两个正整数的和为素数，则这两个正整数称之为“素数伴侣”，如2和5、6和13，它们能应用于通信加密。现在密码学会请你设计一个程序，从已有的 N
（ N 为偶数）个正整数中挑选出若干对组成“素数伴侣”，挑选方案多种多样，例如有4个正整数：2，5，6，13，
如果将5和6分为一组中只能得到一组“素数伴侣”，而将2和5、6和13编组将得到两组“素数伴侣”，
能组成“素数伴侣”最多的方案称为“最佳方案”，当然密码学会希望你寻找出“最佳方案”。

输入:

有一个正偶数 n ，表示待挑选的自然数的个数。后面给出 n 个具体的数字。

输出:

输出一个整数 K ，表示你求得的“最佳方案”组成“素数伴侣”的对数。
'''


def hj_28():
    num_num = input()
    num_content = input()
    num_list = list((num_content.split(" ")))
    num_list = [int(x) for x in num_list]

    idx_i = 0
    idx_j = 1
    prime_count = 0
    while True:
        if len(num_list) < 2:
            break
        else:
            acc = num_list[idx_i] + num_list[idx_j]
            # print(acc)
            if is_prime(acc) is True:
                prime_count += 1
                print(num_list[idx_i], num_list[idx_j])
                a = num_list[idx_i]
                b = num_list[idx_j]
                num_list.remove(a)
                num_list.remove(b)
                idx_i = 0
                idx_j = 1
            else:
                if idx_j == len(num_list) - 1:
                    idx_i += 1
                    idx_j = idx_i + 1
                    if idx_i == len(num_list) - 1:
                        break
                else:
                    idx_j += 1
    print(prime_count)


def is_prime(n):
    if n == 2:
        return True
    if n > 2:
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                if i == n - 1:
                    return True


if __name__ == '__main__':
    hj_28()
    is_prime(4)
