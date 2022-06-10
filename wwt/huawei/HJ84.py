def hj_84():
    content = input()
    count = 0
    for i in content:
        if ord("Z") >= ord(i) >= ord("A"):
            count += 1
    print(count)


if __name__ == '__main__':
    hj_84()
