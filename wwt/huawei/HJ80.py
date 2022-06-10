def hj_80():
    num1 = input()
    content1 = input()
    num2 = input()
    content2 = input()

    content = list(content1.split(" ")) + list(content2.split(" "))
    # content = [int(x) for x in content]
    res = "".join(sorted(content))
    print(res)
    print(len(res))
    i = 0
    while True:
        if res[i] == res[i + 1]:
            res.replace(res[i], "")
            i += 1
            print(i)
            if i == len(res):
                print(res)
                break
        else:
            pass


if __name__ == '__main__':
    hj_80()
