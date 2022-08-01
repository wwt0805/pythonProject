def exam2():
    n = int(input())
    m = int(input())
    m1 = list(map(int, input().split(" ")))
    k = int(input())

    counts = [1 for _ in range(n)]
    for i in m1:
        counts[i - 1] = 0
    # print(counts)

    forhead = 0
    behind = 0
    remind = 0
    for behind in range(n):
        k -= 1 - counts[behind]
        while k < 0:
            k += 1 - counts[forhead]
            forhead += 1
        remind = max(remind, behind - forhead + 1)
    return remind


if __name__ == '__main__':
    print(exam2())