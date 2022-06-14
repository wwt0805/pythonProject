def hj_102():
    content = input()
    dictionary = {}
    for i in content:
        dictionary[i] = dictionary.get(i, 0) + 1
    a = sorted(dictionary.items(), key=lambda x: x[1], reverse=True)
    print(a)
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j][1] == a[j + 1][1]:
                if ord(a[j][0]) > ord(a[j + 1][0]):
                    a[j], a[j + 1] = a[j + 1], a[j]
    for i in a:
        print(i[0], end="")


if __name__ == '__main__':
    hj_102()
