def main():
    content = input()
    content_ord = sorted(list(map(lambda x: ord(x), content)))
    content_list = list(map(lambda x: chr(x), content_ord))
    res = "".join(content_list)
    print(res)


if __name__ == '__main__':
    main()
