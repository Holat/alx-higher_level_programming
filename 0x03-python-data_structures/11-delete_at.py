#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return my_list

    new_list = list(range(len(my_list) - 1))
    j = 0
    for i in my_list:
        if i == my_list[idx]:
                continue
        new_list[j] = my_list[j]
        j += 1

    my_list = list(new_list)
    return (new_list)
