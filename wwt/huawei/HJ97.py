def hj_97():
    num = input()
    num_series = input().split(' ')
    positive_list = []
    negative_list = []
    for i in list(num_series):
        if int(i) < 0:
            negative_list.append(int(i))
        elif int(i) > 0:
            positive_list.append(int(i))
    if len(positive_list) != 0:
        print(len(negative_list), round(sum(positive_list) / len(positive_list), 1))
    else:
        print(len(negative_list), 0.0)


if __name__ == '__main__':
    hj_97()
