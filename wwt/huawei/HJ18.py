'''
私网IP范围是：
子网掩码为二进制下前面是连续的1，然后全是0。（例如：255.255.255.32就是一个非法的掩码）（注意二进制下全是1或者全是0均为非法子网掩码）
注意：
1. 类似于【0.*.*.*】和【127.*.*.*】的IP地址不属于上述输入的任意一类，也不属于不合法ip地址，计数时请忽略
2. 私有IP地址和A,B,C,D,E类地址是不冲突的
'''


def hj_18():
    count_a, count_b, count_c, count_d, count_e, count_wrong, count_private = 0, 0, 0, 0, 0, 0, 0
    while True:
        if input() == '':
            print(count_a, count_b, count_c, count_d, count_e, count_wrong, count_private)
            break
        ip, mask = input().split("~")
        # print(ip, mask)
        # print("".join(ip.split('.')))
        if int("".join("1.0.0.0".split('.'))) <= int("".join(ip.split('.'))) <= int(
                "".join("126.255.255.255".split('.'))):
            count_a += 1
            if int("".join("10.0.0.0".split('.'))) <= int("".join(ip.split('.'))) <= int(
                    "".join("10.255.255.255".split('.'))):
                count_private += 1
        if int("".join("128.0.0.0".split('.'))) <= int("".join(ip.split('.'))) <= int(
                "".join("191.255.255.255".split('.'))):
            count_b += 1
            if int("".join("172.16.0.0".split('.'))) <= int("".join(ip.split('.'))) <= int(
                    "".join("172.31.255.255".split('.'))):
                count_private += 1
        if int("".join("192.0.0.0".split('.'))) <= int("".join(ip.split('.'))) <= int(
                "".join("223.255.255.255".split('.'))):
            count_c += 1
            if int("".join("192.168.0.0".split('.'))) <= int("".join(ip.split('.'))) <= int(
                    "".join("192.168.255.255".split('.'))):
                count_private += 1
        if int("".join("224.0.0.0".split('.'))) <= int("".join(ip.split('.'))) <= int(
                "".join("239.255.255.255".split('.'))):
            count_d += 1
        if int("".join(ip.split('.'))) <= int("".join("1.0.0.0".split('.'))):
            count_wrong += 1

        c = map(lambda x: bin(int(x)), mask)


if __name__ == '__main__':
    hj_18()
