def list_of_unique_values(orig_list):
    return [n for n in orig_list if orig_list.count(n) == 1]


orig_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

print(list_of_unique_values(orig_list))
