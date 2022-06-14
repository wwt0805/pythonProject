def hj_5():
    content = input()
    dictionary = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    i = 1
    total = 0
    while True:
        total += pow(16, i - 1) * dictionary.index(content[-i])
        i += 1
        if i == len(content) - 1:
            print(total)
            break


if __name__ == '__main__':
    hj_5()
