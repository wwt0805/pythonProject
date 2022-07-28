'''
判断素数，给定一个正整数n，请返回1-n中所有的素数
'''


def solve1(n):
    prime_list = []
    for i in range(1, n + 1):  # 2~n的数 i
        for j in range(2, i):  # 2~(n-1)的约数
            if i % j == 0:
                break
            else:
                if j == i - 1:
                    prime_list.append(i)
    print(prime_list)


def is_prime(k):
    for i in range(2, k):
        if k % i == 0:
            return False
    return True


def get_prime(n):
    primes = []
    for i in range(1, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


if __name__ == '__main__':
    solve1(100)
    print(get_prime(100))
