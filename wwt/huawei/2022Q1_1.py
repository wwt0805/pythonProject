def main():
    input_num = input()
    input_cont = input().split(" ")
    input_cont = list(map(int, input_cont))
    output_num = eval(input())
    if int(min(input_cont)) >= 0 and int(max(input_num)) <= 1000:
        a = sorted(list(input_cont))
        print(a)
        a = list(map(int, a))
        max_list = a[-output_num::]
        min_list = a[0:output_num]
        for i in min_list:
            if i in max_list:
                print("-1")
                break
        else:
            print(int(sum(max_list)) + int(sum(min_list)))
    else:
        print("input out of range")


if __name__ == '__main__':
    main()
