def hj_96():
    content = input()
    store_list = []
    for i in content:
        if len(store_list) == 0:
            store_list.append(i)
        else:
            if store_list[-1].isdigit() and i.isdigit() is False:
                store_list.append("*")
            if store_list[-1].isdigit() is False and i.isdigit():
                store_list.append("*")
                store_list.append(i)
            else:
                store_list.append(i)
    if len(store_list) == 1:
        print(store_list[0])
    else:
        if store_list[-1].isdigit() is False:
            store_list.append("*")
            print("".join(store_list))
        else:
            store_list.insert(0, "*")
            print("".join(store_list))


if __name__ == '__main__':
    hj_96()
