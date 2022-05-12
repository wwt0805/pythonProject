def main(lst):
    tem = []
    for i in lst:
        if i not in tem:
            tem.append(i)
    print(tem)


if __name__ == '__main__':
    main([1, 2, 3, 1, 4])
