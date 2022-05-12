def main(lst, item):
    for i in lst:
        if i == item:
            return lst.index(i)
    else:
        return '不存在'


if __name__ == '__main__':
    print(main([1, 3, 2, 3, 5, 1, 1], 3))
