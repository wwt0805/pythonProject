def main(lst):
    result = []
    avg = sum(lst) / len(lst)
    for i in lst:
        if i >= avg:
            result.append(i)
    return result


if __name__ == '__main__':
    main([3, 4, 5, 6, 1, 5, 6, 7, 10, 999, 345])
