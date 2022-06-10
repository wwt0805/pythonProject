def hj_73():
    month_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year, month, day = input().split(' ')
    if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
        print(sum(month_day[:int(month) - 1]) + int(day))
    else:
        if int(month) > 2:
            print(sum(month_day[:int(month) - 1]) + int(day) - 1)
        else:
            print(sum(month_day[:int(month) - 1]) + int(day))


if __name__ == '__main__':
    hj_73()
